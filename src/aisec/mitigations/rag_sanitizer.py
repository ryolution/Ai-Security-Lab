"""RAG document sanitization helpers."""

from __future__ import annotations


def strip_hidden_markdown_instructions(document: str) -> str:
    lines = []
    for line in document.splitlines():
        stripped = line.strip()
        if stripped.startswith("<!--") and stripped.endswith("-->"):
            continue
        lines.append(line)
    return "\n".join(lines)
