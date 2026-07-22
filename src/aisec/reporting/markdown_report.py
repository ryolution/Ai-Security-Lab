"""Markdown report renderer."""

from __future__ import annotations

from aisec.core.result import ScanReport


def render_markdown(report: ScanReport) -> str:
    lines = [
        "# AI Security Lab Report",
        "",
        f"- Target: `{report.target.get('id', 'unknown')}`",
        f"- Policy: `{report.policy.get('name', 'unknown')}`",
        f"- Started: `{report.started_at}`",
        f"- Finished: `{report.finished_at}`",
        "",
        "| Vulnerability | Test | Status | Confidence | Summary |",
        "| --- | --- | --- | ---: | --- |",
    ]
    for result in report.results:
        lines.append(
            "| "
            f"{result.vulnerability_id} | "
            f"{result.test_id} | "
            f"{result.status} | "
            f"{result.confidence:.2f} | "
            f"{_escape(result.summary)} |"
        )
    lines.append("")
    return "\n".join(lines)


def _escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")
