from __future__ import annotations

from pathlib import Path

from aisec.registry.discovery import discover_vulnerability_packs
from aisec.registry.validator import validate_pack, validate_unique_ids


def test_valid_pack_has_no_registry_issues(tmp_path: Path) -> None:
    pack = tmp_path / "vulnerabilities" / "rag" / "AIV-0001-indirect-prompt-injection"
    (pack / "secure").mkdir(parents=True)
    (pack / "regression").mkdir()
    (pack / "manifest.yml").write_text(
        """
id: AIV-0001
name: Indirect Prompt Injection
slug: indirect-prompt-injection
version: 1.0.0
status: confirmed
category: rag
severity:
  level: high
requirements:
  target_capabilities:
    - chat
probe:
  type: declarative
  cases: cases.yml
detectors:
  - type: canary
mitigations:
  - context_separation
safe_by_default: true
created: 2026-07-22
updated: 2026-07-22
""".strip()
        + "\n",
        encoding="utf-8",
    )
    (pack / "README.md").write_text("# Test\n", encoding="utf-8")
    (pack / "cases.yml").write_text(
        """
cases:
  - id: AIV-0001-T01
    name: Test case
    input:
      prompt: Hello
    detectors:
      - canary
""".strip()
        + "\n",
        encoding="utf-8",
    )
    (pack / "secure" / "mitigation.md").write_text("# Mitigation\n", encoding="utf-8")
    (pack / "regression" / "vulnerable.expected.yml").write_text(
        "expected_status: FAIL\n",
        encoding="utf-8",
    )
    (pack / "regression" / "secured.expected.yml").write_text(
        "expected_status: PASS\n",
        encoding="utf-8",
    )
    (pack / "references.md").write_text("# References\n", encoding="utf-8")

    packs = discover_vulnerability_packs(tmp_path / "vulnerabilities")

    assert len(packs) == 1
    assert validate_pack(packs[0]) == []
    assert validate_unique_ids(packs) == []
