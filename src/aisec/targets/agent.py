"""Tool-using agent target adapter."""

from __future__ import annotations

from aisec.targets.http_api import HttpApiTarget


class AgentTarget(HttpApiTarget):
    """HTTP agent adapter that preserves raw tool traces when provided."""
