"""Severity helpers for findings and manifests."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class SeverityLevel(StrEnum):
    INFO = "info"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass(frozen=True)
class Severity:
    level: SeverityLevel
    score: float | None = None
    exploitability: int | None = None
    confidentiality: int | None = None
    integrity: int | None = None
    availability: int | None = None
    autonomy: int | None = None
    confidence: int | None = None

    @classmethod
    def from_mapping(cls, value: dict[str, object]) -> Severity:
        level = SeverityLevel(str(value.get("level", "info")))
        score = value.get("score")
        return cls(
            level=level,
            score=float(score) if isinstance(score, int | float) else None,
            exploitability=_optional_int(value.get("exploitability")),
            confidentiality=_optional_int(value.get("confidentiality")),
            integrity=_optional_int(value.get("integrity")),
            availability=_optional_int(value.get("availability")),
            autonomy=_optional_int(value.get("autonomy")),
            confidence=_optional_int(value.get("confidence")),
        )


def _optional_int(value: object) -> int | None:
    return int(value) if isinstance(value, int) else None


def score_to_level(score: float | None) -> SeverityLevel:
    if score is None:
        return SeverityLevel.INFO
    if score >= 9:
        return SeverityLevel.CRITICAL
    if score >= 7:
        return SeverityLevel.HIGH
    if score >= 4:
        return SeverityLevel.MEDIUM
    if score > 0:
        return SeverityLevel.LOW
    return SeverityLevel.INFO
