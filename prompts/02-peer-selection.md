# Peer Group Selection & Financial Data Prompt

**Base configuration:** See `prompts/_base.md` for role, language, data sources, and standards.

---

## Objective

Identify a defensible peer group of 5-10 comparable companies AND extract standardized financial data for valuation analysis.

**Utility Reference:** Use `prompts/_extract-financials.md` for per-company data extraction methodology.

---

## Input Requirements

| Required | Source |
|----------|--------|
| Target company summary | Output from `01-target-summary.md` |
| Industry classification | From target summary |
| Revenue range | Target company financials |

---

## Step 0: Target Profile Summary

| Attribute | Value |
|-----------|-------|
| **Industry** | [e.g., AI Software / Edge AI] |
| **Business Model** | [e.g., B2B Platform Licensing] |
| **Revenue (Latest FY)** | $[X]M |
| **Revenue Growth** | [X]% YoY |
| **Profitability** | [Profitable / Pre-profit] |
| **Key Competitors (from summary)** | [List from 01-target-summary] |

---

## Part 1: Peer Selection

> **Reference:** See `instructions/shared-standards.md#peer-selection-criteria` for detailed criteria and red flags.

### Step 1: Define Screening Universe

| Filter | Criteria | Rationale |
|--------|----------|-----------|
| Industry | [GICS/SIC code or description] | |
| Revenue Range | [0.25x - 4x target revenue] | |
| Listing Status | Public (required for trading comps) | |

### Step 2: Apply Screening Criteria

| Step | Criteria | Companies Remaining | Notes |
|------|----------|---------------------|-------|
| 1 | Industry: [specific sector] | | |
| 2 | Revenue: $[X]M - $[Y]M | | |
| 3 | Business Model: [type] | | |
| 4 | Data Availability | | |

### Step 3: Qualitative Validation

<thinking>
Validate business similarity beyond numbers:
- Same products/services? (Feature overlap)
- Same customers? (Enterprise vs SMB)
- Similar go-to-market? (Direct vs channel)
- Comparable growth stage?
</thinking>

| Company | Feature Overlap | Customer Similarity | Growth Stage |
|---------|-----------------|---------------------|--------------|
| Peer A | High/Med/Low | High/Med/Low | High-growth/Mature |

### Step 4: Document Exclusions

| Company | Ticker | Exclusion Reason |
|---------|--------|------------------|
| | | e.g., Acquired, Private, Diversified revenue |

---

## Part 2: Financial Data Extraction

**For each peer, extract using `prompts/_extract-financials.md`.**

### Required Metrics

| Metric | Definition | Unit | Period |
|--------|------------|------|--------|
| Revenue | Total net revenue/sales | $M | LTM |
| EBITDA | Operating Income + D&A | $M | LTM |
| Net Income | Bottom line earnings | $M | LTM |
| Cash | Cash & equivalents | $M | MRQ |
| Total Debt | Short + Long-term debt | $M | MRQ |
| Market Cap | Price × Shares | $M | Current |
| Enterprise Value | MCap + Debt - Cash | $M | Calculated |

### Validation Rules

<thinking>
For each company, verify:
1. EBITDA > Revenue? (Impossible - check units)
2. Net Income > EBITDA? (Unlikely unless one-time gain)
3. EV = Market Cap + Debt - Cash? (Must be true)
</thinking>

---

## Output

**Save to:** `output/{company-name}/02-peer-selection.md`

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

---

## 4. Peer Group 특성 요약

| Metric | Mean | Median | Min | Max |
|--------|------|--------|-----|-----|
| Revenue ($M) | | | | |
| Growth (%) | | | | |

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
```

---

## CSV Export

**Save to:** `output/{company-name}/02-peer-data.csv`

```csv
company,ticker,revenue_m,ebitda_m,cash_m,debt_m,market_cap_m,ev_m,growth_pct,source
Target,XXX,100,15,50,20,500,470,25,10-K
Peer1,AAA,150,22,80,30,750,700,18,stockanalysis.com
```

---

## Validation Checklist

- [ ] 5-10 peers selected with rationale
- [ ] All peers have financial data extracted
- [ ] EV calculated correctly for each company
- [ ] Pre-profit companies flagged
- [ ] Sources documented
- [ ] CSV exported

---

## Next Steps

→ Proceed to `03-valuation-analysis.md`
