# Security Policy

AI Security Lab is security tooling and must be treated as a high-risk application. It may process adversarial prompts, model output, retrieved documents, tool definitions, payload files, and reports.

## Reporting Security Issues

Please report suspected vulnerabilities privately through the repository security advisory process when available. If advisories are unavailable, open a minimal issue that does not disclose exploit details and ask for a private contact path.

## Supported Versions

The project is pre-release. Security fixes are applied to the default branch until versioned releases begin.

## Framework Safety Expectations

- No real secrets in examples, tests, fixtures, or reports.
- No destructive tests by default.
- No unrestricted shell or network access by default.
- Explicit authorization is required before scanning a target.
- Outputs should redact credentials and high-risk tokens.
- External integrations must be adapters, not implicit dependencies.
