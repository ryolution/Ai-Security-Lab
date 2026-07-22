"""AI Security Lab command-line application."""

from __future__ import annotations

import typer

from aisec import __version__
from aisec.cli.list_rules import list_app
from aisec.cli.report import report_command
from aisec.cli.retest import retest_command
from aisec.cli.scan import scan_command
from aisec.cli.secure import secure_command
from aisec.cli.validate import validate_app

app = typer.Typer(
    name="aisec",
    help="Test new AI vulnerabilities. Apply mitigations. Verify the fix.",
    no_args_is_help=True,
)
app.add_typer(list_app, name="list")
app.add_typer(validate_app, name="validate")
app.command("scan")(scan_command)
app.command("test")(scan_command)
app.command("secure")(secure_command)
app.command("retest")(retest_command)
app.command("report")(report_command)


def version_callback(value: bool) -> None:
    if value:
        typer.echo(__version__)
        raise typer.Exit()


@app.callback()
def root(
    version: bool = typer.Option(
        False,
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Show the installed version.",
    ),
) -> None:
    """AI vulnerability testing and hardening framework."""


def main() -> None:
    app()
