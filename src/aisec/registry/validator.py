"""Validation for vulnerability packs."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from aisec.core.exceptions import RegistryError
from aisec.registry.discovery import VulnerabilityPack
from aisec.registry.loader import load_cases, load_manifest

REQUIRED_PACK_FILES = (
    "manifest.yml",
    "README.md",
    "cases.yml",
    "secure/mitigation.md",
    "regression/vulnerable.expected.yml",
    "regression/secured.expected.yml",
    "references.md",
)

VALID_CATEGORIES = {
    "prompt-injection",
    "information-disclosure",
    "rag",
    "agents",
    "mcp",
    "models",
    "multimodal",
    "supply-chain",
    "resource-abuse",
}


@dataclass(frozen=True)
class RegistryIssue:
    path: Path
    message: str
    severity: str = "error"


def validate_pack(pack: VulnerabilityPack) -> list[RegistryIssue]:
    issues: list[RegistryIssue] = []
    for relative in REQUIRED_PACK_FILES:
        if not (pack.path / relative).exists():
            issues.append(RegistryIssue(pack.path / relative, "required file is missing"))

    if issues and not pack.manifest_path.exists():
        return issues

    try:
        manifest = load_manifest(pack.manifest_path)
    except Exception as exc:
        return [RegistryIssue(pack.manifest_path, str(exc))]

    issues.extend(_validate_manifest_shape(pack.manifest_path, manifest))
    cases_path = pack.path / "cases.yml"
    if cases_path.exists():
        issues.extend(_validate_cases(cases_path))
    return issues


def validate_unique_ids(packs: list[VulnerabilityPack]) -> list[RegistryIssue]:
    seen: dict[str, Path] = {}
    issues: list[RegistryIssue] = []
    for pack in packs:
        try:
            manifest = load_manifest(pack.manifest_path)
        except RegistryError:
            continue
        vulnerability_id = str(manifest.get("id", ""))
        if not vulnerability_id:
            continue
        if vulnerability_id in seen:
            issues.append(
                RegistryIssue(
                    pack.manifest_path,
                    (
                        f"duplicate vulnerability id {vulnerability_id}; "
                        f"first seen at {seen[vulnerability_id]}"
                    ),
                )
            )
        else:
            seen[vulnerability_id] = pack.manifest_path
    return issues


def _validate_manifest_shape(path: Path, manifest: dict[str, Any]) -> list[RegistryIssue]:
    issues: list[RegistryIssue] = []
    required = {
        "id",
        "name",
        "slug",
        "version",
        "status",
        "category",
        "severity",
        "requirements",
        "probe",
        "detectors",
        "mitigations",
        "safe_by_default",
        "created",
        "updated",
    }
    for key in sorted(required - set(manifest)):
        issues.append(RegistryIssue(path, f"manifest missing required field: {key}"))

    vulnerability_id = manifest.get("id")
    if isinstance(vulnerability_id, str) and not re.fullmatch(r"AIV-[0-9]{4}", vulnerability_id):
        issues.append(RegistryIssue(path, "id must match AIV-XXXX"))

    category = manifest.get("category")
    if isinstance(category, str) and category not in VALID_CATEGORIES:
        issues.append(RegistryIssue(path, f"unknown category: {category}"))

    detectors = manifest.get("detectors")
    if "detectors" in manifest and not _is_non_empty_list(detectors):
        issues.append(RegistryIssue(path, "detectors must be a non-empty list"))

    mitigations = manifest.get("mitigations")
    if "mitigations" in manifest and not isinstance(mitigations, list):
        issues.append(RegistryIssue(path, "mitigations must be a list"))

    return issues


def _validate_cases(path: Path) -> list[RegistryIssue]:
    issues: list[RegistryIssue] = []
    try:
        cases = load_cases(path)
    except Exception as exc:
        return [RegistryIssue(path, str(exc))]

    seen: set[str] = set()
    for index, case in enumerate(cases):
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id:
            issues.append(RegistryIssue(path, f"case at index {index} is missing id"))
            continue
        if case_id in seen:
            issues.append(RegistryIssue(path, f"duplicate case id: {case_id}"))
        seen.add(case_id)
        if "detectors" not in case:
            issues.append(RegistryIssue(path, f"case {case_id} missing detectors"))
    return issues


def _is_non_empty_list(value: object) -> bool:
    return isinstance(value, list) and bool(value)
