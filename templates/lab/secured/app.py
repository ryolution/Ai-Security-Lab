"""Secured lab template."""

from __future__ import annotations


def handle_request(prompt: str, context: str) -> str:
    safe_context = context.replace("AIV_SYNTHETIC_CANARY", "[redacted synthetic canary]")
    return f"Summary prepared for: {prompt}\nContext: {safe_context}"
