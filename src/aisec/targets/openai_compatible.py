"""OpenAI-compatible chat-completions target adapter."""

from __future__ import annotations

import os

import httpx

from aisec.core.exceptions import ConfigurationError, TargetExecutionError
from aisec.targets.base import TargetAdapter, TargetRequest, TargetResponse


class OpenAICompatibleTarget(TargetAdapter):
    async def send(self, request: TargetRequest) -> TargetResponse:
        base_url = str(self.config.connection.get("base_url", "")).rstrip("/")
        model = self.config.connection.get("model")
        api_key_env = self.config.connection.get("api_key_env")
        timeout = float(self.config.connection.get("timeout_seconds", 30))

        if not base_url or not model:
            raise ConfigurationError("openai-compatible target requires base_url and model")

        headers = {"Content-Type": "application/json"}
        if api_key_env:
            api_key = os.getenv(str(api_key_env))
            if api_key:
                headers["Authorization"] = f"Bearer {api_key}"

        messages = [{"role": "user", "content": request.prompt}]
        if request.context:
            messages.insert(0, {"role": "system", "content": request.context})

        try:
            async with httpx.AsyncClient(timeout=timeout) as client:
                response = await client.post(
                    f"{base_url}/chat/completions",
                    headers=headers,
                    json={"model": model, "messages": messages},
                )
                response.raise_for_status()
        except httpx.HTTPError as exc:
            raise TargetExecutionError(f"OpenAI-compatible request failed: {exc}") from exc

        data = response.json()
        text = _extract_text(data)
        usage = data.get("usage", {})
        return TargetResponse(
            text=text,
            raw=data,
            token_usage={key: int(value) for key, value in usage.items() if isinstance(value, int)},
        )


def _extract_text(data: dict[str, object]) -> str:
    choices = data.get("choices")
    if not isinstance(choices, list) or not choices:
        return ""
    first = choices[0]
    if not isinstance(first, dict):
        return ""
    message = first.get("message")
    if not isinstance(message, dict):
        return ""
    content = message.get("content")
    return content if isinstance(content, str) else ""
