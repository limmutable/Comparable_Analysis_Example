# Prompts Directory

This directory contains modular, reusable prompt templates for financial analysis.

## Prompt Index

| File | Description | Workflow Stage | Key Features |
|------|-------------|----------------|--------------|
| `_base.md` | Shared configuration | All stages | Reasoning protocol, citation standards |
| `01-target-summary.md` | Target company analysis | [Stage 2](../instructions/02-target-analysis.md) | `<thinking>` validation, source citations |
| `02-peer-selection.md` | Peer group identification | [Stage 3](../instructions/03-peer-selection.md) | Qualitative validation, feature overlap |
| `03-data-extraction.md` | Financial data collection | [Stage 4](../instructions/04-valuation.md) | Self-correction, source tracking |
| `04-valuation-analysis.md` | Trading multiples & valuation | [Stage 4](../instructions/04-valuation.md) | Premium/discount justification |
| `05-output-format.md` | Report formatting | [Stage 5](../instructions/05-output-reports.md) | Markdown/CSV templates |
| `startup-comps-full.md` | Complete workflow | [All Stages](../instructions/analysis-workflow.md) | End-to-end orchestration |

## Quick Start

### Run Full Analysis

```bash
claude
> "Using prompts/startup-comps-full.md, perform a complete comparable company analysis for the company in dataroom/target-company/"
```

### Run Individual Modules

```bash
# Step 1: Target summary
> "Using prompts/01-target-summary.md, analyze dataroom/company/pitch-deck.pdf"

# Step 2: Peer selection
> "Using prompts/02-peer-selection.md, identify 5-7 comparable companies"

# Step 3: Data extraction
> "Using prompts/03-data-extraction.md, extract financials for all peers"

# Step 4: Valuation
> "Using prompts/04-valuation-analysis.md, calculate implied valuation"

# Step 5: Format output
> "Using prompts/05-output-format.md, generate final report"
```

## Workflow Diagram

```
┌─────────────────────┐
│   _base.md          │  (Shared configuration)
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ 01-target-summary   │  → Company overview, financials, risks
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ 02-peer-selection   │  → Comparable companies list
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ 03-data-extraction  │  → Financial data for all companies
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ 04-valuation        │  → Trading multiples, implied value
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ 05-output-format    │  → Final report (MD) + data (CSV)
└─────────────────────┘
```

## Output Language

All prompts are configured to:
- **Research:** Any language (use best available sources)
- **Output:** Korean (한국어) with English financial terms

To change output language, modify the Language Settings section in `_base.md`.

## Quality Standards (from `_base.md`)

### Reasoning Protocol (Chain-of-Thought)
1. **Identify the Goal** - State what needs to be analyzed
2. **Data Survey** - List available data and sources before calculating
3. **Logic Step** - Explain *why* a calculation is being made
4. **Execution** - Perform the calculation
5. **Sanity Check** - Validate (e.g., "Does 90% margin make sense?")
6. **Final Output** - Present in requested format

### Citation Standard (Strict)
Every number requires a source citation:
```
Revenue: $100M [10-K-2023.pdf, p.45]
EBITDA: $15M [Calc: Operating Income + D&A]
```

### Self-Correction (`<thinking>` blocks)
Each prompt includes validation logic:
```
<thinking>
Check if EBITDA > Revenue (Impossible - verify units)
Check if Net Income > EBITDA (Unlikely unless one-off gain)
</thinking>
```

## Creating Custom Prompts

1. Copy an existing prompt as a template
2. Reference `_base.md` at the top: `**Base configuration:** See prompts/_base.md`
3. Define clear Objective, Input Requirements, and Output Format
4. Save with descriptive filename (e.g., `dcf-valuation.md`)

## Related Documentation

### Workflow Guides (`/instructions/`)

| Document | Description |
|----------|-------------|
| [Analysis Workflow](../instructions/analysis-workflow.md) | Overview and navigation hub |
| [01-dataroom-setup.md](../instructions/01-dataroom-setup.md) | Stage 1: Prepare source materials |
| [02-target-analysis.md](../instructions/02-target-analysis.md) | Stage 2: Analyze target company |
| [03-peer-selection.md](../instructions/03-peer-selection.md) | Stage 3: Select peer group |
| [04-valuation.md](../instructions/04-valuation.md) | Stage 4: Valuation analysis |
| [05-output-reports.md](../instructions/05-output-reports.md) | Stage 5: Generate reports |

### Reference Materials

- [Key Metrics Reference](../.claude/skills/financial-analysis/key-metrics.md) - Financial formulas and definitions
- [Financial Analysis Skill](../.claude/skills/financial-analysis/SKILL.md) - Claude skill for comps analysis
- [Financial Modeling Skill](../.claude/skills/financial-modeling/SKILL.md) - Claude skill for DCF/forecasts
