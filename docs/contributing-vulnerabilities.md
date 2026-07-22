# Contributing Vulnerabilities

New vulnerability packs should be safe, reproducible, documented, and regression-ready.

Checklist:

- Stable `AIV-XXXX` ID
- Complete manifest
- Safe test cases
- Detector configuration
- Expected vulnerable behavior
- Expected secure behavior
- Mitigation guidance
- Regression expectations
- References
- Safety considerations

Run `python scripts/validate_registry.py vulnerabilities` before submitting.
