"""Load vulnerability registry files."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from aisec.core.exceptions import RegistryError
from aisec.registry.discovery import VulnerabilityPack
from aisec.utils.serialization import read_yaml


def load_manifest(path: Path) -> dict[str, Any]:
    try:
        return read_yaml(path)
    except Exception as exc:
        raise RegistryError(f"Could not load manifest {path}: {exc}") from exc


def load_cases(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise RegistryError(f"cases.yml must contain a mapping: {path}")
    cases = data.get("cases", [])
    if not isinstance(cases, list):
        raise RegistryError(f"cases.yml field 'cases' must be a list: {path}")
    return [case for case in cases if isinstance(case, dict)]


def load_pack_manifest(pack: VulnerabilityPack) -> dict[str, Any]:
    return load_manifest(pack.manifest_path)
