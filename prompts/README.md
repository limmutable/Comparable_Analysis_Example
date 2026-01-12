# Prompts Directory

This directory contains modular, reusable prompt templates for financial analysis.

## Prompt Index

| File | Description | Workflow Stage | Key Features |
|------|-------------|----------------|--------------|
| `_base.md` | Shared configuration | All stages | Reasoning protocol, citation standards |
| `_extract-financials.md` | Financial data extraction (utility) | Referenced by others | Reusable data extraction methodology |
| `01-target-summary.md` | Target company analysis | [Stage 1](../instructions/01-target-analysis.md) | `<thinking>` validation, source citations |
| `02-peer-selection.md` | Peer selection + data extraction | [Stage 2](../instructions/02-peer-selection.md) | Qualitative validation, financial data |
| `03-valuation-analysis.md` | Trading multiples & valuation | [Stage 3](../instructions/03-valuation.md) | Premium/discount justification |
| `04-output-format.md` | Report formatting | [Stage 4](../instructions/04-output-reports.md) | Markdown/CSV templates |
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

# Step 2: Peer selection + data extraction
> "Using prompts/02-peer-selection.md, identify 5-7 comparable companies and extract their financial data"

# Step 3: Valuation
> "Using prompts/03-valuation-analysis.md, calculate implied valuation"

# Step 4: Format output
> "Using prompts/04-output-format.md, generate final report"
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
┌─────────────────────┐     ┌─────────────────────┐
│ 02-peer-selection   │────▶│ _extract-financials │
│ (includes data)     │     │ (utility prompt)    │
└─────────┬───────────┘     └─────────────────────┘
          │
          ▼
┌─────────────────────┐
│ 03-valuation        │  → Trading multiples, implied value
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ 04-output-format    │  → Final report (MD) + data (CSV)
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

## Utility Prompt Pattern

Files prefixed with underscore (`_`) are **utility prompts** - reusable components referenced by other prompts:

| File | Purpose | Referenced By |
|------|---------|---------------|
| `_base.md` | Shared configuration (role, language, citation standards) | All prompts |
| `_extract-financials.md` | Standardized financial data extraction methodology | `01-target-summary.md`, `02-peer-selection.md` |

**Why use utility prompts?**
- **DRY principle**: Don't repeat extraction logic in every prompt
- **Consistency**: All stages use identical methodology
- **Maintainability**: Update logic in one place

**Creating a utility prompt:**
1. Name it with underscore prefix: `_my-utility.md`
2. Design for reuse (no stage-specific content)
3. Reference from other prompts: `**Utility Reference:** See prompts/_my-utility.md`

## Creating Custom Prompts

1. Copy an existing prompt as a template
2. Reference `_base.md` at the top: `**Base configuration:** See prompts/_base.md`
3. Reference utility prompts as needed (e.g., `_extract-financials.md`)
4. Define clear Objective, Input Requirements, and Output Format
5. Save with descriptive filename (e.g., `dcf-valuation.md`)

## Related Documentation

### Workflow Guides (`/instructions/`)

| Document | Description |
|----------|-------------|
| [Analysis Workflow](../instructions/analysis-workflow.md) | Overview and navigation hub |
| [Shared Standards](../instructions/shared-standards.md) | **Methodology hub**: Peer criteria, valuation formulas, templates |
| [00-dataroom-setup.md](../instructions/00-dataroom-setup.md) | Stage 0: Prepare source materials |
| [01-target-analysis.md](../instructions/01-target-analysis.md) | Stage 1: Analyze target company |
| [02-peer-selection.md](../instructions/02-peer-selection.md) | Stage 2: Select peers + extract data |
| [03-valuation.md](../instructions/03-valuation.md) | Stage 3: Valuation analysis |
| [04-output-reports.md](../instructions/04-output-reports.md) | Stage 4: Generate reports |

### Reference Materials

- [Key Metrics Reference](../.claude/skills/financial-analysis/key-metrics.md) - Financial formulas and definitions
- [Financial Analysis Skill](../.claude/skills/financial-analysis/SKILL.md) - Claude skill for comps analysis
- [Financial Modeling Skill](../.claude/skills/financial-modeling/SKILL.md) - Claude skill for DCF/forecasts
