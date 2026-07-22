"""Regression retest command."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer

from aisec.cli.scan import scan_command


def retest_command(
    vulnerability_id: Annotated[str, typer.Argument(help="Vulnerability ID to retest.")],
    target: Annotated[Path, typer.Option("--target", "-t", help="Target YAML file.")],
    policy: Annotated[Path, typer.Option("--policy", "-p", help="Policy YAML file.")] = Path(
        "policies/ci.yml"
    ),
    registry: Annotated[
        Path,
        typer.Option("--registry", help="Vulnerability registry root."),
    ] = Path("vulnerabilities"),
    output: Annotated[
        Path | None,
        typer.Option("--output", "-o", help="Write report to file."),
    ] = None,
    format: Annotated[str, typer.Option("--format", "-f")] = "console",
) -> None:
    """Run a selected vulnerability as a regression check."""

    scan_command(
        vulnerability_id=vulnerability_id,
        target=target,
        policy=policy,
        registry=registry,
        category=None,
        output=output,
        format=format,
    )
