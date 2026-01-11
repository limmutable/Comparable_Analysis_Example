---
name: financial-analysis
description: Perform comparable company analysis, analyze financial statements, calculate valuation multiples, and identify peer group metrics. Use when analyzing SEC filings, comparing companies, or evaluating financial health.
allowed-tools: Read, Bash, Edit, Write, Glob, Grep, WebSearch, WebFetch
---

# Financial Analysis & Comparable Company Analysis

## Quick Reference

| Task | Approach |
|------|----------|
| Get peer financials | WebSearch "[company] [ticker] revenue 2024 market cap" |
| Check multiples | WebSearch "[industry] EV/Revenue multiple 2025" |
| Verify data | WebFetch from stockanalysis.com, Yahoo Finance |
| Calculate EV | Market Cap + Debt - Cash |

## Instructions

### 1. Data Collection Methodology

**Primary Sources (Web Search):**
```
"[company name] [ticker] revenue 2024 financial results"
"[company name] market cap enterprise value"
"[company name] Q4 2024 earnings"
```

**Free Data Sources:**

| Source | URL | Data Available |
|--------|-----|----------------|
| Stock Analysis | stockanalysis.com | Revenue, market cap, statistics |
| Yahoo Finance | finance.yahoo.com | Price, key stats, financials |
| Company IR | ir.[company].com | Earnings releases, 10-K/10-Q |
| SEC EDGAR | sec.gov/edgar | Official filings |

**Data Points to Collect:**

| Category | Metrics |
|----------|---------|
| Income Statement | Revenue, Gross Profit, EBITDA, Net Income |
| Balance Sheet | Cash, Total Debt, Shares Outstanding |
| Market Data | Stock Price, Market Cap |
| Calculated | Enterprise Value (Market Cap + Debt - Cash) |

### 2. Comparable Company Analysis

**Peer Selection:**
- Same industry/sector (GICS classification)
- Similar business model (SaaS, licensing, hardware, etc.)
- Revenue scale within 0.25x - 4x of target
- Document selection rationale for each peer

**Calculate Trading Multiples:**

| Multiple | Formula | Best For |
|----------|---------|----------|
| EV/Revenue | EV / LTM Revenue | Pre-profit companies |
| EV/EBITDA | EV / LTM EBITDA | Profitable companies |
| P/E | Price / EPS | Mature, profitable |
| P/S | Market Cap / Revenue | Growth companies |

**Multiple Statistics:**
- Calculate Mean, Median, High, Low
- Identify and flag outliers (>2 standard deviations)
- Use median for valuation (less sensitive to outliers)

### 3. Pre-Profit Company Valuation

For companies with negative EBITDA/Net Income:

1. **Use EV/Revenue only** - Do not calculate EV/EBITDA or P/E
2. **Growth-adjusted multiples** - Higher growth = higher multiple
3. **Peer selection** - Include other pre-profit peers
4. **Document assumptions** - Note that profitability is not yet proven

**Growth-Multiple Relationship:**

| Growth Rate | Typical EV/Revenue Range |
|-------------|--------------------------|
| <10% | 1.0x - 3.0x |
| 10-30% | 2.0x - 5.0x |
| 30-50% | 4.0x - 8.0x |
| 50-100% | 6.0x - 15.0x |
| >100% | 10.0x - 30.0x+ |

### 4. Outlier Handling

**Identification:**
- Multiple > 2x the median
- Multiple < 0.5x the median
- Extreme growth or decline situations

**Treatment Options:**

| Situation | Action |
|-----------|--------|
| Single outlier | Exclude from median calculation |
| Multiple outliers | Report both with/without outliers |
| All outliers high | Market may be pricing in growth |
| Negative EBITDA | Use "NM" (Not Meaningful) |

### 5. Sensitivity Analysis

**Required Tables:**

1. **Multiple Sensitivity:**
   - Vary EV/Revenue from Low to High
   - Show implied valuation at each level

2. **Revenue Sensitivity:**
   - Current year vs. forward year estimates
   - Show impact of growth scenarios

3. **Combined Matrix:**
   - Revenue (rows) x Multiple (columns)
   - Highlight base case

### 6. Financial Statement Analysis

**Profitability Metrics:**
- Gross margin, Operating margin, Net margin
- ROE, ROA, ROIC (for profitable companies)

**Liquidity Metrics:**
- Current ratio, Quick ratio
- Cash runway (Cash / Monthly Burn)

**Leverage Metrics:**
- Debt/Equity, Net Debt/EBITDA
- Interest coverage ratio

**Growth Metrics:**
- Revenue CAGR (3-year, 5-year)
- Organic vs. inorganic growth

### 7. Premium/Discount Adjustments

**Premium Factors:**
- Higher growth than peers
- Market leadership position
- Strong IP portfolio
- Blue-chip customer base

**Discount Factors:**
- Smaller market / lower liquidity
- Pre-profit status
- Customer concentration
- Regulatory risk

## Output Format

### Required Deliverables

1. **Financial Data Table** (`03-financial-data.md`)
   - Target company financials
   - All peer company data
   - Trading multiples with statistics

2. **Valuation Analysis** (`04-valuation-analysis.md`)
   - Multiple comparison table
   - Implied valuation calculation
   - Sensitivity analysis
   - Assumptions and limitations

3. **CSV Export** (optional)
   - `financial-data.csv` for spreadsheet analysis

### Table Formatting

```markdown
| Company | Ticker | Revenue ($M) | EV ($M) | EV/Revenue | Growth |
|---------|--------|--------------|---------|------------|--------|
| Peer 1 | XXX | 100 | 500 | 5.0x | +20% |
| **Mean** | | | | **5.0x** | |
| **Median** | | | | **4.5x** | |
```

### Source Citation

Always include data sources at the end:
```markdown
**데이터 출처:**
- [Source Name](URL)
- [Company IR](URL)
```

## Common Pitfalls

1. **Using stale data** - Always verify data currency
2. **Ignoring outliers** - Can skew mean significantly
3. **Applying EBITDA multiple to pre-profit** - Use revenue multiple instead
4. **Forgetting EV bridge** - EV = Market Cap + Debt - Cash
5. **Currency mismatch** - Convert all to same currency
