# Peer Group Selection Prompt

**Base configuration:** See `prompts/_base.md` for role, language, data sources, and standards.

---

## Objective

Identify and document a defensible peer group of 5-10 comparable companies for valuation benchmarking.

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
| **Key Competitors (from summary)** | [List from 01-company-summary] |

---

## Research Methodology

### Primary Sources for Peer Discovery

1. **From Target Summary**: Check competitors listed in `output/{company}/01-company-summary.md`
2. **Web Search**: Search for "[industry] public companies stock ticker"
3. **Industry Reports**: Look for market reports mentioning key players
4. **ETF Holdings**: Check holdings of relevant sector ETFs

### Search Queries to Use

```
# Find public peers
"[industry] public companies stock ticker 2025"
"[competitor name] alternatives competitors public"
"small cap [industry] stocks revenue"

# Validate financials
"[company] [ticker] revenue 2024 market cap"
```

### Free Data Sources

| Source | URL | Data Available |
|--------|-----|----------------|
| Yahoo Finance | finance.yahoo.com | Price, financials, key stats |
| Stock Analysis | stockanalysis.com | Financials, metrics |
| Simply Wall St | simplywall.st | Peer comparisons |
| Finviz | finviz.com | Screener, charts |

---

## Selection Checklist

Before finalizing peer group:
- [ ] Target profile summarized
- [ ] Industry/sector alignment verified
- [ ] Business model similarity assessed
- [ ] Size comparability considered (0.25x - 4x revenue)
- [ ] Geographic relevance evaluated
- [ ] Data availability confirmed
- [ ] Exclusions documented with rationale

---

## Section: Peer Group 선정 (Peer Selection)

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

### Step 4: Final Peer Selection

| # | Company | Ticker:Exchange | Revenue ($M) | Market Cap ($M) | Growth | Selection Rationale |
|---|---------|-----------------|--------------|-----------------|--------|---------------------|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |

### Step 5: Exclusions

Document companies considered but excluded:

| Company | Ticker | Exclusion Reason |
|---------|--------|------------------|
| | | e.g., Acquired by larger company |
| | | e.g., Private / Not listed |
| | | e.g., Conglomerate with diversified revenue |
| | | e.g., Revenue scale too different (>10x) |
| | | e.g., Negative EBITDA distorts multiples |

---

## Handling Special Cases

### When Direct Competitors Are Private

Many emerging tech sectors have private competitors. Strategies:

1. **Look broader**: Expand to adjacent industries with similar business models
2. **Use larger public companies**: Include bigger players (with size adjustment notes)
3. **Geographic expansion**: Include international peers from similar markets
4. **Document the gap**: Note that direct comps are limited

Example: "Most AI model optimization companies (Deci AI, Neural Magic) have been acquired or remain private. Using broader AI software/Edge AI peers."

### For Early-Stage / Pre-Profit Companies

When target is pre-revenue or pre-profit:

1. **Revenue multiples only**: Use EV/Revenue, not EV/EBITDA
2. **Growth-adjusted**: Prioritize growth rate similarity over absolute size
3. **Include other pre-profit peers**: Don't force profitability match
4. **Consider private market comps**: Reference recent funding rounds as context

### For Non-US Companies (e.g., KOSDAQ)

1. **Include both local and global peers**: Mix of home market and international
2. **Note liquidity differences**: Smaller markets may have valuation discounts
3. **Currency alignment**: Note if revenue/valuation in different currencies

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
- Regulatory overhang or major litigation

---

## Output Format

Save to: `output/{company-name}/02-peer-selection.md`

```markdown
# Peer Group 선정 - {Company Name}

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

## 3. Qualitative Validation

| Company | Feature Overlap | Customer Similarity | Growth Stage |
|---------|-----------------|---------------------|--------------|
| | | | |

---

## 4. 최종 Peer Group

| # | 회사명 | 티커 | 매출 ($M) | 시총 ($M) | 성장률 | 선정 근거 |
|---|--------|------|-----------|-----------|--------|-----------|
| 1 | | | | | | |
...

---

## 5. 제외 기업

| 회사명 | 티커 | 제외 사유 |
|--------|------|-----------|
| | | |

---

## 6. Peer Group 특성 요약

- **산업:**
- **평균 매출:** $[X]M
- **매출 범위:** $[Min]M - $[Max]M
- **평균 성장률:** [X]%

---

**선정 기준일:** YYYY-MM-DD
**데이터 출처:** [Sources with URLs]
```

---

## Usage Example

```bash
claude
> "Using prompts/02-peer-selection.md, identify comparable companies for Nota based on output/nota/01-company-summary.md"
```

---

## Next Steps

After completing peer selection, proceed to:
- `03-data-extraction.md` - Extract financial data for all peers
- `04-valuation-analysis.md` - Calculate trading multiples
