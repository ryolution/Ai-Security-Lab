# AI Security Lab

AI Security Lab is an open-source framework for continuously testing, hardening, and retesting AI systems against known vulnerability classes.

The project is built around a repeatable lifecycle:

```text
TEST -> DETECT -> SECURE -> RETEST -> REGRESS
```

It is not a proof that an AI system is secure. It is a practical validation framework that helps teams measure risk, collect evidence, apply defensive controls, and keep fixed issues covered by regression checks.

## Scope

The framework is designed for authorized testing of:

- OpenAI-compatible model APIs
- Ollama and local model endpoints
- Retrieval-augmented generation systems
- Tool-using agents
- MCP clients and servers
- Multimodal and model-supply-chain surfaces

## Safety

Only test systems you own or are explicitly authorized to assess. The default project templates avoid destructive actions, real credentials, unrestricted networking, and uncontrolled execution of adversarial content.

Potentially high-impact tests should require explicit opt-in through policy and target configuration.

## Repository Layout

```text
src/aisec/          framework package
vulnerabilities/   versioned vulnerability packs
labs/              intentionally vulnerable and secured examples
policies/          reusable behavior and execution policies
schemas/           JSON schemas for manifests, targets, policies, and reports
configs/           example target and scan profiles
docs/              contributor and architecture documentation
scripts/           registry and documentation maintenance helpers
```

## Quick Start

```bash
python -m venv .venv
python -m pip install -e ".[dev]"
aisec validate registry
aisec list vulnerabilities
```

Example scan command:

```bash
aisec scan --target configs/targets/openai-compatible.example.yml --policy policies/default.yml
```

The foundation currently focuses on stable interfaces, schemas, templates, and safe defaults. Vulnerability packs and lab-specific tests can be added incrementally as new issues are discovered and reviewed.

## Vulnerability Packs

Each vulnerability should live in its own directory and include a manifest, safe cases, mitigation guidance, regression expectations, and references.

```text
vulnerabilities/<category>/<AIV-XXXX-slug>/
  manifest.yml
  README.md
  cases.yml
  secure/mitigation.md
  regression/vulnerable.expected.yml
  regression/secured.expected.yml
  references.md
```

Run validation before opening a pull request:

```bash
python scripts/validate_registry.py vulnerabilities
```
