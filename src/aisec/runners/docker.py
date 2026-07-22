"""Docker runner command builder.

The foundation only builds command metadata. Actual container execution is left to
callers so dangerous flags and host mounts can be reviewed explicitly.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DockerRunSpec:
    image: str
    workdir: str
    readonly_mount: Path
    command: list[str]
    network: str = "none"
    memory: str = "512m"
    pids_limit: int = 128

    def argv(self) -> list[str]:
        return [
            "docker",
            "run",
            "--rm",
            "--network",
            self.network,
            "--memory",
            self.memory,
            "--pids-limit",
            str(self.pids_limit),
            "--read-only",
            "-v",
            f"{self.readonly_mount.resolve()}:{self.workdir}:ro",
            "-w",
            self.workdir,
            self.image,
            *self.command,
        ]
