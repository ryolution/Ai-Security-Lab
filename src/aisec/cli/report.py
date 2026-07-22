"""Report conversion command."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Annotated, Any

import typer

from aisec.core.result import ScanReport, TestResult
from aisec.reporting.html_report import render_html
from aisec.reporting.json_report import render_json
from aisec.reporting.markdown_report import render_markdown
from aisec.reporting.sarif_report import render_sarif
from aisec.utils.serialization import write_text


def report_command(
    results: Annotated[Path, typer.Argument(help="JSON report produced by aisec scan.")],
    format: Annotated[
        str,
        typer.Option("--format", "-f", help="Output format: json, markdown, html, sarif."),
    ] = "markdown",
    output: Annotated[
        Path | None,
        typer.Option("--output", "-o", help="Write converted report."),
    ] = None,
) -> None:
    """Convert a JSON scan report into another static report format."""

    report = _load_report(results)
    rendered = _render(report, format)
    if output:
        write_text(output, rendered)
        typer.echo(f"Wrote {output}")
    else:
        typer.echo(rendered)


def _load_report(path: Path) -> ScanReport:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise typer.BadParameter("report JSON must contain an object")
    results = [
        TestResult(
            vulnerability_id=str(item["vulnerability_id"]),
            test_id=str(item["test_id"]),
            target_id=str(item["target_id"]),
            status=item["status"],
            score=item.get("score"),
            confidence=float(item.get("confidence", 0.0)),
            summary=str(item.get("summary", "")),
            evidence=dict(item.get("evidence", {})),
            error=item.get("error"),
        )
        for item in _list(payload.get("results", []))
    ]
    return ScanReport(
        framework=dict(payload.get("framework", {})),
        target=dict(payload.get("target", {})),
        policy=dict(payload.get("policy", {})),
        started_at=str(payload.get("started_at", "")),
        finished_at=str(payload.get("finished_at", "")),
        results=results,
        metadata=dict(payload.get("metadata", {})),
    )


def _render(report: ScanReport, format: str) -> str:
    normalized = format.lower()
    if normalized == "json":
        return render_json(report)
    if normalized in {"md", "markdown"}:
        return render_markdown(report)
    if normalized == "html":
        return render_html(report)
    if normalized == "sarif":
        return render_sarif(report)
    raise typer.BadParameter(f"Unsupported report format: {format}")


def _list(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, dict)]
