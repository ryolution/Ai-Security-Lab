"""Output filtering helpers."""

from __future__ import annotations

from aisec.utils.redaction import redact_text


def redact_output(value: str) -> str:
    return redact_text(value)
