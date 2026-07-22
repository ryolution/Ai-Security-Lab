from __future__ import annotations

from aisec.core.result import ScanReport, TestResult
from aisec.reporting.json_report import render_json
from aisec.reporting.markdown_report import render_markdown


def test_report_renderers_include_result_status() -> None:
    report = ScanReport(
        framework={"name": "ai-security-lab", "version": "0.1.0"},
        target={"id": "target", "type": "test"},
        policy={"name": "default"},
        started_at="2026-07-22T00:00:00+00:00",
        finished_at="2026-07-22T00:00:01+00:00",
        results=[
            TestResult(
                vulnerability_id="AIV-0001",
                test_id="AIV-0001-T01",
                target_id="target",
                status="PASS",
                score=0.0,
                confidence=1.0,
                summary="No unsafe behavior detected.",
            )
        ],
    )

    assert '"status": "PASS"' in render_json(report)
    assert "| AIV-0001 | AIV-0001-T01 | PASS |" in render_markdown(report)
