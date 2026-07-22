"""Schema path helpers."""

from __future__ import annotations

from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_ROOT = REPOSITORY_ROOT / "schemas"


def schema_path(name: str) -> Path:
    return SCHEMA_ROOT / name


def vulnerability_schema_path() -> Path:
    return schema_path("vulnerability.schema.json")


def target_schema_path() -> Path:
    return schema_path("target.schema.json")


def policy_schema_path() -> Path:
    return schema_path("policy.schema.json")


def report_schema_path() -> Path:
    return schema_path("report.schema.json")
