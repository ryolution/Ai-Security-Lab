"""Discover vulnerability packs on disk."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class VulnerabilityPack:
    path: Path
    category: str

    @property
    def manifest_path(self) -> Path:
        return self.path / "manifest.yml"


def discover_vulnerability_packs(root: Path) -> list[VulnerabilityPack]:
    if not root.exists():
        return []

    packs: list[VulnerabilityPack] = []
    for manifest in sorted(root.glob("*/*/manifest.yml")):
        category = manifest.parent.parent.name
        packs.append(VulnerabilityPack(path=manifest.parent, category=category))
    return packs
