"""Filesystem safety helpers."""

from __future__ import annotations

from pathlib import Path

from aisec.core.exceptions import SafetyError


def resolve_under(path: Path, root: Path) -> Path:
    resolved_path = path.resolve()
    resolved_root = root.resolve()
    if not resolved_path.is_relative_to(resolved_root):
        raise SafetyError(f"Path escapes allowed root: {path}")
    return resolved_path
