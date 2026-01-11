# Stage 4: Valuation Analysis

Calculate trading multiples and derive implied valuation for the target company.

**Previous:** [Peer Selection](03-peer-selection.md) | **Next:** [Output & Reports](05-output-reports.md) | **Main:** [Workflow Overview](analysis-workflow.md)

---

## Overview

This stage involves:
1. Extracting financial data for all peer companies
2. Calculating trading multiples
3. Applying multiples to derive target valuation
4. Performing sensitivity analysis

**Prompt Templates:**
- `prompts/03-data-extraction.md` - Extract peer financials
- `prompts/04-valuation-analysis.md` - Calculate multiples and valuation

---

## Quick Start

```bash
claude
# Use the financial-analysis skill for comprehensive valuation
> "Use the financial-analysis skill to perform valuation analysis for Nota using the peer group from output/nota/02-peer-selection.md"

# Or step by step:
# Extract peer data
> "Using prompts/03-data-extraction.md, extract financial data for all companies in the peer group"

# Run valuation
> "Using prompts/04-valuation-analysis.md, calculate trading multiples and implied valuation for the target"
```

---

## Data Collection Methodology

### Web Search for Peer Financials

For each peer company, use these search queries:

```
"[company name] [ticker] revenue 2024 financial results"
"[company name] market cap enterprise value"
"[company name] Q4 2024 earnings"
```

### Free Data Sources

| Source | URL | Best For |
|--------|-----|----------|
| Stock Analysis | stockanalysis.com | Revenue, market cap, multiples |
| Yahoo Finance | finance.yahoo.com | Current price, key statistics |
| Company IR | ir.[company].com | Latest earnings releases |
| Simply Wall St | simplywall.st | Peer comparisons |

### Pre-Profit Company Handling

For companies with negative EBITDA (common in AI/tech):

| Target Status | Use | Avoid |
|---------------|-----|-------|
| Pre-profit, high growth | EV/Revenue | EV/EBITDA, P/E |
| Pre-profit, low growth | EV/Revenue (low multiple) | All profit-based |
| Profitable | All methods | None |

**Growth-Multiple Relationship:**

| Growth Rate | Typical EV/Revenue |
|-------------|-------------------|
| <10% | 1.0x - 3.0x |
| 10-30% | 2.0x - 5.0x |
| 30-50% | 4.0x - 8.0x |
| 50-100% | 6.0x - 15.0x |
| >100% | 10.0x - 30.0x+ |

---

## Step 1: Extract Peer Financial Data

### Required Metrics

| Metric | Definition | Source |
|--------|------------|--------|
| Revenue (LTM) | Trailing 12-month revenue | Income Statement |
| EBITDA (LTM) | Operating Income + D&A | Calculated |
| EBIT (LTM) | Operating Income | Income Statement |
| Net Income (LTM) | Bottom line earnings | Income Statement |
| Cash | Cash & equivalents | Balance Sheet |
| Total Debt | Short + Long term debt | Balance Sheet |
| Market Cap | Price × Shares | Market data |
| Enterprise Value | Market Cap + Debt - Cash | Calculated |

### Data Extraction Template

```bash
> "For each peer company, extract and create a table with:
   - Revenue (LTM)
   - EBITDA (LTM)
   - Net Income (LTM)
   - Cash
   - Total Debt
   - Market Cap
   - Calculate Enterprise Value
   Include source citations [File, Page] for each metric."
```

### Self-Correction Checks

```
<thinking>
1. Is EBITDA > Revenue? (Impossible - check units)
2. Is Net Income > EBITDA? (Unlikely unless one-time gain)
3. Does Market Cap = Price × Shares?
4. Does EV = Market Cap + Debt - Cash?
</thinking>
```

---

## Step 2: Calculate Trading Multiples

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

### Comps Table Format

| Company | Revenue ($M) | EBITDA ($M) | Market Cap ($M) | EV ($M) | EV/Rev | EV/EBITDA | P/E |
|---------|-------------|-------------|-----------------|---------|--------|-----------|-----|
| Peer 1  | | | | | | | |
| Peer 2  | | | | | | | |
| ...     | | | | | | | |
| **Mean** | | | | | **X.Xx** | **XX.Xx** | **XX.Xx** |
| **Median** | | | | | **X.Xx** | **XX.Xx** | **XX.Xx** |
| **High** | | | | | X.Xx | XX.Xx | XX.Xx |
| **Low** | | | | | X.Xx | XX.Xx | XX.Xx |

---

## Step 3: Apply Multiples to Target

### Implied Valuation Calculation

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

### Valuation Summary Table

| Method | Target Metric | Multiple (Median) | Implied EV ($M) | Implied Equity ($M) |
|--------|---------------|-------------------|-----------------|---------------------|
| EV/Revenue | Revenue: $XXX | X.Xx | $XXX | $XXX |
| EV/EBITDA | EBITDA: $XXX | XX.Xx | $XXX | $XXX |
| P/E | EPS: $X.XX | XX.Xx | - | $XXX |

---

## Step 4: Qualitative Adjustment

### Premium/Discount Analysis

```
<thinking>
Compare Target to Median peer:
- If Target grows FASTER → Should trade at PREMIUM to median
- If Target has LOWER margins → Should trade at DISCOUNT to median
- If Target has HIGHER risk → Should trade at DISCOUNT to median

Conclusion: Target warrants a [Premium/Discount] because...
</thinking>
```

### Adjustment Rationale

| Factor | Target vs Peers | Adjustment |
|--------|-----------------|------------|
| Growth Rate | Faster / Slower / Similar | +/- X% |
| Profitability | Higher / Lower / Similar | +/- X% |
| Market Position | Leader / Challenger | +/- X% |
| Risk Profile | Lower / Higher | +/- X% |

**Selected Multiple:** [Median / Adjusted Median]
**Rationale:** [Why]

---

## Step 5: Sensitivity Analysis

### Multiple Sensitivity

| Scenario | EV/Revenue | EV/EBITDA | Implied EV |
|----------|------------|-----------|------------|
| Bear (Low) | X.Xx | XX.Xx | $XXX M |
| Base (Median) | X.Xx | XX.Xx | $XXX M |
| Bull (High) | X.Xx | XX.Xx | $XXX M |

### Revenue/EBITDA Sensitivity Matrix

**EV/Revenue Sensitivity ($M)**

| Revenue ↓ / Multiple → | 2.0x | 2.5x | 3.0x | 3.5x | 4.0x |
|------------------------|------|------|------|------|------|
| $80M | $160 | $200 | $240 | $280 | $320 |
| $100M | $200 | $250 | $300 | $350 | $400 |
| $120M | $240 | $300 | $360 | $420 | $480 |

---

## Step 6: Valuation Range Summary

| Method | Low | Mid | High |
|--------|-----|-----|------|
| EV/Revenue | $XXX M | $XXX M | $XXX M |
| EV/EBITDA | $XXX M | $XXX M | $XXX M |
| P/E | $XXX M | $XXX M | $XXX M |
| **Blended** | **$XXX M** | **$XXX M** | **$XXX M** |

### Blending Weights

| Method | Weight | Rationale |
|--------|--------|-----------|
| EV/Revenue | XX% | [e.g., "High-growth, EBITDA negative"] |
| EV/EBITDA | XX% | [e.g., "Standard for profitable SaaS"] |
| P/E | XX% | [e.g., "Stable profitability"] |

---

## Output Format

Save valuation analysis to `output/{company-name}/04-valuation-analysis.md`:

```markdown
# {Company Name} 밸류에이션 분석

**분석일:** YYYY-MM-DD

## 1. Trading Multiples 비교

[Comps table]

## 2. Target 밸류에이션

[Valuation calculation table]

## 3. 민감도 분석

[Sensitivity tables]

## 4. 밸류에이션 범위

| 방법론 | Low | Mid | High |
|--------|-----|-----|------|
| EV/Revenue | $XXX M | $XXX M | $XXX M |
| EV/EBITDA | $XXX M | $XXX M | $XXX M |
| **Blended** | **$XXX M** | **$XXX M** | **$XXX M** |

## 5. 주요 가정

- [Assumption 1]
- [Assumption 2]
```

Also export data to `output/{company-name}/04-comps-table.csv`.

---

## Validation Checklist

- [ ] All peer data extracted with sources
- [ ] Multiples calculated correctly
- [ ] Negative EBITDA peers excluded from EV/EBITDA
- [ ] Target valuation calculated using multiple methods
- [ ] Sensitivity analysis completed
- [ ] Premium/discount rationale documented

---

## Next Step

→ Proceed to [Output & Reports](05-output-reports.md)
