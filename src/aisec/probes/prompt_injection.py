"""Reusable prompt-injection probe helpers."""

from __future__ import annotations

from aisec.probes.base import ProbeCase


def direct_prompt_case(case_id: str, prompt: str, *, name: str | None = None) -> ProbeCase:
    return ProbeCase(id=case_id, name=name or case_id, prompt=prompt)
