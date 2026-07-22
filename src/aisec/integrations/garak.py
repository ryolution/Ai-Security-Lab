"""Optional garak integration boundary."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GarakRunSpec:
    probe: str
    model_type: str
    model_name: str
    output_path: str

    def argv(self) -> list[str]:
        return [
            "garak",
            "--probes",
            self.probe,
            "--model_type",
            self.model_type,
            "--model_name",
            self.model_name,
            "--report_prefix",
            self.output_path,
        ]
