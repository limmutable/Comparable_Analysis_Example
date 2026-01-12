# Instructions

Welcome to the Comparable Analysis project documentation. This directory contains educational materials to help you learn automated financial analysis using AI tools.

## Documentation Index

### Getting Started

| Document | Description |
|----------|-------------|
| [Getting Started](getting-started.md) | Environment setup, CLI installation, project configuration |

### Analysis Workflow

| Document | Description |
|----------|-------------|
| [Analysis Workflow](analysis-workflow.md) | Overview and navigation hub for all workflow stages |

### Workflow Stages

| Stage | Document | Description | Prompt |
|-------|----------|-------------|--------|
| 0 | [Dataroom Setup](00-dataroom-setup.md) | Prepare and organize source materials | - |
| 1 | [Target Analysis](01-target-analysis.md) | Analyze target company financials | `01-target-summary.md` |
| 2 | [Peer Selection](02-peer-selection.md) | Identify peers and extract financial data | `02-peer-selection.md` |
| 3 | [Valuation Analysis](03-valuation.md) | Calculate multiples and implied value | `03-valuation-analysis.md` |
| 4 | [Output & Reports](04-output-reports.md) | Generate deliverables | `04-output-format.md` |

### Reference

| Document | Description |
|----------|-------------|
| [Shared Standards](shared-standards.md) | Consolidated methodology, criteria, and templates used across all stages |

---

## Suggested Learning Path

```
┌─────────────────┐
│ Getting Started │  ← Start here
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│Analysis Workflow│  ← Overview
└────────┬────────┘
         │
    ┌────┴────┐
    ▼         ▼
Stage 1 → Stage 2 → Stage 3 → Stage 4
```

1. **[Getting Started](getting-started.md)** - Set up development environment, install CLI tools
2. **[Analysis Workflow](analysis-workflow.md)** - Understand the overall workflow
3. **[Dataroom Setup](00-dataroom-setup.md)** - Organize source documents
4. **[Target Analysis](01-target-analysis.md)** - Analyze target company
5. **[Peer Selection](02-peer-selection.md)** - Select peers and extract financial data
6. **[Valuation Analysis](03-valuation.md)** - Calculate multiples and valuation
7. **[Output & Reports](04-output-reports.md)** - Generate final deliverables

---

## Quick Links

| Resource | Location | Description |
|----------|----------|-------------|
| Source Documents | `../dataroom/` | SEC filings and input documents |
| Prompt Templates | `../prompts/` | Reusable analysis prompts |
| Analysis Outputs | `../output/` | Generated reports and data |
| Claude Skills | `../.claude/skills/` | Auto-activated analysis skills |
| Scripts | `../scripts/` | Educational Python scripts |

---

## Related Documentation

- **[Prompts README](../prompts/README.md)** - Prompt template index and usage
- **[Key Metrics Reference](../.claude/skills/financial-analysis/key-metrics.md)** - Financial formulas and definitions

---

## Need Help?

- **Setup Issues:** Check [Troubleshooting](getting-started.md#troubleshooting) in Getting Started
- **Workflow Questions:** See [Analysis Workflow](analysis-workflow.md) overview
- **Prompt Usage:** See [Prompts README](../prompts/README.md)
