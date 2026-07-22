"""Reusable data-leakage probe helpers."""

from __future__ import annotations

from aisec.probes.base import ProbeCase


def canary_leak_case(case_id: str, prompt: str, canary: str) -> ProbeCase:
    return ProbeCase(
        id=case_id,
        name=f"Canary leakage check {case_id}",
        prompt=prompt,
        metadata={"canary": canary},
    )
