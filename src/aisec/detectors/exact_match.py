"""Exact text matching detector."""

from __future__ import annotations

from aisec.detectors.base import DetectionResult
from aisec.targets.base import TargetResponse


class ExactMatchDetector:
    name = "exact_match"

    def __init__(self, patterns: list[str]) -> None:
        self.patterns = patterns

    def detect(self, response: TargetResponse) -> DetectionResult:
        for pattern in self.patterns:
            if pattern and pattern in response.text:
                return DetectionResult(
                    detector=self.name,
                    matched=True,
                    confidence=1.0,
                    summary="Exact indicator found in target response.",
                    evidence={"pattern": pattern},
                )
        return DetectionResult(
            detector=self.name,
            matched=False,
            confidence=1.0,
            summary="No exact indicators were found.",
            evidence={"checked_patterns": len(self.patterns)},
        )
