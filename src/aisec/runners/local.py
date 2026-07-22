"""Local scan runner."""

from __future__ import annotations

from aisec.core.orchestrator import SecurityOrchestrator
from aisec.core.result import ScanReport


class LocalRunner:
    def __init__(self, orchestrator: SecurityOrchestrator) -> None:
        self.orchestrator = orchestrator

    def run(self) -> ScanReport:
        return self.orchestrator.run()
