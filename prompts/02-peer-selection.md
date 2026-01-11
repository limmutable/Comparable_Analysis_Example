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

## Selection Checklist

Before finalizing peer group:
- [ ] Industry/sector alignment verified
- [ ] Business model similarity assessed
- [ ] Size comparability considered (revenue, market cap)
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
| Revenue Range | [Min - Max] | |
| Listing Status | [Public/Private/Both] | |

### Step 2: Screening Criteria

Apply sequential filters to narrow the universe:

| Step | Criteria | Companies Remaining | Notes |
|------|----------|---------------------|-------|
| 1 | Industry: [specific sector] | | |
| 2 | Revenue: $[X]M - $[Y]M | | |
| 3 | Business Model: [type] | | |
| 4 | Geography: [regions] | | |
| 5 | Data Availability | | |

### Step 3: Qualitative Validation (New)

<thinking>
Just numbers are not enough. Check business quality.
- Do they sell the same thing? (Feature overlap)
- do they have similar customer base? (Enterprise vs SMB)
</thinking>

| Company | Feature Overlap (High/Med/Low) | Customer Base Similarity |
|---------|--------------------------------|--------------------------|
| Peer A | High | Medium (They target SMBs) |
| Peer B | Low | High |

### Step 4: Final Peer Selection

| # | Company | Ticker:Exchange | Revenue ($M) | Selection Rationale |
|---|---------|-----------------|--------------|---------------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |
| 7 | | | | |

### Step 5: Exclusions

Document companies considered but excluded:

| Company | Ticker | Exclusion Reason |
|---------|--------|------------------|
| | | e.g., Conglomerate with diversified revenue |
| | | e.g., Negative EBITDA distorts multiples |
| | | e.g., Recent M&A activity |
| | | e.g., Insufficient public data |

---

## Selection Criteria Reference

### Primary Criteria (Must Match)

| Criterion | Description | Weight |
|-----------|-------------|--------|
| **Industry** | Same GICS sub-industry or direct competitor | High |
| **Business Model** | Similar revenue model (SaaS, transactional, etc.) | High |
| **Revenue Stage** | Within 0.5x - 2.0x of target revenue | Medium |

### Secondary Criteria (Should Match)

| Criterion | Description | Weight |
|-----------|-------------|--------|
| **Growth Profile** | Similar revenue growth rate (±10%) | Medium |
| **Profitability** | Similar margin profile | Medium |
| **Geography** | Same primary market | Low |
| **Customer Base** | B2B vs B2C, enterprise vs SMB | Low |

### Red Flags (Consider Exclusion)

- Negative EBITDA (exclude from EV/EBITDA comps)
- Recent large M&A (distorted financials)
- Pending delisting or restructuring
- Revenue concentration >50% in different segment
- Regulatory overhang or litigation

---

## Output Format

```markdown
# Peer Group 선정

## 1. 스크리닝 기준

| 단계 | 기준 | 선정 기업 (ticker:exchange) | 근거 |
|------|------|----------------------------|------|
| 1 | 산업: [sector] | [companies] | |
| 2 | 매출: $[X]M - $[Y]M | [companies] | |
| 3 | 비즈니스 모델: [type] | [companies] | |
| 4 | 지역: [regions] | [companies] | |
| 5 | 데이터 가용성 | [companies] | |

## 2. 최종 Peer Group

| # | 회사명 | 티커 | 매출 ($M) | 선정 근거 |
|---|--------|------|-----------|-----------|
| 1 | | | | |
| 2 | | | | |
...

## 3. 제외 기업

| 회사명 | 티커 | 제외 사유 |
|--------|------|-----------|
| | | |

## 4. Peer Group 특성 요약

- **산업:**
- **평균 매출:** $[X]M
- **매출 범위:** $[Min]M - $[Max]M
- **평균 성장률:** [X]%
- **지역 분포:**

---
**선정 기준일:** YYYY-MM-DD
**데이터 출처:** [Sources]
```

---

## Usage Example

```bash
claude
> "Using prompts/02-peer-selection.md, identify comparable companies for {Target Company} based on the summary in output/target/company-summary.md"
```

---

## Next Steps

After completing peer selection, proceed to:
- `03-data-extraction.md` - Extract financial data for all peers
- `04-valuation-analysis.md` - Calculate trading multiples
