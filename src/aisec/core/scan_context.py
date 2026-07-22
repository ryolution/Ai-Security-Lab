"""Scan context and configuration models."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class TargetConfig:
    id: str
    type: str
    authorization: dict[str, Any]
    connection: dict[str, Any]
    capabilities: tuple[str, ...]
    limits: dict[str, Any] = field(default_factory=dict)
    raw: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_mapping(cls, data: dict[str, Any]) -> TargetConfig:
        return cls(
            id=str(data["id"]),
            type=str(data["type"]),
            authorization=dict(data.get("authorization", {})),
            connection=dict(data.get("connection", {})),
            capabilities=tuple(str(item) for item in data.get("capabilities", [])),
            limits=dict(data.get("limits", {})),
            raw=data,
        )

    @property
    def authorization_confirmed(self) -> bool:
        return bool(self.authorization.get("confirmed", False))


@dataclass(frozen=True)
class PolicyConfig:
    name: str
    authorization_required: bool = True
    destructive_tests_enabled: bool = False
    network_default: str = "deny"
    forbidden_actions: tuple[str, ...] = ()
    require_confirmation: tuple[str, ...] = ()
    limits: dict[str, Any] = field(default_factory=dict)
    raw: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_mapping(cls, data: dict[str, Any]) -> PolicyConfig:
        return cls(
            name=str(data.get("name", "default")),
            authorization_required=bool(data.get("authorization_required", True)),
            destructive_tests_enabled=bool(data.get("destructive_tests_enabled", False)),
            network_default=str(data.get("network_default", "deny")),
            forbidden_actions=tuple(str(item) for item in data.get("forbidden_actions", [])),
            require_confirmation=tuple(str(item) for item in data.get("require_confirmation", [])),
            limits=dict(data.get("limits", {})),
            raw=data,
        )


@dataclass(frozen=True)
class ScanContext:
    target: TargetConfig
    policy: PolicyConfig
    registry_root: Path
    scan_id: str
    categories: tuple[str, ...] = ()
    vulnerability_ids: tuple[str, ...] = ()
