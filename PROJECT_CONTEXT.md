# Project Context

AI Security Lab is a clean starter structure for manual AI vulnerability
research.

The repo has one folder for vulnerability categories:

```text
vulnerabilities/
```

Inside it, each category has its own folder. When a new vulnerability is tested,
copy `template/vulnerability/` into the right category and fill it in manually.

## Goal

Keep the project easy to use:

- no scanner framework
- no prefilled vulnerability examples
- no complex CLI
- one reusable template
- one category folder for each vulnerability type

## Workflow

```text
Research -> reproduce in a lab -> attack manually -> secure -> retest -> document
```

The human researcher decides whether the vulnerability is valid and whether the
mitigation actually works.
