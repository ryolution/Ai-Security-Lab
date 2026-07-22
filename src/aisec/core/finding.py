"""Finding model used by reports and integrations."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from aisec.core.result import Status
from aisec.core.severity import SeverityLevel


@dataclass(frozen=True)
class Finding:
    vulnerability_id: str
    test_id: str
    target_id: str
    status: Status
    severity: SeverityLevel
    confidence: float
    summary: str
    evidence: dict[str, Any] = field(default_factory=dict)
    mitigation: str | None = None
    references: list[str] = field(default_factory=list)

    @property
    def is_failing(self) -> bool:
        return self.status == "FAIL"
