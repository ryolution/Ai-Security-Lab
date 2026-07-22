"""Regular-expression detector."""

from __future__ import annotations

import re

from aisec.detectors.base import DetectionResult
from aisec.targets.base import TargetResponse


class RegexDetector:
    name = "regex"

    def __init__(self, patterns: list[str]) -> None:
        self.patterns = [re.compile(pattern) for pattern in patterns]

    def detect(self, response: TargetResponse) -> DetectionResult:
        for pattern in self.patterns:
            match = pattern.search(response.text)
            if match:
                return DetectionResult(
                    detector=self.name,
                    matched=True,
                    confidence=0.9,
                    summary="Regex indicator matched target response.",
                    evidence={"pattern": pattern.pattern, "match": match.group(0)},
                )
        return DetectionResult(
            detector=self.name,
            matched=False,
            confidence=0.9,
            summary="No regex indicators were found.",
            evidence={"checked_patterns": len(self.patterns)},
        )
