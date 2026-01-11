# Stage 1: Target Company Analysis

Analyze and extract financial data from the target company.

**Previous:** [Dataroom Setup](00-dataroom-setup.md) | **Next:** [Peer Selection](02-peer-selection.md) | **Main:** [Workflow Overview](analysis-workflow.md)

---

## Overview

This stage extracts key financial metrics and business context from the target company's source documents.

**Prompt Template:** `prompts/01-target-summary.md`

---

## Quick Start

```bash
claude
> "Using prompts/01-target-summary.md, analyze the company in dataroom/target-company/10-K-2024.pdf"
```

---

## Handling Large Documents

> **Token Limit Warning:** Full 10-K filings (100-300 pages) often exceed LLM context windows. Use the strategies below.

### Step 1: Check Document Size

```bash
# Check all files in dataroom
uv run python scripts/check_document_size.py dataroom/

# Check specific directory
uv run python scripts/check_document_size.py dataroom/target-company/
```

If a file shows "TOO LARGE", use one of these strategies:

### Strategy A: Page-Range Reading (Recommended)

Read specific sections instead of the full document:

```bash
# Quick company overview (low tokens)
> "Read pages 1-10 of dataroom/nota/nota-sec.pdf and summarize the company"

# Financial summary - Item 6 (medium tokens)
> "Read pages 45-55 of the 10-K and extract the Selected Financial Data table"

# Full financials - Item 8 (chunk if needed)
> "Read pages 80-100 of the 10-K and extract the Income Statement and Balance Sheet"
> "Read pages 100-120 and extract the Cash Flow Statement"
```

### Strategy B: Section-by-Section Analysis

Break into multiple requests:

| Request | Pages | Content |
|---------|-------|---------|
| 1 | 1-25 | Business overview (Item 1) |
| 2 | 45-55 | Selected Financial Data (Item 6) |
| 3 | 80-100 | Income Statement, Balance Sheet |
| 4 | 100-120 | Cash Flow, Notes |

### Strategy C: Pre-Extract with Scripts (Recommended for Large Files)

```bash
# Extract financial statement pages to text
uv run python scripts/extract_sections.py dataroom/nota/nota-sec.pdf --pages 80-120 --output .working/nota/financials.txt

# Then analyze the smaller extracted file
claude
> "Read .working/nota/financials.txt and extract key metrics"
```

### Strategy D: Targeted Queries

Ask for specific data points:

```bash
> "In dataroom/nota/nota-sec.pdf, find and extract ONLY:
   - Total Revenue for FY2023 and FY2022
   - Net Income for FY2023 and FY2022
   - Total Assets and Total Debt as of year-end
   Look in Item 6 (Selected Financial Data) or Item 8 (Financial Statements)"
```

### 10-K Section Reference

| Section | Typical Pages | Content |
|---------|---------------|---------|
| Cover & TOC | 1-5 | Basic info, table of contents |
| Item 1: Business | 6-25 | Business description |
| Item 1A: Risk Factors | 25-45 | Risk disclosures |
| Item 6: Selected Financial | 45-55 | 5-year financial summary |
| Item 7: MD&A | 55-80 | Management discussion |
| Item 8: Financials | 80-130 | Full financial statements |

### Script Reference

```bash
# Check all files in dataroom
uv run python scripts/check_document_size.py dataroom/

# View 10-K section guide
uv run python scripts/extract_sections.py --guide

# View chunking strategies
uv run python scripts/extract_sections.py --strategies

# Get PDF page count
uv run python scripts/extract_sections.py dataroom/nota/nota-sec.pdf --info

# Extract specific pages
uv run python scripts/extract_sections.py dataroom/nota/nota-sec.pdf --pages 80-120 --output .working/nota/financials.txt
```

---

## Key Data Points to Extract

### From Income Statement

| Metric | Description | Source Section |
|--------|-------------|----------------|
| Revenue | Total net sales | Income Statement |
| COGS | Cost of goods sold | Income Statement |
| Gross Profit | Revenue - COGS | Income Statement |
| Operating Expenses | SG&A + R&D | Income Statement |
| EBIT | Operating Income | Income Statement |
| EBITDA | EBIT + D&A | Calculated |
| Net Income | Bottom line | Income Statement |
| EPS (Diluted) | Net Income / Diluted Shares | Income Statement |

### From Balance Sheet

| Metric | Description | Source Section |
|--------|-------------|----------------|
| Cash & Equivalents | Cash + short-term investments | Balance Sheet |
| Total Assets | All assets | Balance Sheet |
| Total Debt | Short-term + Long-term debt | Balance Sheet / Notes |
| Shareholders' Equity | Total equity | Balance Sheet |
| Shares Outstanding | Diluted share count | Cover page / Notes |

### From Cash Flow Statement

| Metric | Description | Source Section |
|--------|-------------|----------------|
| Operating Cash Flow | Cash from operations | Cash Flow Statement |
| CapEx | Capital expenditures | Cash Flow Statement |
| Free Cash Flow | OCF - CapEx | Calculated |
| D&A | Depreciation & Amortization | Cash Flow Statement |

---

## Using Claude to Parse Documents

### Public Company (10-K)

```bash
# Full extraction
> "Read dataroom/target-company/10-K-2024.pdf and extract key financial metrics for the most recent fiscal year. Include Revenue, EBITDA, Net Income, Total Debt, Cash, and Shares Outstanding."

# Multi-year extraction
> "From the 10-K, extract Revenue, EBITDA, and Net Income for the last 3 fiscal years. Create a table showing year-over-year growth rates."

# Specific section
> "Read the Management Discussion & Analysis section and summarize key business drivers and risks."
```

### Private Company (Pitch Deck / Financials)

```bash
# Pitch deck analysis
> "Read dataroom/target-company/presentations/intro-deck-2024.pdf. Summarize the business model, key customers, revenue, and any financial milestones mentioned."

# Unaudited financials
> "Read dataroom/target-company/financials/unaudited-2023.xlsx. Extract the historical P&L and reformat into a standard Income Statement. Flag any unusual line items (e.g., owner expenses)."

# Validate projections
> "Compare management projections in dataroom/target-company/financials/projections.xlsx with historical growth rates. Flag any aggressive assumptions."
```

---

## Unit Economics (SaaS / Transaction Businesses)

### SaaS / Subscription

| Metric | Formula | What to Look For |
|--------|---------|------------------|
| ARR | MRR x 12 | Growth rate |
| ARPU | ARR / Customers | Expansion vs. contraction |
| CAC | S&M Spend / New Customers | Efficiency |
| LTV | ARPU x Gross Margin x Lifetime | Rule of thumb: >3x CAC |
| LTV/CAC | LTV / CAC | Target: 3-5x |
| Payback | CAC / (ARPU x Gross Margin) | Target: <18 months |

### Transaction / Marketplace

| Metric | Formula | What to Look For |
|--------|---------|------------------|
| GMV/TPV | Total transaction value | Volume growth |
| Take Rate | Revenue / GMV | Monetization |
| AOV | GMV / Transactions | Basket size |

---

## Data Validation

### Self-Correction Checks

Use these validation rules (built into `prompts/01-target-summary.md`):

```
<thinking>
1. Gross Profit < Revenue? (Must be true)
2. EBITDA < Gross Profit? (Usually true)
3. Net Income < EBITDA? (Usually true, unless one-time gains)
4. Market Cap = Price x Shares? (Verify)
5. Units consistent? (Check millions vs. thousands)
</thinking>
```

### Validation Checklist

- [ ] Numbers match between document sections
- [ ] Units are consistent (millions, thousands)
- [ ] Fiscal year end dates are correct
- [ ] EBITDA = Operating Income + D&A
- [ ] EPS = Net Income / Diluted Shares

---

## Output Format

Save extracted data to `output/{company-name}/01-target-summary.md`:

```markdown
# {Company Name} 회사 요약

**분석일:** YYYY-MM-DD
**데이터 출처:** [Source file, date]

## 1. 사업 개요

| 구분 | 내용 |
|------|------|
| 산업 | [Industry] |
| 제품/서비스 | [Products] |
| 수익 모델 | [Revenue model] |
| 타겟 시장 | [Target market] |

## 2. 재무 현황

| Metric | Value | Period | Source |
|--------|-------|--------|--------|
| Revenue | $XXX M | FY2024 | [10-K, p.XX] |
| EBITDA | $XXX M | FY2024 | [Calc: EBIT + D&A] |
| Net Income | $XXX M | FY2024 | [10-K, p.XX] |
| Cash | $XXX M | Q4 2024 | [10-K, p.XX] |
| Total Debt | $XXX M | Q4 2024 | [10-K, p.XX] |

## 3. 주요 리스크
- [Risk 1]
- [Risk 2]
```

---

## Next Step

Proceed to [Peer Selection](03-peer-selection.md)
