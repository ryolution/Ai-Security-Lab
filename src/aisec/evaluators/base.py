"""Evaluator contracts."""

from __future__ import annotations

from dataclasses import dataclass

from aisec.core.result import ERROR, FAIL, INCONCLUSIVE, PASS, Status, TestResult
from aisec.detectors.base import DetectionResult


@dataclass(frozen=True)
class EvaluationInput:
    vulnerability_id: str
    test_id: str
    target_id: str
    detections: list[DetectionResult]
    error: str | None = None


class VulnerabilityEvaluator:
    """Default evaluator for vulnerability tests.

    Matching detectors indicate unsafe behavior and therefore produce FAIL.
    """

    def evaluate(self, item: EvaluationInput) -> TestResult:
        if item.error:
            return TestResult(
                vulnerability_id=item.vulnerability_id,
                test_id=item.test_id,
                target_id=item.target_id,
                status=ERROR,
                score=None,
                confidence=0.0,
                summary="Test execution failed.",
                evidence={},
                error=item.error,
            )

        if not item.detections:
            return TestResult(
                vulnerability_id=item.vulnerability_id,
                test_id=item.test_id,
                target_id=item.target_id,
                status=INCONCLUSIVE,
                score=None,
                confidence=0.0,
                summary="No detector evidence was produced.",
            )

        matched = [detection for detection in item.detections if detection.matched]
        status: Status = FAIL if matched else PASS
        confidence = max((detection.confidence for detection in item.detections), default=0.0)
        return TestResult(
            vulnerability_id=item.vulnerability_id,
            test_id=item.test_id,
            target_id=item.target_id,
            status=status,
            score=1.0 if matched else 0.0,
            confidence=confidence,
            summary="Unsafe behavior detected." if matched else "No unsafe behavior detected.",
            evidence={"detections": [detection.__dict__ for detection in item.detections]},
        )
