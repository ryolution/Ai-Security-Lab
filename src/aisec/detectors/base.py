"""Detector contracts and factory helpers."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol

from aisec.targets.base import TargetResponse


@dataclass(frozen=True)
class DetectionResult:
    detector: str
    matched: bool
    confidence: float
    summary: str
    evidence: dict[str, Any] = field(default_factory=dict)


class Detector(Protocol):
    name: str

    def detect(self, response: TargetResponse) -> DetectionResult:
        """Analyze a target response."""


def build_detector(config: dict[str, Any]) -> Detector:
    detector_type = str(config.get("type", ""))
    if detector_type == "exact_match":
        from aisec.detectors.exact_match import ExactMatchDetector

        return ExactMatchDetector(patterns=[str(item) for item in config.get("patterns", [])])
    if detector_type == "regex":
        from aisec.detectors.regex import RegexDetector

        return RegexDetector(patterns=[str(item) for item in config.get("patterns", [])])
    if detector_type == "canary":
        from aisec.detectors.canary import CanaryDetector

        return CanaryDetector(canaries=[str(item) for item in config.get("canaries", [])])
    if detector_type == "tool_call":
        from aisec.detectors.tool_call import ToolCallDetector

        forbidden_tools = [str(item) for item in config.get("forbidden_tools", [])]
        return ToolCallDetector(forbidden_tools=forbidden_tools)
    if detector_type == "policy_violation":
        from aisec.detectors.policy_violation import PolicyViolationDetector

        forbidden_actions = [str(item) for item in config.get("forbidden_actions", [])]
        return PolicyViolationDetector(forbidden_actions=forbidden_actions)

    from aisec.detectors.semantic import ManualReviewDetector

    return ManualReviewDetector(detector_type=detector_type or "manual")
