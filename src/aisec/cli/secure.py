"""Mitigation guidance command."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer

from aisec.registry.discovery import discover_vulnerability_packs
from aisec.registry.loader import load_manifest


def secure_command(
    vulnerability_id: Annotated[
        str,
        typer.Argument(help="Vulnerability ID, for example AIV-0001."),
    ],
    registry: Annotated[
        Path,
        typer.Option("--registry", help="Vulnerability registry root."),
    ] = Path("vulnerabilities"),
) -> None:
    """Show mitigation guidance for a vulnerability.

    This command does not claim to apply fixes automatically. It points reviewers to
    the pack-owned mitigation files that should be implemented and validated manually.
    """

    for pack in discover_vulnerability_packs(registry):
        manifest = load_manifest(pack.manifest_path)
        if manifest.get("id") == vulnerability_id:
            mitigation = pack.path / "secure" / "mitigation.md"
            policy = pack.path / "secure" / "policy.yml"
            typer.echo(f"Mitigation guidance: {mitigation}")
            if policy.exists():
                typer.echo(f"Suggested policy: {policy}")
            typer.echo("Manual implementation and retest are required.")
            return

    typer.secho(f"Vulnerability not found: {vulnerability_id}", fg=typer.colors.RED, err=True)
    raise typer.Exit(2)
