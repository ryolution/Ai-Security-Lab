"""List commands."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer

from aisec.registry.discovery import discover_vulnerability_packs
from aisec.registry.loader import load_manifest

list_app = typer.Typer(help="List registry and configuration entries.", no_args_is_help=True)


@list_app.command("vulnerabilities")
def list_vulnerabilities(
    registry: Annotated[
        Path,
        typer.Option("--registry", help="Vulnerability registry root."),
    ] = Path("vulnerabilities"),
) -> None:
    packs = discover_vulnerability_packs(registry)
    if not packs:
        typer.echo("No vulnerability packs found.")
        return

    for pack in packs:
        manifest = load_manifest(pack.manifest_path)
        typer.echo(
            f"{manifest.get('id', 'UNKNOWN')} "
            f"{manifest.get('name', pack.path.name)} "
            f"[{manifest.get('category', pack.category)}]"
        )


@list_app.command("targets")
def list_targets(
    configs: Annotated[Path, typer.Option("--configs", help="Target config directory.")] = Path(
        "configs/targets"
    ),
) -> None:
    targets = sorted(configs.glob("*.yml"))
    if not targets:
        typer.echo("No target configs found.")
        return
    for target in targets:
        typer.echo(str(target))
