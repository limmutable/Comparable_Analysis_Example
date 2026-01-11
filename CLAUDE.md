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

- **financial-modeling** - Build financial models, forecasts, DCF valuations
- **financial-analysis** - Comparable company analysis, financial statement analysis, valuation multiples

These skills are automatically activated when relevant to your request.

## Development Rules

- Educational materials go in `/instructions`
- Educational scripts go in `/scripts`
- Internal tooling goes in `/src`
- All outputs should be Markdown, CSV, or plain text (no frontend/website)
