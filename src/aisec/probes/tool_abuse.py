"""Reusable tool-abuse probe helpers."""

from __future__ import annotations

from aisec.probes.base import ProbeCase


def forbidden_tool_case(case_id: str, prompt: str, forbidden_tools: list[str]) -> ProbeCase:
    return ProbeCase(
        id=case_id,
        name=f"Forbidden tool check {case_id}",
        prompt=prompt,
        metadata={"forbidden_tools": forbidden_tools},
    )
