"""JSON report renderer."""

from __future__ import annotations

import json

from aisec.core.result import ScanReport


def render_json(report: ScanReport) -> str:
    return json.dumps(report.to_dict(), indent=2, sort_keys=True) + "\n"
