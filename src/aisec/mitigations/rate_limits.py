"""Rate-limit helpers."""

from __future__ import annotations


def within_limit(count: int, limit: int) -> bool:
    return count <= limit
