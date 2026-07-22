"""Permission policy helpers."""

from __future__ import annotations


def is_action_allowed(action: str, forbidden_actions: list[str]) -> bool:
    return action not in set(forbidden_actions)
