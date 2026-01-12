# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an educational project demonstrating how to automate comparable financial analysis for investors using AI tools (Claude and Gemini CLI apps) and Python scripts. The project generates financial statements, peer group comparisons, valuation analysis, and related financial documents.

## Directory Structure

- `/dataroom` - Source documents (e.g., SEC filings as PDFs)
- `/prompts` - LLM prompts for financial analysis tasks
- `/scripts` - User-facing utility scripts (document processing, extraction)
- `/instructions` - Educational materials, instructions, and how-to guides for students
- `/.working` - Temporary/intermediate files (pre-extracted PDFs) - auto-generated, gitignored
- `/output` - Final analysis outputs and reports
- `/src` - Internal source code for project tooling (not student-facing)

## Claude Code Skills

This project includes custom skills in `.claude/skills/`:

- **doc-prepare** - Prepare large documents (10-K, SEC filings) for analysis by checking sizes and extracting pages
- **financial-analysis** - Comparable company analysis, financial statement analysis, valuation multiples
- **financial-modeling** - Build financial models, forecasts, DCF valuations

These skills are automatically activated when relevant to your request.

**Hooks:** The `doc-prepare-activator` hook (`.claude/hooks/`) triggers document size checks when SEC filings or large PDFs are mentioned.

## Analysis Workflow (5 Stages)

| Stage | Instruction | Prompt | Description |
|-------|-------------|--------|-------------|
| 0 | `00-dataroom-setup.md` | - | Organize source documents |
| 1 | `01-target-analysis.md` | `01-target-summary.md` | Analyze target company |
| 2 | `02-peer-selection.md` | `02-peer-selection.md` | Select peers + extract data |
| 3 | `03-valuation.md` | `03-valuation-analysis.md` | Calculate valuation multiples |
| 4 | `04-output-reports.md` | `04-output-format.md` | Generate final reports |

**Utility Prompts:** Files prefixed with `_` (e.g., `_base.md`, `_extract-financials.md`) are reusable components referenced by other prompts.

**Full Workflow:** Use `prompts/startup-comps-full.md` to run all stages end-to-end.

## Development Rules

- Educational materials go in `/instructions`
- Educational scripts go in `/scripts`
- Internal tooling goes in `/src`
- All outputs should be Markdown, CSV, or plain text (no frontend/website)
