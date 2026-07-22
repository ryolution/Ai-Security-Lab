"""Mitigation evaluation helpers."""

from __future__ import annotations

from aisec.core.result import PASS, TestResult


def mitigation_noted(vulnerability_id: str, target_id: str, summary: str) -> TestResult:
    return TestResult(
        vulnerability_id=vulnerability_id,
        test_id="mitigation",
        target_id=target_id,
        status=PASS,
        score=None,
        confidence=0.0,
        summary=summary,
        evidence={"manual_validation_required": True},
    )
