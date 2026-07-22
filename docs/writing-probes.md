# Writing Probes

A probe creates or executes a test case. It should not decide whether the attack succeeded.

Probe rules:

- Keep payloads synthetic and safe.
- Declare required target capabilities.
- Use deterministic fixtures where possible.
- Include timeouts and resource expectations.
- Avoid hidden side effects.

Simple probes should be declarative through `cases.yml`. Python probes are for custom setup or execution only.
