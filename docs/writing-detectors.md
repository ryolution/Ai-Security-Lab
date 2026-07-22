# Writing Detectors

A detector analyzes target behavior and emits evidence.

Detector rules:

- Return structured output.
- Include the matched indicator or reason.
- Preserve only redacted evidence.
- Distinguish missing evidence from safe behavior.
- Keep detection logic reusable across vulnerability packs.

Common detector types include exact match, regex, canary, semantic policy checks, and tool-call validation.
