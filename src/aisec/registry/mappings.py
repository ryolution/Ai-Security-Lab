"""Framework taxonomy mapping helpers."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from aisec.utils.serialization import read_yaml


def load_framework_mapping(path: Path) -> dict[str, Any]:
    return read_yaml(path)


def category_mappings(path: Path) -> dict[str, list[str]]:
    data = load_framework_mapping(path)
    mappings = data.get("mappings", {})
    if not isinstance(mappings, dict):
        return {}
    normalized: dict[str, list[str]] = {}
    for key, value in mappings.items():
        if isinstance(value, list):
            normalized[str(key)] = [str(item) for item in value]
    return normalized
