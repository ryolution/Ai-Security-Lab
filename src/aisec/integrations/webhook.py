"""Webhook payload helpers."""

from __future__ import annotations

from aisec.core.result import ScanReport


def webhook_payload(report: ScanReport) -> dict[str, object]:
    failing = [result.to_dict() for result in report.results if result.status == "FAIL"]
    return {
        "framework": report.framework,
        "target": report.target,
        "started_at": report.started_at,
        "finished_at": report.finished_at,
        "failing_count": len(failing),
        "failing_results": failing,
    }
