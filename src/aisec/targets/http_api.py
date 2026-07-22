"""Generic HTTP target adapter."""

from __future__ import annotations

import os
from string import Template
from typing import Any

import httpx

from aisec.core.exceptions import ConfigurationError, TargetExecutionError
from aisec.targets.base import TargetAdapter, TargetRequest, TargetResponse


class UnsupportedTarget(TargetAdapter):
    async def send(self, request: TargetRequest) -> TargetResponse:
        raise ConfigurationError(f"Unsupported target type: {self.config.type}")


class HttpApiTarget(TargetAdapter):
    async def send(self, request: TargetRequest) -> TargetResponse:
        endpoint = self.config.connection.get("endpoint")
        method = str(self.config.connection.get("method", "POST")).upper()
        timeout = float(self.config.connection.get("timeout_seconds", 30))
        if not endpoint:
            raise ConfigurationError("http target requires connection.endpoint")

        headers = {"Content-Type": "application/json"}
        api_key_env = self.config.connection.get("api_key_env")
        if api_key_env:
            api_key = os.getenv(str(api_key_env))
            if api_key:
                headers["Authorization"] = f"Bearer {api_key}"

        payload = _render_template(self.config.raw.get("request_template", {}), request)
        try:
            async with httpx.AsyncClient(timeout=timeout) as client:
                response = await client.request(
                    method,
                    str(endpoint),
                    headers=headers,
                    json=payload,
                )
                response.raise_for_status()
        except httpx.HTTPError as exc:
            raise TargetExecutionError(f"HTTP target request failed: {exc}") from exc

        data = response.json()
        mapping = self.config.raw.get("response_mapping", {})
        text_path = mapping.get("text_path", "text") if isinstance(mapping, dict) else "text"
        text = _get_path(data, str(text_path))
        return TargetResponse(text=str(text or ""), raw=data)


def _render_template(template: object, request: TargetRequest) -> Any:
    if isinstance(template, dict):
        return {key: _render_template(value, request) for key, value in template.items()}
    if isinstance(template, list):
        return [_render_template(value, request) for value in template]
    if isinstance(template, str):
        normalized = template.replace("{{ prompt }}", "$prompt").replace(
            "{{ context }}",
            "$context",
        )
        return (
            Template(normalized).safe_substitute(
                prompt=request.prompt,
                context=request.context or "",
            )
        )
    return template


def _get_path(data: Any, path: str) -> Any:
    current = data
    for part in path.split("."):
        if isinstance(current, dict):
            current = current.get(part)
        else:
            return None
    return current
