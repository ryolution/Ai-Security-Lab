"""Network policy helpers."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class NetworkPolicy:
    default: str = "deny"
    allowed_hosts: tuple[str, ...] = field(default_factory=tuple)

    def allows(self, host: str) -> bool:
        if self.default == "allow":
            return True
        return host in self.allowed_hosts
