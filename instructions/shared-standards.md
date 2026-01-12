# Shared Standards & Methodology Reference

This document consolidates reusable methodology, criteria, and standards used across all workflow stages. Reference this file instead of duplicating content.

**Usage:** Link to specific sections from stage instructions using `[Section Name](shared-standards.md#section-anchor)`.

---

## Table of Contents

1. [Large Document Handling](#large-document-handling)
2. [Financial Data Points](#financial-data-points)
3. [Peer Selection Criteria](#peer-selection-criteria)
4. [Valuation Multiples](#valuation-multiples)
5. [Sensitivity Analysis Templates](#sensitivity-analysis-templates)
6. [Data Validation Rules](#data-validation-rules)
7. [Output Formatting Standards](#output-formatting-standards)

---

## Large Document Handling

> **Token Limit Warning:** Full 10-K filings (100-300 pages) often exceed LLM context windows.

### Check Document Size First

```bash
uv run python scripts/check_document_size.py dataroom/
```

### Strategy A: Page-Range Reading (Recommended)

```bash
# Quick company overview
> "Read pages 1-10 of dataroom/company/10-K.pdf and summarize"

# Financial summary (Item 6)
> "Read pages 45-55 of the 10-K and extract Selected Financial Data"

# Full financials (Item 8)
> "Read pages 80-100 and extract Income Statement and Balance Sheet"
```

### Strategy B: Pre-Extract with Scripts

```bash
uv run python scripts/extract_sections.py dataroom/company/10-K.pdf --pages 80-120 --output .working/company/financials.txt
```

### 10-K Section Reference

| Section | Typical Pages | Content |
|---------|---------------|---------|
| Cover & TOC | 1-5 | Basic info |
| Item 1: Business | 6-25 | Business description |
| Item 1A: Risk Factors | 25-45 | Risks |
| Item 6: Selected Financial | 45-55 | 5-year summary |
| Item 7: MD&A | 55-80 | Management discussion |
| Item 8: Financials | 80-130 | Full financial statements |

---

## Financial Data Points

### From Income Statement

| Metric | Description | Source |
|--------|-------------|--------|
| Revenue | Total net sales | Income Statement |
| COGS | Cost of goods sold | Income Statement |
| Gross Profit | Revenue - COGS | Calculated |
| EBIT | Operating Income | Income Statement |
| EBITDA | EBIT + D&A | Calculated |
| Net Income | Bottom line | Income Statement |
| EPS (Diluted) | Net Income / Diluted Shares | Income Statement |

### From Balance Sheet

| Metric | Description | Source |
|--------|-------------|--------|
| Cash & Equivalents | Cash + short-term investments | Balance Sheet |
| Total Assets | All assets | Balance Sheet |
| Total Debt | Short-term + Long-term debt | Balance Sheet / Notes |
| Shareholders' Equity | Total equity | Balance Sheet |

### From Cash Flow Statement

| Metric | Description | Source |
|--------|-------------|--------|
| Operating Cash Flow | Cash from operations | Cash Flow |
| CapEx | Capital expenditures | Cash Flow |
| Free Cash Flow | OCF - CapEx | Calculated |
| D&A | Depreciation & Amortization | Cash Flow |

---

## Peer Selection Criteria

### Primary Criteria (Must Match)

| Criterion | Description | Weight |
|-----------|-------------|--------|
| **Industry** | Same GICS sub-industry or direct competitor | High |
| **Business Model** | Similar revenue model (SaaS, transactional) | High |
| **Revenue Stage** | Within 0.25x - 4.0x of target revenue | Medium |

### Secondary Criteria (Should Match)

| Criterion | Description | Weight |
|-----------|-------------|--------|
| **Growth Profile** | Similar revenue growth rate (±10%) | Medium |
| **Profitability** | Similar margin profile | Medium |
| **Geography** | Same primary market | Low |
| **Customer Base** | B2B vs B2C, enterprise vs SMB | Low |

### Red Flags (Consider Exclusion)

- Negative EBITDA → Exclude from EV/EBITDA comps
- Recent large M&A → Distorted financials
- Pending delisting → Price unreliable
- Revenue concentration >50% in different segment
- Regulatory overhang or major litigation

### Special Cases

**When Direct Competitors Are Private:**
1. Expand to adjacent industries with similar business models
2. Include larger public players (with size adjustment notes)
3. Include international peers from similar markets
4. Document that direct comps are limited

**For Pre-Profit Companies:**
1. Use EV/Revenue only (not EV/EBITDA or P/E)
2. Prioritize growth rate similarity over absolute size
3. Include other pre-profit peers
4. Reference recent funding rounds as context

---

## Valuation Multiples

### Enterprise Value Multiples

| Multiple | Formula | When to Use |
|----------|---------|-------------|
| EV/Revenue | EV / Revenue | High-growth, negative EBITDA |
| EV/EBITDA | EV / EBITDA | Most common for profitable cos |
| EV/EBIT | EV / EBIT | Capital-intensive industries |

### Equity Multiples

| Multiple | Formula | When to Use |
|----------|---------|-------------|
| P/E | Price / EPS | Stable, profitable companies |
| P/S | Market Cap / Revenue | Growth companies |
| P/B | Price / Book Value | Asset-heavy industries |

### Pre-Profit Company Handling

| Target Status | Use | Avoid |
|---------------|-----|-------|
| Pre-profit, high growth | EV/Revenue | EV/EBITDA, P/E |
| Pre-profit, low growth | EV/Revenue (low multiple) | All profit-based |
| Profitable | All methods | None |

### Growth-Multiple Relationship

| Growth Rate | Typical EV/Revenue |
|-------------|-------------------|
| <10% | 1.0x - 3.0x |
| 10-30% | 2.0x - 5.0x |
| 30-50% | 4.0x - 8.0x |
| 50-100% | 6.0x - 15.0x |
| >100% | 10.0x - 30.0x+ |

### Implied Valuation Formulas

```
EV/Revenue Method:
  Target Revenue × Median EV/Revenue = Implied EV
  Implied EV - Debt + Cash = Implied Equity Value

EV/EBITDA Method:
  Target EBITDA × Median EV/EBITDA = Implied EV
  Implied EV - Debt + Cash = Implied Equity Value

P/E Method:
  Target EPS × Median P/E = Implied Stock Price
  Implied Price × Shares = Implied Equity Value
```

---

## Sensitivity Analysis Templates

### Multiple Sensitivity

| Scenario | EV/Revenue | EV/EBITDA | Implied EV |
|----------|------------|-----------|------------|
| Bear (Low) | X.Xx | XX.Xx | $XXX M |
| Base (Median) | X.Xx | XX.Xx | $XXX M |
| Bull (High) | X.Xx | XX.Xx | $XXX M |

### EV/Revenue Sensitivity Matrix ($M)

| Revenue ↓ / Multiple → | 2.0x | 2.5x | 3.0x | 3.5x | 4.0x |
|------------------------|------|------|------|------|------|
| $80M | $160 | $200 | $240 | $280 | $320 |
| $100M | $200 | $250 | $300 | $350 | $400 |
| $120M | $240 | $300 | $360 | $420 | $480 |

---

## Data Validation Rules

### Financial Sanity Checks

```
<thinking>
1. Gross Profit < Revenue? (Must be true)
2. EBITDA < Gross Profit? (Usually true)
3. Net Income < EBITDA? (Usually true, unless one-time gains)
4. Market Cap = Price × Shares? (Verify)
5. Units consistent? (Check millions vs. thousands)
</thinking>
```

### Validation Checklist

- [ ] Numbers match between document sections
- [ ] Units are consistent (millions, thousands)
- [ ] Fiscal year end dates are correct
- [ ] EBITDA = Operating Income + D&A
- [ ] EPS = Net Income / Diluted Shares
- [ ] EV = Market Cap + Debt - Cash

---

## Output Formatting Standards

### Markdown Formatting

**Document Header:**
```markdown
# {Document Title}

**회사:** {Company Name}
**분석일:** {YYYY-MM-DD}
**분석가:** {Analyst Name}
**버전:** v1.0

---
```

**Numeric Tables** - Right-align numbers, include units:
```markdown
| Company | Revenue ($M) | EV/EBITDA (x) |
|:--------|-------------:|--------------:|
| Peer A  |       1,234.56 |          12.5 |
| **Mean** |  **1,111.11** |      **11.7** |
```

**Warnings:**
```markdown
> ⚠️ **주의:** [Warning message]
```

### CSV Formatting

**File Naming:**
```
{company}-{content}-{YYYY-MM-DD}.csv
```

**Column Headers:**
- Use snake_case: `revenue_m`, `ev_ebitda_x`
- Include unit suffix: `_m` (millions), `_pct` (percent), `_x` (multiple)

**Data Formatting:**
- Numbers: No commas, period for decimal
- Dates: YYYY-MM-DD
- Missing values: Leave blank or "N/A"

**Example:**
```csv
# Currency: USD (millions)
company,ticker,revenue_m,ev_m,ev_revenue_x
Target Co,XXXX,500.00,1250.00,2.50
Peer A,AAAA,750.00,2050.00,2.73
```

---

## Quick Reference Links

| Topic | Used In |
|-------|---------|
| Large Document Handling | Stage 1 (Target Analysis) |
| Financial Data Points | Stage 1, Stage 2 |
| Peer Selection Criteria | Stage 2 (Peer Selection) |
| Valuation Multiples | Stage 3 (Valuation) |
| Sensitivity Templates | Stage 3 (Valuation) |
| Data Validation | All stages |
| Output Formatting | Stage 4 (Output) |
