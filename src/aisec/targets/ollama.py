"""Ollama local chat target adapter."""

from __future__ import annotations

import httpx

from aisec.core.exceptions import ConfigurationError, TargetExecutionError
from aisec.targets.base import TargetAdapter, TargetRequest, TargetResponse


class OllamaTarget(TargetAdapter):
    async def send(self, request: TargetRequest) -> TargetResponse:
        base_url = str(self.config.connection.get("base_url", "")).rstrip("/")
        model = self.config.connection.get("model")
        timeout = float(self.config.connection.get("timeout_seconds", 45))

        if not base_url or not model:
            raise ConfigurationError("ollama target requires base_url and model")

        messages = [{"role": "user", "content": request.prompt}]
        if request.context:
            messages.insert(0, {"role": "system", "content": request.context})

        try:
            async with httpx.AsyncClient(timeout=timeout) as client:
                response = await client.post(
                    f"{base_url}/api/chat",
                    json={"model": model, "messages": messages, "stream": False},
                )
                response.raise_for_status()
        except httpx.HTTPError as exc:
            raise TargetExecutionError(f"Ollama request failed: {exc}") from exc

        data = response.json()
        message = data.get("message", {})
        text = message.get("content", "") if isinstance(message, dict) else ""
        return TargetResponse(text=str(text), raw=data)
