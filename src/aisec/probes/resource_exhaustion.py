"""Reusable resource-exhaustion probe metadata."""

from __future__ import annotations

from aisec.probes.base import ProbeCase


def bounded_generation_case(case_id: str, prompt: str, max_tokens: int) -> ProbeCase:
    return ProbeCase(
        id=case_id,
        name=f"Bounded generation check {case_id}",
        prompt=prompt,
        metadata={"max_tokens": max_tokens, "destructive": False},
    )
