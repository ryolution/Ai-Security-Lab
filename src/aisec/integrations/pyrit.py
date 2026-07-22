"""Optional PyRIT integration boundary."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PyritScenarioSpec:
    name: str
    target_id: str
    policy: str

    def metadata(self) -> dict[str, str]:
        return {"name": self.name, "target_id": self.target_id, "policy": self.policy}
