---
name: doc-prepare-activator
description: Automatically activates doc-prepare skill when large documents or SEC filings are mentioned
event: UserPromptSubmit
---

# Document Preparation Hook

This hook monitors for keywords indicating the user wants to analyze large documents and reminds Claude to check document sizes first.

## Trigger Keywords

Activate when the user prompt contains:
- `10-K` or `10-Q` (SEC filings)
- `증권신고서` (Korean SEC filing)
- `large PDF` or `big document`
- `context limit` or `token limit`
- `prep document` or `prepare document`
- Paths containing `dataroom/` with `.pdf`

## Action

When triggered, prepend this reminder to Claude's context:

```
IMPORTANT: Before reading any large PDF (especially 10-K, 10-Q, or 증권신고서):
1. First check file size: uv run python scripts/check_document_size.py {file}
2. If TOO LARGE, extract pages first using scripts/prep_documents.py
3. Only then proceed with analysis using extracted files from .working/

See .claude/skills/doc-prepare/SKILL.md for full workflow.
```

## Configuration

```yaml
match_patterns:
  - "10-K"
  - "10-Q"
  - "증권신고서"
  - "SEC filing"
  - "large PDF"
  - "context limit"
  - "dataroom/*.pdf"

action: inject_context
priority: high
```
