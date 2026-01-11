# Peer Group Selection & Financial Data Prompt

**Base configuration:** See `prompts/_base.md` for role, language, data sources, and standards.

---

## Objective

Identify a defensible peer group of 5-10 comparable companies AND extract standardized financial data for valuation analysis.

**This prompt combines two tasks:**
1. **Peer Selection** - Identify comparable public companies
2. **Data Extraction** - Gather financial metrics for comps table

**Utility Reference:** Use `prompts/_extract-financials.md` for per-company data extraction methodology.

---

## Input Requirements

| Required | Source |
|----------|--------|
| Target company summary | Output from `01-target-summary.md` |
| Industry classification | From target summary |
| Revenue range | Target company financials |
| Business model | From target summary |

---

## Step 0: Target Profile Summary

Before searching for peers, summarize the target:

| Attribute | Value |
|-----------|-------|
| **Industry** | [e.g., AI Software / Edge AI] |
| **Business Model** | [e.g., B2B Platform Licensing] |
| **Revenue (Latest FY)** | $[X]M |
| **Revenue Growth** | [X]% YoY |
| **Profitability** | [Profitable / Pre-profit] |
| **Target Customers** | [e.g., Semiconductor, Enterprise] |
| **Key Competitors (from summary)** | [List from 01-target-summary] |

---

## Part 1: Peer Selection

### Research Methodology

#### Primary Sources for Peer Discovery

1. **From Target Summary**: Check competitors listed in `output/{company}/01-target-summary.md`
2. **Web Search**: Search for "[industry] public companies stock ticker"
3. **Industry Reports**: Look for market reports mentioning key players
4. **ETF Holdings**: Check holdings of relevant sector ETFs

#### Search Queries to Use

```
# Find public peers
"[industry] public companies stock ticker 2026"
"[competitor name] alternatives competitors public"
"small cap [industry] stocks revenue"

# Validate financials
"[company] [ticker] revenue 2024 market cap"
```

#### Free Data Sources

| Source | URL | Data Available |
|--------|-----|----------------|
| Stock Analysis | stockanalysis.com | Revenue, market cap, financials |
| Yahoo Finance | finance.yahoo.com | Price, key stats, financials |
| Simply Wall St | simplywall.st | Peer comparisons |
| Finviz | finviz.com | Screener, charts |
| SEC EDGAR | sec.gov/edgar | Official filings |

---

### Step 1: Initial Universe

Define the screening universe:

| Filter | Criteria | Rationale |
|--------|----------|-----------|
| Industry | [GICS/SIC code or description] | |
| Geography | [Regions/countries] | |
| Revenue Range | [0.25x - 4x target revenue] | |
| Listing Status | Public (required for trading comps) | |

### Step 2: Screening Criteria

Apply sequential filters to narrow the universe:

| Step | Criteria | Companies Remaining | Notes |
|------|----------|---------------------|-------|
| 1 | Industry: [specific sector] | | |
| 2 | Revenue: $[X]M - $[Y]M | | |
| 3 | Business Model: [type] | | |
| 4 | Geography: [regions] | | |
| 5 | Data Availability | | |

### Step 3: Qualitative Validation

<thinking>
Numbers alone are not enough. Validate business similarity:
- Do they sell the same thing? (Feature overlap)
- Same customer base? (Enterprise vs SMB)
- Similar go-to-market? (Direct vs channel)
- Comparable growth stage? (Early vs mature)
</thinking>

| Company | Feature Overlap | Customer Similarity | Growth Stage |
|---------|-----------------|---------------------|--------------|
| Peer A | High/Med/Low | High/Med/Low | High-growth/Mature |
| Peer B | High/Med/Low | High/Med/Low | High-growth/Mature |

### Step 4: Document Exclusions

| Company | Ticker | Exclusion Reason |
|---------|--------|------------------|
| | | e.g., Acquired by larger company |
| | | e.g., Private / Not listed |
| | | e.g., Conglomerate with diversified revenue |

---

## Part 2: Financial Data Extraction

**For each selected peer, extract financial data using the methodology in `prompts/_extract-financials.md`.**

### Required Metrics

#### Per Company

| Metric | Definition | Unit | Period |
|--------|------------|------|--------|
| Revenue | Total net revenue/sales | $M | LTM |
| EBITDA | Operating Income + D&A | $M | LTM |
| Net Income | Bottom line earnings | $M | LTM |
| Cash | Cash & equivalents | $M | MRQ |
| Total Debt | Short + Long-term debt | $M | MRQ |
| Market Cap | Price × Shares | $M | Current |
| Enterprise Value | MCap + Debt - Cash | $M | Calculated |

### Data Collection Process

For each peer company:

1. **Search** for latest financial data
2. **Extract** metrics using `_extract-financials.md` format
3. **Validate** using self-correction checks
4. **Document** sources

### Validation Rules

<thinking>
For each company, verify:
1. Is EBITDA > Revenue? (Impossible - check units)
2. Is Net Income > EBITDA? (Unlikely unless one-time gain)
3. Does EV = Market Cap + Debt - Cash?
4. Are growth rates reasonable for the industry?
</thinking>

---

## Handling Special Cases

### When Direct Competitors Are Private

Many emerging tech sectors have private competitors. Strategies:

1. **Look broader**: Expand to adjacent industries with similar business models
2. **Use larger public companies**: Include bigger players (with size adjustment notes)
3. **Geographic expansion**: Include international peers from similar markets
4. **Document the gap**: Note that direct comps are limited

### For Pre-Profit Companies

| Metric | Handling |
|--------|----------|
| Negative EBITDA | Record value, flag "NM" for EV/EBITDA multiple |
| Negative Net Income | Record value, exclude from P/E calculation |

### Currency Conversion

- Convert all non-USD to USD
- Document: "[Currency]/USD = [rate], [date]"

---

## Selection Criteria Reference

### Primary Criteria (Must Match)

| Criterion | Description | Weight |
|-----------|-------------|--------|
| **Industry** | Same GICS sub-industry or direct competitor | High |
| **Business Model** | Similar revenue model (SaaS, licensing, etc.) | High |
| **Revenue Stage** | Within 0.25x - 4.0x of target revenue | Medium |

### Secondary Criteria (Should Match)

| Criterion | Description | Weight |
|-----------|-------------|--------|
| **Growth Profile** | Similar revenue growth rate (±20%) | Medium |
| **Profitability** | Similar margin profile | Medium |
| **Geography** | Same primary market | Low |
| **Customer Base** | B2B vs B2C, enterprise vs SMB | Low |

### Red Flags (Consider Exclusion)

- Negative EBITDA (exclude from EV/EBITDA comps, keep for EV/Revenue)
- Recent large M&A (distorted financials)
- Pending delisting or restructuring
- Revenue concentration >50% in different segment

---

## Output Format

Save to: `output/{company-name}/02-peer-selection.md`

```markdown
# Peer Group 선정 및 재무 데이터 - {Company Name}

**Target:** {Company Name}
**선정일:** YYYY-MM-DD
**데이터 출처:** [Sources]

---

## 1. Target 기업 프로필

| 항목 | 내용 |
|------|------|
| **산업** | |
| **비즈니스 모델** | |
| **FY매출** | $[X]M |
| **성장률** | [X]% |

---

## 2. 스크리닝 기준

| 단계 | 기준 | 결과 | 비고 |
|------|------|------|------|
| 1 | 산업: [sector] | XX개 | |
| 2 | 매출: $[X]M - $[Y]M | XX개 | |
| 3 | 비즈니스 모델 | XX개 | |
| 4 | 데이터 가용성 | XX개 | 최종 |

---

## 3. 최종 Peer Group 및 재무 데이터

| # | Company | Ticker | Revenue ($M) | EBITDA ($M) | Cash ($M) | Debt ($M) | MCap ($M) | EV ($M) | Growth |
|---|---------|--------|-------------:|------------:|----------:|----------:|----------:|--------:|-------:|
| 0 | **Target** | XXX | | | | | | | |
| 1 | Peer 1 | AAA | | | | | | | |
| 2 | Peer 2 | BBB | | | | | | | |
| ... | | | | | | | | | |

---

## 4. Peer Group 특성 요약

| Metric | Mean | Median | Min | Max |
|--------|------|--------|-----|-----|
| Revenue ($M) | | | | |
| Growth (%) | | | | |
| Market Cap ($M) | | | | |

---

## 5. 제외 기업

| 회사명 | 티커 | 제외 사유 |
|--------|------|-----------|
| | | |

---

## 6. 데이터 출처

| Company | Primary Source | Date |
|---------|----------------|------|
| | | |

---

**선정 기준일:** YYYY-MM-DD
```

---

## CSV Export

Also save to: `output/{company-name}/02-peer-data.csv`

```csv
company,ticker,revenue_m,ebitda_m,net_income_m,cash_m,debt_m,market_cap_m,ev_m,growth_pct,source
Target,XXX,100,15,10,50,20,500,470,25,10-K
Peer1,AAA,150,22,15,80,30,750,700,18,stockanalysis.com
```

---

## Validation Checklist

Before proceeding to valuation:
- [ ] 5-10 peers selected with rationale
- [ ] All peers have financial data extracted
- [ ] EV calculated correctly for each company
- [ ] Pre-profit companies flagged
- [ ] Sources documented
- [ ] CSV exported

---

## Usage Example

```bash
claude
> "Using prompts/02-peer-selection.md, identify comparable companies for Nota and extract their financial data. Save to output/nota/02-peer-selection.md and export CSV."
```

---

## Next Steps

After completing peer selection and data extraction, proceed to:
- `03-valuation-analysis.md` - Calculate trading multiples and implied valuation
