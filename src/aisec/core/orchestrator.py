"""Safe scan orchestration for vulnerability packs."""

from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path
from uuid import uuid4

from aisec import __version__
from aisec.core.exceptions import AuthorizationError
from aisec.core.result import PASS, SKIPPED, ScanReport, TestResult
from aisec.core.scan_context import PolicyConfig, ScanContext, TargetConfig
from aisec.registry.discovery import VulnerabilityPack, discover_vulnerability_packs
from aisec.registry.loader import load_cases, load_manifest


class SecurityOrchestrator:
    """Coordinates pack selection and safe placeholder execution.

    The foundation does not auto-exploit targets. Until a vulnerability pack provides
    vetted probes and detectors, cases are reported as skipped with explicit evidence.
    """

    def __init__(self, context: ScanContext) -> None:
        self.context = context

    def run(self) -> ScanReport:
        self._enforce_authorization()
        started = _now()
        packs = self._select_packs(discover_vulnerability_packs(self.context.registry_root))
        results: list[TestResult] = []

        for pack in packs:
            results.extend(self._evaluate_pack(pack))

        finished = _now()
        return ScanReport(
            framework={"name": "ai-security-lab", "version": __version__},
            target={"id": self.context.target.id, "type": self.context.target.type},
            policy=self.context.policy.raw or {"name": self.context.policy.name},
            started_at=started,
            finished_at=finished,
            results=results,
            metadata={
                "scan_id": self.context.scan_id,
                "selected_packs": [str(pack.path) for pack in packs],
            },
        )

    def _enforce_authorization(self) -> None:
        if (
            self.context.policy.authorization_required
            and not self.context.target.authorization_confirmed
        ):
            msg = (
                "Target authorization is not confirmed. Set "
                "authorization.confirmed: true only for systems you are allowed to test."
            )
            raise AuthorizationError(msg)

    def _select_packs(self, packs: list[VulnerabilityPack]) -> list[VulnerabilityPack]:
        selected: list[VulnerabilityPack] = []
        category_filter = set(self.context.categories)
        id_filter = set(self.context.vulnerability_ids)

        for pack in packs:
            manifest = load_manifest(pack.manifest_path)
            if category_filter and manifest.get("category") not in category_filter:
                continue
            if id_filter and manifest.get("id") not in id_filter:
                continue
            selected.append(pack)

        return selected

    def _evaluate_pack(self, pack: VulnerabilityPack) -> list[TestResult]:
        manifest = load_manifest(pack.manifest_path)
        cases = load_cases(pack.path / "cases.yml")
        vulnerability_id = str(manifest.get("id", pack.path.name))
        required = set(manifest.get("requirements", {}).get("target_capabilities", []))
        available = set(self.context.target.capabilities)

        if required and not required.issubset(available):
            return [
                TestResult(
                    vulnerability_id=vulnerability_id,
                    test_id="compatibility",
                    target_id=self.context.target.id,
                    status=SKIPPED,
                    score=None,
                    confidence=0.0,
                    summary="Target does not declare the capabilities required by this pack.",
                    evidence={
                        "required_capabilities": sorted(required),
                        "target_capabilities": sorted(available),
                    },
                )
            ]

        results: list[TestResult] = []
        for case in cases:
            test_id = str(case.get("id", "case"))
            results.append(
                TestResult(
                    vulnerability_id=vulnerability_id,
                    test_id=test_id,
                    target_id=self.context.target.id,
                    status=PASS if case.get("static_expected_status") == PASS else SKIPPED,
                    score=None,
                    confidence=0.0,
                    summary="Case loaded. Manual probe and detector execution is required.",
                    evidence={
                        "pack": str(pack.path),
                        "case_name": case.get("name", test_id),
                        "manual_validation_required": True,
                    },
                )
            )

        if results:
            return results

        return [
            TestResult(
                vulnerability_id=vulnerability_id,
                test_id="no-cases",
                target_id=self.context.target.id,
                status=SKIPPED,
                score=None,
                confidence=0.0,
                summary="Vulnerability pack has no cases.yml entries yet.",
                evidence={"pack": str(pack.path)},
            )
        ]


def build_scan_context(
    target: TargetConfig,
    policy: PolicyConfig,
    registry_root: Path,
    categories: tuple[str, ...] = (),
    vulnerability_ids: tuple[str, ...] = (),
) -> ScanContext:
    return ScanContext(
        target=target,
        policy=policy,
        registry_root=registry_root,
        scan_id=str(uuid4()),
        categories=categories,
        vulnerability_ids=vulnerability_ids,
    )


def _now() -> str:
    return datetime.now(UTC).isoformat()
