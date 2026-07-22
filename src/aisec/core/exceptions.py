"""Framework exception hierarchy."""

from __future__ import annotations


class AisecError(Exception):
    """Base class for framework errors."""


class ConfigurationError(AisecError):
    """Raised when a target, policy, or scan configuration is invalid."""


class AuthorizationError(AisecError):
    """Raised when a scan attempts to run without explicit authorization."""


class RegistryError(AisecError):
    """Raised when vulnerability registry content is invalid."""


class TargetExecutionError(AisecError):
    """Raised when a target adapter cannot complete a request."""


class SafetyError(AisecError):
    """Raised when a requested operation violates the active safety policy."""
