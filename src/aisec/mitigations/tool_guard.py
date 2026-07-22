"""Tool guard helpers."""

from __future__ import annotations


def require_tool_allowed(tool_name: str, allowed_tools: list[str]) -> bool:
    return tool_name in set(allowed_tools)
