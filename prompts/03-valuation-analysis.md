# Valuation Analysis Prompt

**Base configuration:** See `prompts/_base.md` for role, language, data sources, and standards.

---

## Objective

Calculate trading multiples for the peer group and derive an implied valuation range for the target company.

---

## Input Requirements

| Required | Source |
|----------|--------|
| Financial data | Output from `02-peer-selection.md` |
| Target company financials | From `01-target-summary.md` |
| Peer group list | Output from `02-peer-selection.md` |

---

## Method Selection

> **Reference:** See `instructions/shared-standards.md#valuation-multiples` for formulas and when to use each.

| Target Status | Primary Method | Avoid |
|---------------|----------------|-------|
| Pre-profit, high growth | EV/Revenue | EV/EBITDA, P/E |
| Early profitable | EV/Revenue + EV/EBITDA | P/E if volatile |
| Mature profitable | All methods | None |

---

## Step 1: Calculate Trading Multiples

### Enterprise Value Multiples

| Company | Revenue | EBITDA | EV | EV/Revenue | EV/EBITDA |
|---------|---------|--------|-----|------------|-----------|
| Peer 1 | | | | | |
| Peer 2 | | | | | |
| **Mean** | | | | | |
| **Median** | | | | | |
| **High** | | | | | |
| **Low** | | | | | |

### Equity Multiples (if profitable)

| Company | Net Income | EPS | Price | Market Cap | P/E | P/S |
|---------|------------|-----|-------|------------|-----|-----|
| Peer 1 | | | | | | |
| **Median** | | | | | | |

---

## Step 2: Apply Multiples to Target

```
EV/Revenue Method:
Target Revenue × Median EV/Revenue = Implied EV
Implied EV - Debt + Cash = Implied Equity Value

EV/EBITDA Method:
Target EBITDA × Median EV/EBITDA = Implied EV
Implied EV - Debt + Cash = Implied Equity Value
```

### Valuation Summary

| Method | Metric | Multiple (Median) | Target Value | Implied EV | Implied Equity |
|--------|--------|-------------------|--------------|------------|----------------|
| EV/Revenue | Revenue | x.xx | $XXX M | $XXX M | $XXX M |
| EV/EBITDA | EBITDA | x.xx | $XXX M | $XXX M | $XXX M |

---

## Step 3: Sensitivity Analysis

> **Reference:** See `instructions/shared-standards.md#sensitivity-analysis-templates` for matrix formats.

### Multiple Sensitivity Table

| EV/Revenue | 2.0x | 2.5x | 3.0x | 3.5x | 4.0x |
|------------|------|------|------|------|------|
| Revenue $100M | $200M | $250M | $300M | $350M | $400M |
| Revenue $150M | $300M | $375M | $450M | $525M | $600M |

---

## Step 4: Valuation Range Summary

| Method | Low | Mid (Median) | High |
|--------|-----|--------------|------|
| EV/Revenue | $XXX M | $XXX M | $XXX M |
| EV/EBITDA | $XXX M | $XXX M | $XXX M |
| **Blended Range** | **$XXX M** | **$XXX M** | **$XXX M** |

### Blended Valuation Weighting

| Method | Weight | Rationale |
|--------|--------|-----------|
| EV/Revenue | XX% | [e.g., "High-growth, EBITDA negative"] |
| EV/EBITDA | XX% | [e.g., "Standard for industry"] |

### Qualitative Justification

<thinking>
Compare Target to Median peer:
- If Target grows faster → Premium to Median
- If Target has lower margin → Discount to Median
</thinking>

**Adjustment Rationale:**
- Growth vs Peers: [Faster/Slower]
- Profitability vs Peers: [Higher/Lower]
- Selected Multiple: [Median or Adjusted Median]

---

## Output

**Save to:** `output/{company-name}/03-valuation-analysis.md`

```markdown
# {Company Name} 밸류에이션 분석

## 1. Trading Multiples 비교

| 회사 | 매출 ($M) | EBITDA ($M) | EV ($M) | EV/Revenue | EV/EBITDA |
|------|-----------|-------------|---------|------------|-----------|
| Peer 1 | | | | | |
| **중간값** | | | | **x.xx** | **x.xx** |

## 2. Target 밸류에이션

| 방법론 | 지표 | 적용 배수 | Target 값 | Implied EV | Implied Equity |
|--------|------|-----------|-----------|------------|----------------|
| EV/Revenue | 매출 | x.xx | $XXX M | $XXX M | $XXX M |

## 3. 민감도 분석

[Sensitivity tables]

## 4. 밸류에이션 범위 요약

| 방법론 | Low | Mid | High |
|--------|-----|-----|------|
| **Blended** | **$XXX M** | **$XXX M** | **$XXX M** |

## 5. 주요 가정 및 제한사항

- [Assumption 1]
- [Limitation 1]

---
**분석 기준일:** YYYY-MM-DD
```

---

## CSV Export

**Save to:** `output/{company-name}/03-comps-table.csv`

```csv
company,ticker,revenue_m,ebitda_m,ev_m,ev_revenue_x,ev_ebitda_x
Peer1,AAA,150,22,700,4.67,31.82
```

---

## Exclusion Rules

| Situation | Action |
|-----------|--------|
| Negative EBITDA | Exclude from EV/EBITDA, include in EV/Revenue |
| Negative Net Income | Exclude from P/E calculation |
| Outlier (>2x median) | Flag and calculate with/without |

---

## Next Steps

→ Proceed to `04-output-format.md`
