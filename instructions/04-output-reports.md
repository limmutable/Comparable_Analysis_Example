# Stage 4: Output & Reports

Generate final deliverables and reports.

**Previous:** [Valuation Analysis](03-valuation.md) | **Next:** - | **Main:** [Workflow Overview](analysis-workflow.md)

---

## Overview

Compile all analysis outputs into professional deliverables: Markdown reports and CSV data files.

**Prompt Template:** `prompts/04-output-format.md`

---

## Quick Start

```bash
claude
# Compile final report
> "Compile all analysis files in output/nota/ into a final comprehensive report. Save to output/reports/nota-comps-report-{date}.md"

# Or with explicit prompt reference
> "Using prompts/04-output-format.md, compile all analysis for Nota into a final report with CSV exports"
```

---

## What You'll Learn

By completing this stage, you will understand:

1. **Output structure** - What files to create
2. **Formatting standards** - Consistent, professional output
3. **Report compilation** - Combining stage outputs
4. **Quality checks** - Validation before delivery

---

## Output Structure

```
output/
├── {company-name}/
│   ├── 01-target-summary.md      # Stage 1 output
│   ├── 02-peer-selection.md      # Stage 2 output
│   ├── 02-peer-data.csv          # Peer data export
│   ├── 03-valuation-analysis.md  # Stage 3 output
│   ├── 03-comps-table.csv        # Comps table export
│   └── 03-sensitivity.csv        # Sensitivity data
│
└── reports/
    └── {company-name}-comps-report-{YYYY-MM-DD}.md
```

---

## File Formats

| Type | Format | Use For |
|------|--------|---------|
| Markdown (.md) | Narrative | Reports, summaries, formatted tables |
| CSV (.csv) | Data | Spreadsheet-compatible data exports |

> **Reference:** See [Output Formatting Standards](shared-standards.md#output-formatting-standards) for detailed formatting rules.

---

## Final Report Structure

```markdown
# {Company Name} Comparable Analysis Report

**분석일:** YYYY-MM-DD
**분석가:** Claude AI

---

## Executive Summary
### 핵심 결론
- [Key finding 1]
- [Key finding 2]

### 밸류에이션 요약
| Method | Low | Mid | High |
|--------|-----|-----|------|
| EV/Revenue | $XXX M | $XXX M | $XXX M |
| **Blended** | **$XXX M** | **$XXX M** | **$XXX M** |

---

## 1. 회사 개요
[From 01-target-summary.md]

## 2. Peer Group 및 재무 데이터
[From 02-peer-selection.md]

## 3. 밸류에이션 분석
[From 03-valuation-analysis.md]

## 4. 리스크 및 제한사항
- [Limitation 1]
- [Risk 1]

---

## Appendix
### A. 데이터 출처
### B. 용어 정의

---
**Disclaimer:** 본 분석은 교육 목적으로 작성되었으며, 투자 권유가 아닙니다.
```

---

## Common Prompts

### Full Report Generation

```bash
> "Generate a complete comparable analysis report for {Company}. Include:
   - Executive summary with key findings
   - Company overview
   - Peer group analysis
   - Trading multiples comparison
   - Implied valuation range
   - Risk factors
   Save to output/reports/{company}-comps-report-{date}.md"
```

### Compile from Existing

```bash
> "Combine the analysis files in output/{company}/ into a single formatted report:
   - 01-target-summary.md
   - 02-peer-selection.md
   - 03-valuation-analysis.md
   Add executive summary and save to output/reports/"
```

### Export to CSV

```bash
> "Export the comps table to CSV with columns:
   Company, Ticker, Revenue, EBITDA, Market Cap, EV, EV/Revenue, EV/EBITDA
   Save to output/{company}/03-comps-table.csv"
```

---

## Quality Checklist

### Content
- [ ] All sections complete
- [ ] Numbers verified and consistent
- [ ] Sources cited for all data
- [ ] Assumptions documented
- [ ] Limitations disclosed

### Formatting
- [ ] Tables properly aligned
- [ ] Units clearly labeled
- [ ] Consistent decimal places
- [ ] Date stamp included

### Files
- [ ] Markdown renders correctly
- [ ] CSV opens in Excel/Sheets
- [ ] File names follow convention

---

## Post-Analysis Steps

1. **Review** - Verify calculations against source documents
2. **Archive** - Keep source files in dataroom for reference
3. **Share** - Distribute reports to stakeholders
4. **Update** - Refresh analysis when new data available

---

## Workflow Complete

Congratulations! You've completed the comparable analysis workflow.

**Deliverables Created:**
- Target company summary
- Peer group selection with financial data
- Trading multiples analysis
- Implied valuation range
- Sensitivity analysis
- Final comprehensive report

**Return to:** [Workflow Overview](analysis-workflow.md)
