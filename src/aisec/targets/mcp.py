"""MCP target placeholder."""

from __future__ import annotations

from aisec.core.exceptions import ConfigurationError
from aisec.targets.base import TargetAdapter, TargetRequest, TargetResponse


class McpTarget(TargetAdapter):
    async def send(self, request: TargetRequest) -> TargetResponse:
        raise ConfigurationError(
            "mcp target support is scaffolded but not implemented. "
            "Add a vetted MCP client/server adapter before running MCP packs."
        )
