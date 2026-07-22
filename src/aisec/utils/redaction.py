"""Secret redaction utilities."""

from __future__ import annotations

import re
from collections.abc import Mapping, Sequence
from typing import Any

DEFAULT_SECRET_PATTERNS = (
    re.compile(r"(?i)(api[_-]?key|token|secret|password)\s*[:=]\s*['\"]?([A-Za-z0-9_.:/+=-]{8,})"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{16,}\b"),
    re.compile(r"\bghp_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
)


class Redactor:
    def __init__(self, mask: str = "[REDACTED]", extra_patterns: Sequence[str] = ()) -> None:
        self.mask = mask
        self.patterns = [*DEFAULT_SECRET_PATTERNS, *(re.compile(item) for item in extra_patterns)]

    def text(self, value: str) -> str:
        redacted = value
        for pattern in self.patterns:
            redacted = pattern.sub(self.mask, redacted)
        return redacted

    def data(self, value: Any) -> Any:
        if isinstance(value, str):
            return self.text(value)
        if isinstance(value, Mapping):
            return {key: self.data(item) for key, item in value.items()}
        if isinstance(value, list):
            return [self.data(item) for item in value]
        if isinstance(value, tuple):
            return tuple(self.data(item) for item in value)
        return value


def redact_text(value: str, mask: str = "[REDACTED]") -> str:
    return Redactor(mask=mask).text(value)
