"""Check that framework mapping policy files are present."""

from __future__ import annotations

from pathlib import Path

EXPECTED = {
    "owasp-llm.yml",
    "owasp-agentic.yml",
    "mitre-atlas.yml",
}


def main() -> int:
    mapping_dir = Path("policies/frameworks")
    missing = sorted(name for name in EXPECTED if not (mapping_dir / name).exists())

    if missing:
        for name in missing:
            print(f"missing: {mapping_dir / name}")
        return 1

    print(f"Mapping files present: {', '.join(sorted(EXPECTED))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
