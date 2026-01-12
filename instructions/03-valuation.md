# Stage 3: Valuation Analysis

Calculate trading multiples and derive implied valuation for the target company.

**Previous:** [Peer Selection](02-peer-selection.md) | **Next:** [Output & Reports](04-output-reports.md) | **Main:** [Workflow Overview](analysis-workflow.md)

---

## Overview

This stage involves:
1. Calculating trading multiples from peer financial data
2. Applying multiples to derive target valuation
3. Performing sensitivity analysis

**Input:** Peer financial data from `output/{company}/02-peer-selection.md`
**Prompt Template:** `prompts/03-valuation-analysis.md`

---

## Quick Start

```bash
claude
> "Using prompts/03-valuation-analysis.md, calculate trading multiples and implied valuation for Nota"
```

---

## What You'll Learn

By completing this stage, you will understand:

1. **Which multiples to use** - EV/Revenue vs EV/EBITDA vs P/E
2. **How to calculate multiples** - From peer data
3. **How to apply multiples** - To derive target valuation
4. **How to adjust for differences** - Premium/discount rationale
5. **How to stress-test** - Sensitivity analysis

---

## Key Concepts

### Choosing the Right Multiple

| Target Status | Primary Multiple | Why |
|---------------|-----------------|-----|
| Pre-profit, high growth | EV/Revenue | EBITDA is negative |
| Pre-profit, low growth | EV/Revenue (low) | No earnings base |
| Profitable, growing | EV/EBITDA | Standard metric |
| Profitable, stable | P/E | Earnings are reliable |

> **Reference:** See [Valuation Multiples](shared-standards.md#valuation-multiples) for formulas and when to use each.

### The Valuation Process

```
Step 1: Calculate peer multiples
        ↓
Step 2: Find median/mean
        ↓
Step 3: Apply to target metrics
        ↓
Step 4: Adjust for premium/discount
        ↓
Step 5: Stress-test with sensitivity
```

---

## How to Think About Valuation

### From Multiples to Value

```
Target Revenue × Median EV/Revenue = Implied EV
Implied EV - Debt + Cash = Implied Equity Value
```

### Premium vs Discount

Compare target to peer median:

| Factor | Target vs Peers | Adjustment |
|--------|-----------------|------------|
| Growth Rate | Faster → Premium | +10-20% |
| Growth Rate | Slower → Discount | -10-20% |
| Profitability | Higher → Premium | +5-10% |
| Profitability | Lower → Discount | -5-10% |
| Risk Profile | Lower → Premium | +5-10% |
| Risk Profile | Higher → Discount | -5-10% |

---

## Common Mistakes

| Mistake | Why It's Bad | How to Avoid |
|---------|--------------|--------------|
| Using mean, not median | Outliers skew results | Always use median |
| Including negative EBITDA in EV/EBITDA | Meaningless multiple | Exclude or use EV/Revenue |
| Ignoring debt/cash | Equity ≠ Enterprise Value | Always bridge EV to equity |
| Single-point estimate | Appears precise, isn't | Use sensitivity range |
| No rationale for multiple | Seems arbitrary | Document premium/discount logic |

---

## Sensitivity Analysis

Don't present a single number. Show a range:

| Scenario | Multiple | Implied EV |
|----------|----------|------------|
| Bear (Low) | 2.0x | $XXX M |
| Base (Median) | 3.0x | $XXX M |
| Bull (High) | 4.0x | $XXX M |

> **Reference:** See [Sensitivity Analysis Templates](shared-standards.md#sensitivity-analysis-templates) for matrix formats.

---

## Blending Methods

When you have multiple valid approaches:

| Method | Weight | Rationale |
|--------|--------|-----------|
| EV/Revenue | 70% | "Pre-profit, high growth" |
| EV/EBITDA | 30% | "Turning profitable" |

```
Blended Value = (EV/Rev Value × 70%) + (EV/EBITDA Value × 30%)
```

---

## Output

Save to `output/{company-name}/03-valuation-analysis.md` and `03-comps-table.csv`

```markdown
# {Company Name} 밸류에이션 분석

**분석일:** YYYY-MM-DD

## 1. Trading Multiples 비교
| Company | Revenue ($M) | EV ($M) | EV/Revenue |
|---------|-------------|---------|------------|
| Peer 1  | ... | ... | ... |
| **Median** | | | **X.Xx** |

## 2. Target 밸류에이션
| Method | Target Metric | Multiple | Implied EV |
|--------|---------------|----------|------------|
| EV/Revenue | $XXX M | X.Xx | $XXX M |

## 3. 민감도 분석
[Sensitivity table]

## 4. 밸류에이션 범위
| Method | Low | Mid | High |
|--------|-----|-----|------|
| EV/Revenue | $XXX M | $XXX M | $XXX M |
| **Blended** | **$XXX M** | **$XXX M** | **$XXX M** |

## 5. 주요 가정
- [Assumption 1]
- [Assumption 2]
```

---

## Validation Checklist

- [ ] Multiples calculated correctly
- [ ] Negative EBITDA peers excluded from EV/EBITDA
- [ ] Median used (not mean)
- [ ] Premium/discount rationale documented
- [ ] Sensitivity analysis completed
- [ ] EV bridged to equity value

> **Reference:** See [Data Validation Rules](shared-standards.md#data-validation-rules) for calculation checks.

---

## Next Step

→ Proceed to [Output & Reports](04-output-reports.md)
