# Architecture

AI Security Lab separates test generation, target execution, detection, evaluation, mitigation, and reporting.

## Core Flow

```text
Load target -> Load policy -> Select packs -> Run probes -> Detect -> Evaluate -> Report
```

## Boundaries

- Targets normalize access to LLM APIs, local models, RAG systems, agents, and MCP surfaces.
- Probes create or execute test actions.
- Detectors decide whether unsafe behavior occurred.
- Evaluators combine detector outputs into normalized statuses.
- Mitigations describe or implement defensive controls.
- Runners isolate and schedule execution.
- Reports preserve evidence with redaction.

Vulnerability content should live in `vulnerabilities/`. Framework behavior should live in `src/aisec/`.
