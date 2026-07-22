"""Probe contracts."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol

from aisec.targets.base import TargetRequest


@dataclass(frozen=True)
class ProbeCase:
    id: str
    name: str
    prompt: str
    context: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_request(self) -> TargetRequest:
        return TargetRequest(prompt=self.prompt, context=self.context, metadata=self.metadata)


class Probe(Protocol):
    def build_cases(self) -> list[ProbeCase]:
        """Return normalized probe cases."""


def cases_from_yaml(items: list[dict[str, Any]]) -> list[ProbeCase]:
    cases: list[ProbeCase] = []
    for item in items:
        input_data = item.get("input", {})
        setup = item.get("setup", {})
        prompt = input_data.get("prompt", "")
        context = setup.get("context") or setup.get("retrieved_document")
        cases.append(
            ProbeCase(
                id=str(item.get("id", "case")),
                name=str(item.get("name", item.get("id", "case"))),
                prompt=str(prompt),
                context=str(context) if context is not None else None,
                metadata=item,
            )
        )
    return cases
