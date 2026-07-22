from __future__ import annotations

from typer.testing import CliRunner

from aisec.cli.app import app


def test_validate_registry_succeeds_with_empty_registry() -> None:
    runner = CliRunner()

    result = runner.invoke(app, ["validate", "registry", "vulnerabilities"])

    assert result.exit_code == 0
    assert "Validated 0 vulnerability pack(s)" in result.stdout


def test_list_targets_shows_example_configs() -> None:
    runner = CliRunner()

    result = runner.invoke(app, ["list", "targets"])

    assert result.exit_code == 0
    assert "openai-compatible.example.yml" in result.stdout
