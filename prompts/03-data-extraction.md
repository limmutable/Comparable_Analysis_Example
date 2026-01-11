# Financial Data Extraction Prompt

**Base configuration:** See `prompts/_base.md` for role, language, data sources, and standards.

---

## Objective

Extract standardized financial data from source documents for the target company and all peer companies to enable comparable analysis.

---

## Input Requirements

| Required | Source |
|----------|--------|
| Company list | Output from `02-peer-selection.md` |
| Source documents | SEC filings, earnings reports in `/dataroom` |
| Market data | Stock prices, shares outstanding |

---

## Extraction Checklist

Before extracting data:
- [ ] Fiscal year end dates identified for each company
- [ ] Reporting currency noted
- [ ] LTM period defined (trailing 12 months)
- [ ] Source documents available for each company
- [ ] Market data source identified

---

## Section: 데이터 수집 (Data Collection)

### Required Data Points

#### Income Statement (손익계산서)

| Metric | Definition | Unit | Period |
|--------|------------|------|--------|
| Revenue | Total net revenue/sales | $M | LTM |
| COGS | Cost of goods sold | $M | LTM |
| Gross Profit | Revenue - COGS | $M | LTM |
| Operating Expenses | SG&A + R&D | $M | LTM |
| EBITDA | Operating Income + D&A | $M | LTM |
| EBIT | Operating Income | $M | LTM |
| Interest Expense | Total interest expense | $M | LTM |
| Net Income | Bottom line earnings | $M | LTM |
| EPS (Diluted) | Net Income / Diluted Shares | $ | LTM |

#### Balance Sheet (재무상태표)

| Metric | Definition | Unit | Period |
|--------|------------|------|--------|
| Cash & Equivalents | Cash + short-term investments | $M | MRQ |
| Total Debt | Short-term + Long-term debt | $M | MRQ |
| Total Assets | Total assets | $M | MRQ |
| Total Equity | Shareholders' equity | $M | MRQ |
| Shares Outstanding | Diluted shares | M | MRQ |

#### Market Data (시장 데이터)

| Metric | Definition | Unit | Period |
|--------|------------|------|--------|
| Stock Price | Closing price | $ | Current |
| Market Cap | Price × Shares Outstanding | $M | Current |
| Enterprise Value | Market Cap + Debt - Cash | $M | Calculated |

---

## Data Extraction Template

### Per-Company Data Sheet

```markdown
## {Company Name} ({Ticker})

**Fiscal Year End:** [Month]
**Reporting Currency:** [Currency]
**Data As Of:** [Date]
**Source:** [Filing type, date]

### Income Statement (LTM)

| Metric | Value ($M) | Source (Page/Section) |
|--------|------------|-----------------------|
| Revenue | | |
| Gross Profit | | |
| EBITDA | | |
| EBIT | | |
| Net Income | | |
| EPS (Diluted) | $ | |

### Balance Sheet (MRQ)

| Metric | Value ($M) | Source (Page/Section) |
|--------|------------|-----------------------|
| Cash | | |
| Total Debt | | |
| Total Assets | | |
| Total Equity | | |
| Shares Outstanding (M) | | |

### Market Data

| Metric | Value | Date | Source |
|--------|-------|------|--------|
| Stock Price | $ | | |
| Market Cap ($M) | | | |
| Enterprise Value ($M) | | | |

<thinking>
**Self-Correction Step:**
1. Check if EBITDA > Revenue (Impossible? check units)
2. Check if Net Income > EBITDA (Unlikely, unless big one-off gain)
3. Check if Market Cap = Price * Shares
</thinking>
```

---

## Consolidated Data Table

Output a single comparison table with all companies:

```markdown
# Peer Group 재무 데이터

| Company | Ticker | FYE | Revenue | EBITDA | EBIT | Net Income | EPS | Cash | Debt | Market Cap | EV |
|---------|--------|-----|---------|--------|------|------------|-----|------|------|------------|-----|
| Target Co | XXX | Dec | | | | | | | | | |
| Peer 1 | AAA | Dec | | | | | | | | | |
| Peer 2 | BBB | Mar | | | | | | | | | |
| ... | | | | | | | | | | | |

*All values in $M USD unless noted. LTM as of [date]. Market data as of [date].*
```

---

## Special Handling

### Currency Conversion
- Convert all non-USD financials to USD
- Use spot rate as of most recent quarter end
- Document FX rate used: `[Currency]/USD = [rate], [source], [date]`

### Fiscal Year Alignment
- For misaligned fiscal years, use LTM to standardize
- LTM = Q4 of prior FY + Q1-Q3 of current FY (for Dec FYE)
- Note any companies with non-standard fiscal years

### Missing Data Handling

| Situation | Action |
|-----------|--------|
| EBITDA not reported | Calculate: Operating Income + D&A |
| D&A not broken out | Use Cash Flow Statement D&A |
| Metric unavailable | Mark as "N/A" with footnote |
| Data inconsistency | Flag with ⚠️ and note discrepancy |

### Private Company Data

For private companies without public filings:
- Source from pitch deck, CIM, or management
- Flag as unaudited: `(unaudited)`
- Note estimation method if applicable
- Compare growth claims vs. industry benchmarks

---

## Validation Steps

After extraction, verify:

1. **Cross-check totals:** Revenue segments sum to total
2. **EBITDA calculation:** Operating Income + D&A = EBITDA
3. **EV calculation:** Market Cap + Debt - Cash = EV
4. **EPS check:** Net Income / Shares ≈ Reported EPS
5. **YoY reasonability:** Growth rates within expected range

---

## Output Formats

### Markdown Table
Save to: `output/{company}/financial-data.md`

### CSV Export
Save to: `output/{company}/financial-data.csv`

```csv
Company,Ticker,FYE,Revenue_M,EBITDA_M,EBIT_M,NetIncome_M,EPS,Cash_M,Debt_M,MarketCap_M,EV_M
TargetCo,XXX,Dec,1000,150,120,80,1.25,200,300,2500,2600
Peer1,AAA,Dec,1500,225,180,120,2.00,400,500,4000,4100
...
```

---

## Usage Example

```bash
claude
> "Using prompts/03-data-extraction.md, extract financial data for all companies in the peer group. Source documents are in dataroom/peer-companies/. Save consolidated data to output/peer-financials.csv"
```

---

## Next Steps

After completing data extraction, proceed to:
- `04-valuation-analysis.md` - Calculate trading multiples and implied valuation
