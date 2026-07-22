"""Batch runner helpers."""

from __future__ import annotations

import asyncio
from collections.abc import Awaitable


async def run_limited(tasks: list[Awaitable[object]], limit: int) -> list[object]:
    semaphore = asyncio.Semaphore(limit)

    async def guarded(task: Awaitable[object]) -> object:
        async with semaphore:
            return await task

    return await asyncio.gather(*(guarded(task) for task in tasks))
