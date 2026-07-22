"""Async runner helpers."""

from __future__ import annotations

import asyncio
from collections.abc import Coroutine
from typing import Any


def run_sync(awaitable: Coroutine[Any, Any, object]) -> object:
    return asyncio.run(awaitable)
