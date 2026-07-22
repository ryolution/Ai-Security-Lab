"""Console report renderer."""

from __future__ import annotations

from rich.console import Console
from rich.table import Table

from aisec.core.result import ScanReport


def print_console(report: ScanReport, console: Console | None = None) -> None:
    output = console or Console()
    table = Table(title="AI Security Lab Results")
    table.add_column("Vulnerability")
    table.add_column("Test")
    table.add_column("Status")
    table.add_column("Confidence", justify="right")
    table.add_column("Summary")

    for result in report.results:
        table.add_row(
            result.vulnerability_id,
            result.test_id,
            result.status,
            f"{result.confidence:.2f}",
            result.summary,
        )

    output.print(table)
