"""Optional Promptfoo integration boundary."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class PromptfooRunSpec:
    config: Path
    output: Path

    def argv(self) -> list[str]:
        return ["promptfoo", "eval", "-c", str(self.config), "-o", str(self.output)]
