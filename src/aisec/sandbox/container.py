"""Sandbox container defaults."""

from __future__ import annotations

from pathlib import Path

from aisec.runners.docker import DockerRunSpec


def default_sandbox_spec(command: list[str], workspace: Path) -> DockerRunSpec:
    return DockerRunSpec(
        image="ai-security-lab/sandbox:local",
        workdir="/workspace",
        readonly_mount=workspace,
        command=command,
    )
