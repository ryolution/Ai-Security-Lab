from __future__ import annotations

from aisec.detectors.canary import CanaryDetector
from aisec.detectors.tool_call import ToolCallDetector
from aisec.targets.base import TargetResponse


def test_canary_detector_matches_response_text() -> None:
    detector = CanaryDetector(["AIV_CANARY"])

    result = detector.detect(TargetResponse(text="leaked AIV_CANARY"))

    assert result.matched is True
    assert result.confidence == 1.0


def test_tool_call_detector_matches_forbidden_tool() -> None:
    detector = ToolCallDetector(["execute_shell"])

    result = detector.detect(
        TargetResponse(text="", tool_calls=[{"name": "execute_shell", "arguments": {}}])
    )

    assert result.matched is True
    assert result.evidence["tool"] == "execute_shell"
