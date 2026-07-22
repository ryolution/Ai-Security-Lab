"""Mitigation contracts."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Mitigation:
    id: str
    name: str
    description: str
    manual_validation_required: bool = True
