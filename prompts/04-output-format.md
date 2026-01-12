# Output Formatting Prompt

**Base configuration:** See `prompts/_base.md` for role, language, data sources, and standards.

---

## Objective

Compile all analysis outputs into a final professional report and export data tables as CSV.

---

## Quick Reference

| Output Type | Format | Location |
|-------------|--------|----------|
| Target Summary | Markdown | `output/{company}/01-target-summary.md` |
| Peer Selection | Markdown + CSV | `output/{company}/02-peer-selection.md`, `02-peer-data.csv` |
| Valuation | Markdown + CSV | `output/{company}/03-valuation-analysis.md`, `03-comps-table.csv` |
| Final Report | Markdown | `output/reports/{company}-comps-report-{date}.md` |

---

## Output Directory Structure

```
output/
├── {company-name}/
│   ├── 01-target-summary.md
│   ├── 02-peer-selection.md
│   ├── 02-peer-data.csv
│   ├── 03-valuation-analysis.md
│   └── 03-comps-table.csv
└── reports/
    └── {company-name}-comps-report-{YYYY-MM-DD}.md
```

---

## Formatting Standards

> **Reference:** See `instructions/shared-standards.md#output-formatting-standards` for detailed formatting rules.

### Document Header

```markdown
# {Document Title}

**회사:** {Company Name}
**분석일:** {YYYY-MM-DD}
**분석가:** Claude AI
**버전:** v1.0

---
```

### Numeric Tables

- Right-align numbers: `|---:|`
- Include units in header: `Revenue ($M)`
- Use consistent decimals (2 for currency, 1 for multiples)
- Bold summary rows

### CSV Files

- Use snake_case headers: `revenue_m`, `ev_ebitda_x`
- Include unit suffix: `_m` (millions), `_pct` (percent), `_x` (multiples)
- No commas in numbers

---

## Final Report Template

**Save to:** `output/reports/{company}-comps-report-{YYYY-MM-DD}.md`

```markdown
# {Company Name} Comparable Analysis Report

**분석일:** {YYYY-MM-DD}
**분석가:** Claude AI

---

## Executive Summary

### 핵심 결론
- [Key finding 1]
- [Key finding 2]

### 밸류에이션 요약

| 방법론 | Low | Mid | High |
|--------|-----|-----|------|
| EV/Revenue | $XXX M | $XXX M | $XXX M |
| **Blended** | **$XXX M** | **$XXX M** | **$XXX M** |

---

## 1. 회사 개요

[Content from 01-target-summary.md]

---

## 2. Peer Group 및 재무 데이터

[Content from 02-peer-selection.md]

---

## 3. 밸류에이션 분석

[Content from 03-valuation-analysis.md]

---

## 4. 리스크 및 제한사항

### 분석 제한사항
- [Limitation 1]

### 주요 리스크
- [Risk 1]

---

## Appendix

### A. 데이터 출처
| 데이터 | 출처 | 날짜 |
|--------|------|------|
| SEC Filings | SEC EDGAR | YYYY-MM-DD |

### B. 용어 정의
| 용어 | 정의 |
|------|------|
| EV | Enterprise Value = Market Cap + Debt - Cash |
| EBITDA | Earnings Before Interest, Taxes, Depreciation & Amortization |

---

**Disclaimer:** 본 분석은 교육 목적으로 작성되었으며, 투자 권유가 아닙니다.
```

---

## Quality Checklist

### Content
- [ ] All sections complete
- [ ] Numbers verified and consistent
- [ ] Sources cited for all data

### Formatting
- [ ] Tables properly aligned
- [ ] Units clearly labeled
- [ ] Date stamp included

### Files
- [ ] Markdown renders correctly
- [ ] CSV opens in Excel/Sheets
- [ ] File names follow convention
