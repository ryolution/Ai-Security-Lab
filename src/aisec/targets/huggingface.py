"""Local Hugging Face target placeholder."""

from __future__ import annotations

from aisec.core.exceptions import ConfigurationError
from aisec.targets.base import TargetAdapter, TargetRequest, TargetResponse


class HuggingFaceTarget(TargetAdapter):
    async def send(self, request: TargetRequest) -> TargetResponse:
        raise ConfigurationError(
            "huggingface target support is scaffolded but not implemented. "
            "Use a lab-specific adapter or add a vetted local model runner."
        )
