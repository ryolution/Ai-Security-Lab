# Project Context

AI Security Lab is a living AI vulnerability testing and hardening laboratory.

The stable framework is built once and changes carefully:

```text
src/
  cli/
  core/
  targets/
  runners/
  sandbox/
  reporting/
  registry/
  schemas/
  utils/
```

The evolving layer is made of manually researched vulnerability modules:

```text
vulnerabilities/
  prompt-injection/
  rag/
  agents/
  mcp/
  models/
  supply-chain/
```

The project workflow is:

```text
Discover -> Reproduce -> Test -> Secure -> Retest
```

The framework should provide reusable infrastructure such as CLI commands, YAML validation, target adapters, registry loading, runners, reports, Docker sandboxing, logging, secret redaction, CI, and static templates.

Each newly disclosed vulnerability should still be researched and confirmed manually. AI can assist with implementation, but it should not automatically decide that a vulnerability is valid or that a mitigation is proven.

Core message:

```text
Test new AI vulnerabilities. Apply mitigations. Verify the fix.
```
