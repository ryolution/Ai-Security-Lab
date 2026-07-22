"""SARIF report renderer."""

from __future__ import annotations

import json

from aisec import __version__
from aisec.core.result import ScanReport


def render_sarif(report: ScanReport) -> str:
    results = []
    for result in report.results:
        if result.status != "FAIL":
            continue
        results.append(
            {
                "ruleId": result.vulnerability_id,
                "level": "warning",
                "message": {"text": result.summary},
                "locations": [
                    {
                        "physicalLocation": {
                            "artifactLocation": {"uri": "vulnerabilities"},
                            "region": {"startLine": 1},
                        }
                    }
                ],
            }
        )

    payload = {
        "version": "2.1.0",
        "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
        "runs": [
            {
                "tool": {
                    "driver": {
                        "name": "AI Security Lab",
                        "informationUri": "https://github.com/ryolution/Ai-Security-Lab",
                        "version": __version__,
                    }
                },
                "results": results,
            }
        ],
    }
    return json.dumps(payload, indent=2, sort_keys=True) + "\n"
