"""Validate vulnerability pack structure and manifest metadata."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from aisec.registry.discovery import discover_vulnerability_packs  # noqa: E402
from aisec.registry.validator import validate_pack, validate_unique_ids  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default="vulnerabilities", help="Registry root path")
    args = parser.parse_args(argv)

    registry_root = Path(args.root)
    packs = discover_vulnerability_packs(registry_root)
    issues = []

    for pack in packs:
        issues.extend(validate_pack(pack))

    issues.extend(validate_unique_ids(packs))

    if not packs:
        print(f"No vulnerability packs found under {registry_root}")

    if issues:
        for issue in issues:
            print(f"{issue.severity}: {issue.path}: {issue.message}")
        return 1

    print(f"Validated {len(packs)} vulnerability pack(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
