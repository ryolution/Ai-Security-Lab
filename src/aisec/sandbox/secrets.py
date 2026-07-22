"""Secret handling helpers."""

from __future__ import annotations

import os

from aisec.core.exceptions import ConfigurationError


def read_secret_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise ConfigurationError(f"Required environment variable is not set: {name}")
    return value
