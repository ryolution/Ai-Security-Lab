"""HTML report renderer."""

from __future__ import annotations

from html import escape

from aisec.core.result import ScanReport


def render_html(report: ScanReport) -> str:
    rows = "\n".join(
        "<tr>"
        f"<td>{escape(result.vulnerability_id)}</td>"
        f"<td>{escape(result.test_id)}</td>"
        f"<td>{escape(result.status)}</td>"
        f"<td>{result.confidence:.2f}</td>"
        f"<td>{escape(result.summary)}</td>"
        "</tr>"
        for result in report.results
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>AI Security Lab Report</title>
  <style>
    body {{ color: #172033; font-family: system-ui, sans-serif; margin: 2rem; }}
    table {{ border-collapse: collapse; width: 100%; }}
    th, td {{ border: 1px solid #d8dee8; padding: 0.5rem; text-align: left; }}
    th {{ background: #eef2f7; }}
  </style>
</head>
<body>
  <h1>AI Security Lab Report</h1>
  <p>Target: <code>{escape(str(report.target.get("id", "unknown")))}</code></p>
  <p>Policy: <code>{escape(str(report.policy.get("name", "unknown")))}</code></p>
  <table>
    <thead>
      <tr><th>Vulnerability</th><th>Test</th><th>Status</th><th>Confidence</th><th>Summary</th></tr>
    </thead>
    <tbody>
      {rows}
    </tbody>
  </table>
</body>
</html>
"""
