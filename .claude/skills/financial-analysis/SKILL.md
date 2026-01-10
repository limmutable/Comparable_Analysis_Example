---
name: financial-analysis
description: Perform comparable company analysis, analyze financial statements, calculate valuation multiples, and identify peer group metrics. Use when analyzing SEC filings, comparing companies, or evaluating financial health.
allowed-tools: Read, Bash, Edit, Write, Glob, Grep
---

# Financial Analysis & Comparable Company Analysis

## Instructions

### Comparable Company Analysis

1. **Peer Selection**
   - Identify companies in same industry/sector
   - Consider size (market cap, revenue), geography, business model
   - Document selection rationale

2. **Data Collection**
   - Gather from SEC filings (10-K, 10-Q), earnings releases
   - Key metrics: Revenue, EBITDA, Net Income, EPS
   - Market data: Stock price, shares outstanding, market cap

3. **Calculate Trading Multiples**
   - EV/Revenue, EV/EBITDA, EV/EBIT
   - P/E, P/B, P/S
   - Use LTM (Last Twelve Months) and NTM (Next Twelve Months)

4. **Spread Comps**
   - Create comparison table with all peers
   - Show mean, median, high, low for each multiple
   - Highlight where target company falls in range

### Financial Statement Analysis

1. **Profitability**
   - Gross margin, Operating margin, Net margin
   - ROE, ROA, ROIC

2. **Liquidity**
   - Current ratio, Quick ratio
   - Days Sales Outstanding, Days Inventory, Days Payable

3. **Leverage**
   - Debt/Equity, Debt/EBITDA
   - Interest coverage ratio

4. **Growth**
   - Revenue CAGR, EPS growth
   - Organic vs inorganic growth

## Output Format

- Present comps in structured Markdown tables
- Include footnotes for data sources and adjustments
- Export to CSV for spreadsheet analysis
- Save analysis to `/output` directory
