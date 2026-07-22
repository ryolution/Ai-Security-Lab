from __future__ import annotations

from aisec.utils.redaction import redact_text


def test_redacts_common_secret_shapes() -> None:
    value = "api_key=sk-exampleSecretToken123456 and owner admin@example.com"

    redacted = redact_text(value)

    assert "sk-exampleSecretToken123456" not in redacted
    assert "admin@example.com" not in redacted
    assert "[REDACTED]" in redacted
