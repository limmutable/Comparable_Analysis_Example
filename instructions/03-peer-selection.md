# Stage 3: Peer Group Selection

Identify comparable companies for valuation benchmarking.

**Previous:** [Target Analysis](02-target-analysis.md) | **Next:** [Valuation Analysis](04-valuation.md) | **Main:** [Workflow Overview](analysis-workflow.md)

---

## Overview

Select 5-10 comparable public companies that can serve as valuation benchmarks for the target company.

**Prompt Template:** `prompts/02-peer-selection.md`

---

## Quick Start

```bash
claude
> "Using prompts/02-peer-selection.md, identify 5-7 comparable companies for a B2B SaaS company with $50M ARR in the cybersecurity space"
```

---

## Selection Process

### Step 1: Define Universe

Start with broad screening criteria:

| Filter | Criteria | Example |
|--------|----------|---------|
| Industry | GICS sub-industry or sector | "Application Software" |
| Geography | Primary market | "North America" |
| Revenue Range | 0.5× to 2× target | "$25M - $100M" |
| Listing Status | Public companies | NYSE, NASDAQ, KOSPI |

### Step 2: Apply Screening Filters

Narrow progressively:

| Step | Criteria | Companies | Notes |
|------|----------|-----------|-------|
| 1 | Industry: [sector] | 50 | Initial universe |
| 2 | Revenue: $X-$Y | 20 | Size filter |
| 3 | Business model: [type] | 12 | SaaS vs. perpetual |
| 4 | Geography: [region] | 10 | Primary market |
| 5 | Data availability | 8 | Exclude if no recent filings |

### Step 3: Qualitative Validation

Numbers alone aren't enough. Validate business similarity:

```
<thinking>
- Do they sell the same thing? (Feature overlap)
- Same customer base? (Enterprise vs SMB)
- Similar go-to-market? (Direct vs. channel)
- Comparable stage? (Growth vs. mature)
</thinking>
```

| Company | Feature Overlap | Customer Similarity | Stage |
|---------|-----------------|---------------------|-------|
| Peer A | High | High (Enterprise) | Growth |
| Peer B | Medium | High (SMB) | Mature |
| Peer C | Low | Medium | Growth |

### Step 4: Final Selection

| # | Company | Ticker | Revenue ($M) | Selection Rationale |
|---|---------|--------|--------------|---------------------|
| 1 | | | | Direct competitor, similar size |
| 2 | | | | Same vertical, adjacent product |
| 3 | | | | Similar business model |
| ... | | | | |

### Step 5: Document Exclusions

| Company | Ticker | Exclusion Reason |
|---------|--------|------------------|
| BigCorp Inc | BIG | Conglomerate, diversified revenue |
| LossCo | LOSS | Negative EBITDA distorts multiples |
| NewIPO | NEW | <1 year trading history |
| AcquiredCo | ACQ | Pending M&A, price distorted |

---

## Selection Criteria Reference

### Primary Criteria (Must Match)

| Criterion | Description | Weight |
|-----------|-------------|--------|
| **Industry** | Same GICS sub-industry or direct competitor | High |
| **Business Model** | Similar revenue model (SaaS, transactional) | High |
| **Revenue Stage** | Within 0.5× - 2.0× of target revenue | Medium |

### Secondary Criteria (Should Match)

| Criterion | Description | Weight |
|-----------|-------------|--------|
| **Growth Profile** | Similar revenue growth rate (±10%) | Medium |
| **Profitability** | Similar margin profile | Medium |
| **Geography** | Same primary market | Low |
| **Customer Base** | B2B vs B2C, enterprise vs SMB | Low |

### Red Flags (Consider Exclusion)

- Negative EBITDA → Exclude from EV/EBITDA comps
- Recent large M&A → Distorted financials
- Pending delisting → Price unreliable
- Revenue concentration >50% in different segment
- Regulatory overhang or major litigation

---

## Common Peer Sources

### By Industry

| Industry | Where to Find Peers |
|----------|---------------------|
| Tech/SaaS | Bessemer Cloud Index, SaaS Capital |
| Fintech | CB Insights Fintech 250 |
| Healthcare | Healthcare IT News, KLAS |
| Consumer | PitchBook, Crunchbase |
| Industrial | S&P Capital IQ, FactSet |

### Research Shortcuts

```bash
# Ask Claude for suggestions
> "Suggest 10 public company peers for [Target] based on: industry ([X]), revenue ($Y), business model ([Z])"

# Competitor analysis
> "Who are the main public competitors of [Target]? Include ticker symbols."

# Industry mapping
> "What GICS sub-industry does [Target] belong to? List major public companies in that category."
```

---

## Output Format

Save peer selection to `output/{company-name}/02-peer-selection.md`:

```markdown
# Peer Group 선정

**Target:** {Company Name}
**선정일:** YYYY-MM-DD

## 1. 스크리닝 기준

| 단계 | 기준 | 결과 | 비고 |
|------|------|------|------|
| 1 | 산업: [sector] | XX개 | 초기 유니버스 |
| 2 | 매출: $X-$Y | XX개 | 규모 필터 |
| 3 | 비즈니스 모델 | XX개 | [type] |
| 4 | 데이터 가용성 | XX개 | 최종 |

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

## 4. Peer Group 특성

- **산업:** [Industry]
- **평균 매출:** $XXX M
- **매출 범위:** $XX M - $XXX M
- **평균 성장률:** XX%
```

---

## Validation Checklist

Before proceeding to valuation:

- [ ] 5-10 peers selected
- [ ] All peers have recent public filings
- [ ] Selection rationale documented
- [ ] Exclusions documented with reasons
- [ ] No peers with negative EBITDA (or flagged for exclusion from EV/EBITDA)
- [ ] Industry alignment verified

---

## Next Step

→ Proceed to [Valuation Analysis](04-valuation.md)
