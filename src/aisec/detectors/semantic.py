"""Semantic detector placeholder.

Semantic judgment is intentionally manual in the foundation. A future vetted evaluator
can implement this interface without changing vulnerability pack metadata.
"""

from __future__ import annotations

from aisec.detectors.base import DetectionResult
from aisec.targets.base import TargetResponse


class ManualReviewDetector:
    name = "manual_review"

    def __init__(self, detector_type: str = "semantic") -> None:
        self.detector_type = detector_type

    def detect(self, response: TargetResponse) -> DetectionResult:
        return DetectionResult(
            detector=self.detector_type,
            matched=False,
            confidence=0.0,
            summary="Detector requires manual review or a custom implementation.",
            evidence={"response_length": len(response.text)},
        )
