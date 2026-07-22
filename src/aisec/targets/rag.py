"""RAG target alias for generic HTTP RAG endpoints."""

from __future__ import annotations

from aisec.targets.http_api import HttpApiTarget


class RagTarget(HttpApiTarget):
    """Target adapter for retrieval-augmented generation HTTP endpoints."""
