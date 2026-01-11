# Financial Data Extraction (Utility Prompt)

**Type:** Reusable utility prompt - can be referenced by other prompts

**Base configuration:** See `prompts/_base.md` for role, language, data sources, and standards.

---

## Purpose

Extract standardized financial data for ANY company (target or peer). This utility provides consistent data extraction methodology across all analysis stages.

---

## Usage

This prompt can be invoked:

1. **Standalone** - For a single company
2. **In a loop** - For multiple companies in a peer group
3. **Referenced** - By other prompts (01-target-summary, 02-peer-selection)

```bash
# Single company
> "Using prompts/_extract-financials.md, extract financial data for CEVA Inc (CEVA)"

# Multiple companies
> "Using prompts/_extract-financials.md, extract financial data for: CEVA, SoundHound (SOUN), C3.ai (AI)"
```

---

## Input

| Parameter | Required | Example |
|-----------|----------|---------|
| Company name | Yes | "CEVA Inc" |
| Ticker | Recommended | "CEVA" |
| Source document | Optional | "dataroom/ceva/10-K-2024.pdf" |

---

## Data Sources (Priority Order)

### For Public Companies

1. **SEC Filings** (if in dataroom) - Most accurate
2. **Stock Analysis** (stockanalysis.com) - Comprehensive free data
3. **Yahoo Finance** (finance.yahoo.com) - Market data, key stats
4. **Company IR** (ir.[company].com) - Latest earnings

### Web Search Queries

```
# Revenue and financials
"[company] [ticker] revenue 2024 annual report"
"[company] [ticker] Q4 2024 earnings results"

# Market data
"[company] [ticker] market cap shares outstanding"
"[ticker] enterprise value debt cash"
```

---

## Required Data Points

### Income Statement (LTM)

| Metric | Definition | Unit |
|--------|------------|------|
| Revenue | Total net revenue/sales | $M |
| Gross Profit | Revenue - COGS | $M |
| EBITDA | Operating Income + D&A | $M |
| EBIT | Operating Income | $M |
| Net Income | Bottom line earnings | $M |

### Balance Sheet (MRQ)

| Metric | Definition | Unit |
|--------|------------|------|
| Cash | Cash & short-term investments | $M |
| Total Debt | Short + Long-term debt | $M |
| Shares Outstanding | Diluted shares | M |

### Market Data (Current)

| Metric | Definition | Unit |
|--------|------------|------|
| Stock Price | Latest closing price | $ |
| Market Cap | Price x Shares Outstanding | $M |
| Enterprise Value | Market Cap + Debt - Cash | $M |

---

## Output Format

```markdown
## {Company Name} ({Ticker})

**Data Date:** YYYY-MM-DD
**Fiscal Year End:** [Month]
**Currency:** USD

### Financial Summary

| Metric | Value | Source |
|--------|------:|--------|
| Revenue (LTM) | $XXX M | [Source] |
| EBITDA (LTM) | $XXX M | [Source] |
| Net Income (LTM) | $XXX M | [Source] |
| Cash | $XXX M | [Source] |
| Total Debt | $XXX M | [Source] |
| Market Cap | $X,XXX M | [Source] |
| Enterprise Value | $X,XXX M | [Calc: MCap + Debt - Cash] |

### Notes
- [Any data quality notes, e.g., "EBITDA negative, excluded from EV/EBITDA"]
- [Currency conversion if applicable]
```

---

## Validation Rules

<thinking>
Before finalizing data, verify:
1. Is EBITDA > Revenue? (Impossible - check units)
2. Is Net Income > EBITDA? (Unlikely unless one-time gain)
3. Does Market Cap ≈ Price × Shares?
4. Does EV = Market Cap + Debt - Cash?
5. Are units consistent? ($M vs $B vs $K)
</thinking>

---

## Special Cases

### Pre-Profit Companies

| Metric | Handling |
|--------|----------|
| Negative EBITDA | Record as negative, flag for EV/Revenue only |
| Negative Net Income | Record as negative, exclude from P/E |

### Currency Conversion

```
Non-USD → USD conversion:
- Use spot rate as of data date
- Document: "[Currency]/USD = [rate], [date]"
- Example: "KRW/USD = 1,300, 2026-01-12"
```

### Missing Data

| Situation | Action |
|-----------|--------|
| EBITDA not reported | Calculate: Operating Income + D&A |
| D&A not available | Check Cash Flow Statement |
| Metric unavailable | Mark as "N/A" |

---

## CSV Export Format

When exporting to CSV, use this structure:

```csv
company,ticker,revenue_m,ebitda_m,net_income_m,cash_m,debt_m,market_cap_m,ev_m,data_date,source
Company Name,TICK,100.0,15.0,10.0,50.0,20.0,500.0,470.0,2026-01-12,stockanalysis.com
```

Column naming convention:
- `_m` = millions USD
- `_pct` = percentage
- `_x` = multiple

---

## Example Output

```markdown
## SoundHound AI (SOUN)

**Data Date:** 2026-01-12
**Fiscal Year End:** December
**Currency:** USD

### Financial Summary

| Metric | Value | Source |
|--------|------:|--------|
| Revenue (LTM) | $84.7 M | Stock Analysis |
| EBITDA (LTM) | $(45.2) M | Stock Analysis |
| Net Income (LTM) | $(98.3) M | Stock Analysis |
| Cash | $200.0 M | Yahoo Finance |
| Total Debt | $0 M | Yahoo Finance |
| Market Cap | $4,720 M | Yahoo Finance |
| Enterprise Value | $4,520 M | [Calc: 4720 + 0 - 200] |

### Notes
- Pre-profit company: EBITDA and Net Income negative
- Use EV/Revenue only for valuation (exclude from EV/EBITDA)
- High market cap reflects AI sector premium
```
