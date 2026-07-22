"""Target adapter contracts."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

from aisec.core.scan_context import TargetConfig


@dataclass(frozen=True)
class TargetRequest:
    prompt: str
    context: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class TargetResponse:
    text: str
    raw: dict[str, Any] = field(default_factory=dict)
    tool_calls: list[dict[str, Any]] = field(default_factory=list)
    token_usage: dict[str, int] = field(default_factory=dict)


class TargetAdapter(ABC):
    def __init__(self, config: TargetConfig) -> None:
        self.config = config

    @abstractmethod
    async def send(self, request: TargetRequest) -> TargetResponse:
        """Send a normalized request to the target."""


def build_target(config: TargetConfig) -> TargetAdapter:
    if config.type == "openai-compatible":
        from aisec.targets.openai_compatible import OpenAICompatibleTarget

        return OpenAICompatibleTarget(config)
    if config.type == "ollama":
        from aisec.targets.ollama import OllamaTarget

        return OllamaTarget(config)
    if config.type in {"http-api", "rag-http"}:
        from aisec.targets.http_api import HttpApiTarget

        return HttpApiTarget(config)
    if config.type == "agent-http":
        from aisec.targets.agent import AgentTarget

        return AgentTarget(config)
    if config.type == "huggingface":
        from aisec.targets.huggingface import HuggingFaceTarget

        return HuggingFaceTarget(config)
    if config.type == "mcp":
        from aisec.targets.mcp import McpTarget

        return McpTarget(config)

    from aisec.targets.http_api import UnsupportedTarget

    return UnsupportedTarget(config)
