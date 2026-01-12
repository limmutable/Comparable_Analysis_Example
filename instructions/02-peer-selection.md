# Stage 2: Peer Group Selection

Identify comparable companies for valuation benchmarking.

**Previous:** [Target Analysis](01-target-analysis.md) | **Next:** [Valuation Analysis](03-valuation.md) | **Main:** [Workflow Overview](analysis-workflow.md)

---

## Overview

Select 5-10 comparable public companies that can serve as valuation benchmarks for the target company.

**Prompt Template:** `prompts/02-peer-selection.md`

---

## Quick Start

```bash
claude
> "Using prompts/02-peer-selection.md, identify comparable companies for Nota based on output/nota/01-target-summary.md"
```

---

## What You'll Learn

By completing this stage, you will understand:

1. **How to think about comparability** - Industry, size, business model
2. **How to screen peers** - Progressive filtering approach
3. **How to validate selections** - Qualitative checks beyond numbers
4. **How to extract peer data** - Financial metrics for each peer

---

## Key Concepts

### What Makes a Good Peer?

Good peers are companies that:
- **Trade publicly** (so we have market valuations)
- **Operate similarly** (same industry, business model)
- **Are comparable size** (0.25x to 4x revenue of target)
- **Have available data** (recent filings)

### The Screening Funnel

```
Industry Universe (50+ companies)
       ↓ Size filter
Revenue Range (20 companies)
       ↓ Business model
Similar Operations (12 companies)
       ↓ Data availability
Final Peer Group (5-10 companies)
```

> **Reference:** See [Peer Selection Criteria](shared-standards.md#peer-selection-criteria) for detailed criteria and weights.

---

## How to Think About Peer Matching

Ask these questions for each candidate:

| Question | What You're Checking |
|----------|---------------------|
| Do they sell the same thing? | Feature/product overlap |
| To the same customers? | Enterprise vs SMB, B2B vs B2C |
| In the same way? | Direct sales vs channel |
| At similar scale? | Revenue, growth stage |

### Qualitative Validation

Numbers alone aren't enough. Create a qualitative assessment:

| Company | Feature Overlap | Customer Similarity | Stage |
|---------|-----------------|---------------------|-------|
| Peer A | High | High | Growth |
| Peer B | Medium | High | Mature |
| Peer C | Low | Medium | Growth |

---

## Common Mistakes

| Mistake | Why It's Bad | How to Avoid |
|---------|--------------|--------------|
| Too few peers (<5) | Statistically unreliable | Expand search criteria |
| Too many peers (>10) | Dilutes comparability | Tighten criteria |
| Size mismatch (10x+) | Different economics | Use 0.25x-4x rule |
| Including acquirees | Distorted prices | Check for M&A activity |
| Negative EBITDA in all | Can't use EV/EBITDA | Flag for EV/Revenue only |

> **Reference:** See [Red Flags](shared-standards.md#red-flags-consider-exclusion) for exclusion criteria.

---

## Data Sources

### Free Sources

| Source | URL | Best For |
|--------|-----|----------|
| Yahoo Finance | finance.yahoo.com | Price, basic stats |
| Stock Analysis | stockanalysis.com | Detailed financials |
| SEC EDGAR | sec.gov/edgar | 10-K, 10-Q filings |
| Finviz | finviz.com | Screening, charts |

### Search Queries

```
# Find public peers
"[industry] public companies stock ticker 2026"
"[competitor] alternatives competitors public"

# Validate financials
"[company] [ticker] revenue 2024 market cap"
```

---

## Special Cases

| Situation | What to Do |
|-----------|------------|
| Direct competitors are private | Expand to adjacent industries |
| Target is pre-profit | Use pre-profit peers, EV/Revenue only |
| Non-US company (e.g., KOSDAQ) | Mix local and global peers |

> **Reference:** See [Special Cases](shared-standards.md#special-cases) for detailed guidance.

---

## Output

Save to `output/{company-name}/02-peer-selection.md` and `02-peer-data.csv`

```markdown
# Peer Group 선정

**Target:** {Company Name}
**선정일:** YYYY-MM-DD

## 1. 스크리닝 기준
| 단계 | 기준 | 결과 | 비고 |
|------|------|------|------|
| 1 | 산업 | XX개 | 초기 유니버스 |
| 2 | 매출 규모 | XX개 | $X-$Y M |
| 3 | 비즈니스 모델 | XX개 | [type] |
| 4 | 데이터 가용성 | XX개 | 최종 |

## 2. 최종 Peer Group
| # | 회사명 | 티커 | 매출 ($M) | 시총 ($M) | 선정 근거 |
|---|--------|------|-----------|-----------|-----------|
| 1 | ... | ... | ... | ... | ... |

## 3. 제외 기업
| 회사명 | 티커 | 제외 사유 |
|--------|------|-----------|
| ... | ... | ... |
```

---

## Validation Checklist

- [ ] 5-10 peers selected
- [ ] All have recent public filings
- [ ] Industry/sector alignment verified
- [ ] Size comparability (0.25x-4x revenue)
- [ ] Selection rationale documented
- [ ] Exclusions documented with reasons

---

## Next Step

→ Proceed to [Valuation Analysis](03-valuation.md)
