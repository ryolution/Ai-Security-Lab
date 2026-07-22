# Contributing

AI Security Lab accepts contributions that improve safe, reproducible AI security validation.

## Contribution Types

- Framework code and target adapters
- Vulnerability manifests and safe test cases
- Detectors and evaluators
- Mitigation guidance
- Intentionally vulnerable labs with secured variants
- Documentation, examples, and policy mappings

## Vulnerability Contributions

A vulnerability contribution should include:

- `manifest.yml`
- `README.md`
- `cases.yml`
- `secure/mitigation.md`
- `regression/vulnerable.expected.yml`
- `regression/secured.expected.yml`
- `references.md`

Use synthetic canaries, mock secrets, and local fixtures. Do not include real credentials, private data, destructive payloads, or uncontrolled exploit logic.

## Development

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python scripts/validate_registry.py vulnerabilities
```

## Safety Rules

- Test only authorized targets.
- Keep probes separate from detectors.
- Make dangerous behavior explicit and opt-in.
- Redact secrets before logging or reporting.
- Prefer declarative YAML packs where possible.
