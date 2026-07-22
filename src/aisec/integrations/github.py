"""GitHub integration helpers."""

from __future__ import annotations

from aisec.core.result import ScanReport


def github_step_summary(report: ScanReport) -> str:
    failing = sum(1 for result in report.results if result.status == "FAIL")
    total = len(report.results)
    return f"AI Security Lab: {failing} failing finding(s) across {total} result(s)."
