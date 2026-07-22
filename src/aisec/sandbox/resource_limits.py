"""Resource limit models."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ResourceLimits:
    max_runtime_seconds: int = 60
    max_tokens: int = 4000
    max_tool_calls: int = 5
    max_parallel_tasks: int = 1
    memory: str = "512m"
    pids_limit: int = 128
