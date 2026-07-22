"""Intentionally vulnerable lab template."""

from __future__ import annotations


def handle_request(prompt: str, context: str) -> str:
    return f"{context}\n\nUser asked: {prompt}"
