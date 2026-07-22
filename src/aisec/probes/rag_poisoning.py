"""Reusable RAG poisoning probe helpers."""

from __future__ import annotations

from aisec.probes.base import ProbeCase


def retrieved_document_case(case_id: str, prompt: str, document: str) -> ProbeCase:
    return ProbeCase(
        id=case_id,
        name=f"Retrieved document check {case_id}",
        prompt=prompt,
        context=document,
        metadata={"surface": "rag"},
    )
