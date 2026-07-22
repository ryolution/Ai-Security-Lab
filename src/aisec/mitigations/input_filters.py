"""Input filtering helpers."""

from __future__ import annotations


def reject_if_contains(value: str, blocked_terms: list[str]) -> bool:
    normalized = value.casefold()
    return any(term.casefold() in normalized for term in blocked_terms)
