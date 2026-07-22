"""Generate a Markdown catalog from vulnerability manifests."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from aisec.registry.discovery import discover_vulnerability_packs  # noqa: E402
from aisec.registry.loader import load_manifest  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default="vulnerabilities")
    parser.add_argument("--output", default="docs/vulnerability-catalog.md")
    args = parser.parse_args(argv)

    packs = discover_vulnerability_packs(Path(args.root))
    lines = ["# Vulnerability Catalog", ""]

    for pack in packs:
        manifest = load_manifest(pack.manifest_path)
        lines.append(f"## {manifest.get('id', 'UNKNOWN')} - {manifest.get('name', pack.path.name)}")
        lines.append("")
        lines.append(f"- Category: `{manifest.get('category', 'unknown')}`")
        lines.append(f"- Version: `{manifest.get('version', '0.0.0')}`")
        lines.append(f"- Status: `{manifest.get('status', 'draft')}`")
        lines.append("")

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
