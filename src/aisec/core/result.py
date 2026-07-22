"""Normalized scan and regression results."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

Status = Literal["PASS", "FAIL", "INCONCLUSIVE", "ERROR", "SKIPPED"]

PASS: Status = "PASS"  # noqa: S105
FAIL: Status = "FAIL"
INCONCLUSIVE: Status = "INCONCLUSIVE"
ERROR: Status = "ERROR"
SKIPPED: Status = "SKIPPED"


@dataclass(frozen=True)
class TestResult:
    """A normalized result for a single vulnerability test case."""

    __test__ = False

    vulnerability_id: str
    test_id: str
    target_id: str
    status: Status
    score: float | None
    confidence: float
    summary: str
    evidence: dict[str, Any] = field(default_factory=dict)
    error: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "vulnerability_id": self.vulnerability_id,
            "test_id": self.test_id,
            "target_id": self.target_id,
            "status": self.status,
            "score": self.score,
            "confidence": self.confidence,
            "summary": self.summary,
            "evidence": self.evidence,
            "error": self.error,
        }


@dataclass(frozen=True)
class ScanReport:
    """Report payload shared by all report renderers."""

    framework: dict[str, str]
    target: dict[str, Any]
    policy: dict[str, Any]
    started_at: str
    finished_at: str
    results: list[TestResult]
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "framework": self.framework,
            "target": self.target,
            "policy": self.policy,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "metadata": self.metadata,
            "results": [result.to_dict() for result in self.results],
        }
