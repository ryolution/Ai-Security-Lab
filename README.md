# AI Security Lab

A simple starter workspace for manual AI vulnerability research.

The project is intentionally small:

```text
template/
vulnerabilities/
```

Use it to collect AI/LLM/RAG/agent/MCP security tests, lab notes, attack assets,
mitigation notes, demos, and blog drafts.

## Structure

```text
vulnerabilities/
  agents/
  data-leakage/
  llm/
  mcp/
  models/
  multimodal/
  prompt-injection/
  rag/
  supply-chain/
  tool-use/

template/
  vulnerability/
    README.md
    lab-setup.md
    assets/
    secure/
    blog/
    demo/
    evidence/
```

## Add A Vulnerability

1. Pick the category in `vulnerabilities/`.
2. Copy `template/vulnerability/` into that category.
3. Rename the copied folder, for example:

```text
vulnerabilities/rag/example-vulnerability-name/
```

Windows PowerShell:

```powershell
Copy-Item -Recurse template\vulnerability vulnerabilities\rag\example-vulnerability-name
```

Linux Bash:

```bash
cp -r template/vulnerability vulnerabilities/rag/example-vulnerability-name
```

4. Fill in:

```text
README.md
lab-setup.md
assets/
secure/
blog/
demo/before/
demo/after/
evidence/
```

## Workflow

```text
Research -> run a real lab -> attack manually -> secure -> retest -> write it up
```

This repo does not decide automatically whether a vulnerability is valid or
fixed. You run the lab, capture evidence, make the security change, and retest.

## Private Notes

Use local files for private research:

```text
*.local.md
*.private.md
*.evidence.local.md
blog-drafts/
research-notes/
private-notes/
```

Those paths are ignored by Git.

## Useful Commands

List category folders on Windows:

```powershell
Get-ChildItem vulnerabilities -Directory
```

List category folders on Linux:

```bash
find vulnerabilities -mindepth 1 -maxdepth 1 -type d | sort
```

Create a private blog draft folder on Windows:

```powershell
New-Item -ItemType Directory -Force blog-drafts
```

Create a private blog draft folder on Linux:

```bash
mkdir -p blog-drafts
```
