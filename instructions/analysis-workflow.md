# Analysis Workflow Guide

This guide provides a structured approach to conducting comparable financial analysis. Each workflow stage has its own detailed guide.

---

## Workflow Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                        ANALYSIS WORKFLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐            │
│   │  1. Setup   │───▶│  2. Target  │───▶│  3. Peers   │            │
│   │  Dataroom   │    │  Analysis   │    │  Selection  │            │
│   └─────────────┘    └─────────────┘    └─────────────┘            │
│         │                  │                  │                     │
│         ▼                  ▼                  ▼                     │
│   01-dataroom-      02-target-         03-peer-                    │
│   setup.md          analysis.md        selection.md                │
│                                                                     │
│   ┌─────────────┐    ┌─────────────┐                               │
│   │ 4. Valuation│───▶│ 5. Output & │                               │
│   │  Analysis   │    │   Reports   │                               │
│   └─────────────┘    └─────────────┘                               │
│         │                  │                                        │
│         ▼                  ▼                                        │
│   04-valuation.md    05-output-                                    │
│                      reports.md                                     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Workflow Stages

| Stage | Guide | Description | Prompt Template |
|-------|-------|-------------|-----------------|
| 1 | [Dataroom Setup](01-dataroom-setup.md) | Prepare and organize source materials | - |
| 2 | [Target Analysis](02-target-analysis.md) | Analyze target company financials | `prompts/01-target-summary.md` |
| 3 | [Peer Selection](03-peer-selection.md) | Identify comparable companies | `prompts/02-peer-selection.md` |
| 4 | [Valuation Analysis](04-valuation.md) | Calculate multiples and implied value | `prompts/03-data-extraction.md`, `prompts/04-valuation-analysis.md` |
| 5 | [Output & Reports](05-output-reports.md) | Generate deliverables | `prompts/05-output-format.md` |

**Full Workflow Prompt:** `prompts/startup-comps-full.md` - Runs all stages end-to-end

---

## Quick Start

### Option 1: Run Full Analysis (Automated)

```bash
cd ~/Projects/Comparable_Analysis_Example
claude

> "Using prompts/startup-comps-full.md, perform a complete comparable company analysis for the company in dataroom/target-company/"
```

### Option 2: Run Stage by Stage (Manual)

```bash
# Stage 1: Setup dataroom (manual - see 01-dataroom-setup.md)

# Stage 2: Target analysis
> "Using prompts/01-target-summary.md, analyze dataroom/target-company/10-K-2024.pdf"

# Stage 3: Peer selection
> "Using prompts/02-peer-selection.md, identify 5-7 comparable companies"

# Stage 4: Valuation analysis
> "Using prompts/04-valuation-analysis.md, calculate implied valuation"

# Stage 5: Generate report
> "Using prompts/05-output-format.md, generate final report to output/reports/"
```

---

## Project Structure Reference

```
Comparable_Analysis_Example/
├── dataroom/              # Source documents (Stage 1)
│   ├── target-company/
│   ├── peer-companies/
│   └── market-data/
├── prompts/               # Analysis prompt templates
│   ├── _base.md
│   ├── 01-target-summary.md
│   ├── 02-peer-selection.md
│   ├── 03-data-extraction.md
│   ├── 04-valuation-analysis.md
│   ├── 05-output-format.md
│   └── startup-comps-full.md
├── scripts/               # Utility scripts
│   ├── check_document_size.py   # Check file sizes
│   └── extract_sections.py      # Extract PDF sections
├── .working/              # Intermediate files (pre-extracted PDFs)
│   └── {company-name}/    # Auto-created by make extract-pages
├── output/                # Final analysis outputs (Stage 5)
│   ├── {company-name}/
│   └── reports/
├── instructions/          # This documentation
│   ├── README.md
│   ├── getting-started.md
│   ├── analysis-workflow.md  ← You are here
│   ├── 01-dataroom-setup.md
│   ├── 02-target-analysis.md
│   ├── 03-peer-selection.md
│   ├── 04-valuation.md
│   └── 05-output-reports.md
└── .claude/skills/        # Claude skills
    ├── financial-analysis/
    └── financial-modeling/
```

---

## Quality Standards

All analysis follows these standards (defined in `prompts/_base.md`):

### Reasoning Protocol
1. **Identify Goal** → State analysis objective
2. **Data Survey** → List available sources
3. **Logic Step** → Explain calculations
4. **Execution** → Perform analysis
5. **Sanity Check** → Validate results
6. **Output** → Present findings

### Citation Requirements
- Every number needs a source: `[File, Page X]`
- Calculated values: `[Calc: formula]`
- Missing data: `"Data Not Available"`

### Output Language
- **Research:** Any language
- **Output:** Korean (한국어) with English financial terms

---

## Claude Skills

Two skills auto-activate based on your request:

| Skill | Activates When | Example |
|-------|----------------|---------|
| `financial-analysis` | Comps, financial statements, multiples | "Create a comp table" |
| `financial-modeling` | DCF, forecasts, projections | "Build a 5-year DCF model" |

---

## Common Commands

| Task | Command |
|------|---------|
| Read filing | `"Read dataroom/[file].pdf and summarize key financials"` |
| Extract data | `"Extract revenue, EBITDA, net income from the 10-K"` |
| Create comps | `"Create a comparable company analysis table"` |
| Calculate multiples | `"Calculate EV/EBITDA and P/E multiples"` |
| Build DCF | `"Build a DCF model with 5-year projections"` |
| Generate report | `"Generate analysis report, save to output/"` |
| Export CSV | `"Export data to CSV format"` |

---

## Key Metrics Reference

See `.claude/skills/financial-analysis/key-metrics.md` for:
- Valuation multiples (EV/EBITDA, P/E, EV/Revenue)
- Profitability ratios (margins, ROE, ROIC)
- Liquidity ratios (current ratio, quick ratio)
- Leverage ratios (Debt/EBITDA, interest coverage)

---

## Troubleshooting

### "Exceeds context window limit"

**Cause:** Document is too large for the LLM's context window.

**Solution:**
```bash
# 1. Check file sizes
make check

# 2. Pre-extract specific pages (recommended)
make extract-pages FILE=dataroom/nota/nota-sec.pdf PAGES=80-120 OUT=.working/nota/financials.txt

# 3. Then analyze the extracted file
claude
> "Read .working/nota/financials.txt and extract key financial metrics"
```

See [Target Analysis - Handling Large Documents](02-target-analysis.md#handling-large-documents) for detailed strategies.

### "File not found" errors

**Cause:** Incorrect file path or file not in dataroom.

**Solution:**
```bash
# Check dataroom contents
ls -la dataroom/

# Use correct relative path from project root
> "Read dataroom/nota/nota-sec.pdf"  # NOT "Read nota-sec.pdf"
```

### "No financial data found"

**Cause:** Looking in wrong section of 10-K.

**Solution:**
- Item 6 (pages ~45-55): 5-year financial summary
- Item 8 (pages ~80-130): Full financial statements
- Try: `"Read pages 45-55 of the 10-K and find Selected Financial Data"`

### Scripts not working

**Cause:** Missing Python dependencies.

**Solution:**
```bash
# For PDF extraction
pip install PyPDF2

# Check Python version (3.7+ required)
python --version
```

---

## Next Steps

1. **New to the project?** → Start with [Getting Started](getting-started.md)
2. **Ready to analyze?** → Begin with [Dataroom Setup](01-dataroom-setup.md)
3. **Have source docs?** → Jump to [Target Analysis](02-target-analysis.md)
