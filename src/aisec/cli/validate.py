"""Validation commands."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer

from aisec.registry.discovery import discover_vulnerability_packs
from aisec.registry.validator import validate_pack, validate_unique_ids

validate_app = typer.Typer(help="Validate project content.", no_args_is_help=True)


@validate_app.command("registry")
def validate_registry(
    registry: Annotated[Path, typer.Argument(help="Vulnerability registry root.")] = Path(
        "vulnerabilities"
    ),
) -> None:
    packs = discover_vulnerability_packs(registry)
    issues = []
    for pack in packs:
        issues.extend(validate_pack(pack))
    issues.extend(validate_unique_ids(packs))

    if issues:
        for issue in issues:
            typer.secho(f"{issue.severity}: {issue.path}: {issue.message}", fg=typer.colors.RED)
        raise typer.Exit(1)

    typer.echo(f"Validated {len(packs)} vulnerability pack(s)")
