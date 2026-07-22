"""Scan and vulnerability test commands."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer

from aisec.core.exceptions import AuthorizationError, ConfigurationError, RegistryError
from aisec.core.orchestrator import SecurityOrchestrator, build_scan_context
from aisec.core.result import ScanReport
from aisec.core.scan_context import PolicyConfig, TargetConfig
from aisec.reporting.console import print_console
from aisec.reporting.html_report import render_html
from aisec.reporting.json_report import render_json
from aisec.reporting.markdown_report import render_markdown
from aisec.reporting.sarif_report import render_sarif
from aisec.utils.serialization import read_yaml, write_text


def scan_command(
    vulnerability_id: Annotated[
        str | None,
        typer.Argument(help="Optional vulnerability ID, for example AIV-0001."),
    ] = None,
    target: Annotated[Path, typer.Option("--target", "-t", help="Target YAML file.")] = Path(
        "configs/targets/openai-compatible.example.yml"
    ),
    policy: Annotated[Path, typer.Option("--policy", "-p", help="Policy YAML file.")] = Path(
        "policies/default.yml"
    ),
    registry: Annotated[
        Path,
        typer.Option("--registry", help="Vulnerability registry root."),
    ] = Path("vulnerabilities"),
    category: Annotated[
        list[str] | None,
        typer.Option("--category", "-c", help="Restrict scan to a vulnerability category."),
    ] = None,
    output: Annotated[
        Path | None,
        typer.Option("--output", "-o", help="Write report to file."),
    ] = None,
    format: Annotated[
        str,
        typer.Option("--format", "-f", help="Report format: console, json, markdown, html, sarif."),
    ] = "console",
) -> None:
    """Run a safe scan or a single vulnerability test against an authorized target."""

    try:
        report = _run_scan(
            target_path=target,
            policy_path=policy,
            registry_root=registry,
            categories=tuple(category or ()),
            vulnerability_ids=(vulnerability_id,) if vulnerability_id else (),
        )
    except AuthorizationError as exc:
        typer.secho(str(exc), fg=typer.colors.RED, err=True)
        raise typer.Exit(4) from exc
    except (ConfigurationError, RegistryError) as exc:
        typer.secho(str(exc), fg=typer.colors.RED, err=True)
        raise typer.Exit(2) from exc

    rendered = _render(report, format)
    if output:
        write_text(output, rendered)
        typer.echo(f"Wrote {output}")
    elif format == "console":
        print_console(report)
    else:
        typer.echo(rendered)

    if any(result.status == "FAIL" for result in report.results):
        raise typer.Exit(1)


def _run_scan(
    *,
    target_path: Path,
    policy_path: Path,
    registry_root: Path,
    categories: tuple[str, ...] = (),
    vulnerability_ids: tuple[str, ...] = (),
) -> ScanReport:
    target = TargetConfig.from_mapping(read_yaml(target_path))
    policy = PolicyConfig.from_mapping(read_yaml(policy_path))
    context = build_scan_context(
        target,
        policy,
        registry_root=registry_root,
        categories=categories,
        vulnerability_ids=vulnerability_ids,
    )
    return SecurityOrchestrator(context).run()


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
    if normalized == "console":
        return ""
    raise ConfigurationError(f"Unsupported report format: {format}")
