"""Create starter report template assets for downstream customization."""

from __future__ import annotations

from pathlib import Path

HTML_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>AI Security Lab Report</title>
  <style>
    body { font-family: system-ui, sans-serif; margin: 2rem; color: #172033; }
    table { border-collapse: collapse; width: 100%; }
    th, td { border: 1px solid #d8dee8; padding: 0.5rem; text-align: left; }
    th { background: #eef2f7; }
  </style>
</head>
<body>
  {{ body }}
</body>
</html>
"""


def main() -> int:
    output_dir = Path("docs/report-templates")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "base.html").write_text(HTML_TEMPLATE, encoding="utf-8")
    print(f"Wrote {output_dir / 'base.html'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
