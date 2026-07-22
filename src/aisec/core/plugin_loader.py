"""Helpers for loading explicitly allowed local plugin symbols."""

from __future__ import annotations

import importlib.util
from pathlib import Path
from types import ModuleType
from typing import Any

from aisec.core.exceptions import SafetyError


def load_module_from_path(path: Path, *, allowed_root: Path) -> ModuleType:
    resolved_path = path.resolve()
    resolved_root = allowed_root.resolve()

    if not resolved_path.is_relative_to(resolved_root):
        raise SafetyError(f"Plugin path escapes allowed root: {path}")

    if resolved_path.suffix != ".py":
        raise SafetyError(f"Plugin path must be a Python file: {path}")

    module_name = f"aisec_user_plugin_{abs(hash(resolved_path))}"
    spec = importlib.util.spec_from_file_location(module_name, resolved_path)
    if spec is None or spec.loader is None:
        raise SafetyError(f"Cannot load plugin module: {path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_symbol(path: Path, symbol: str, *, allowed_root: Path) -> Any:
    module = load_module_from_path(path, allowed_root=allowed_root)
    if not hasattr(module, symbol):
        raise SafetyError(f"Plugin symbol not found: {symbol}")
    return getattr(module, symbol)
