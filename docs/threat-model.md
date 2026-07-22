# Threat Model

AI Security Lab treats all vulnerability inputs and target outputs as untrusted.

## Untrusted Inputs

- Prompts and payload files
- Model responses
- Retrieved documents
- Tool descriptions and tool outputs
- MCP server data
- Model files and plugins
- Generated reports and external integration data

## Required Controls

- Explicit authorization before scanning
- Default-deny network policy for sandboxed execution
- Resource limits for time, tokens, tools, memory, and process count
- Secret redaction before logs and reports
- Path validation for files read from vulnerability packs
- No destructive tests by default

## Non-Goals

A passing scan does not prove that a system is secure. It means the configured tests did not produce failing evidence under the selected policy and target conditions.
