"""Regression comparison helpers."""

from __future__ import annotations

from aisec.core.result import FAIL, PASS, Status


def compare_expected(actual: Status, expected: Status) -> Status:
    if actual == expected:
        return PASS
    return FAIL
