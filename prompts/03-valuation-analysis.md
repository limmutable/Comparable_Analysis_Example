# Valuation Analysis Prompt

**Base configuration:** See `prompts/_base.md` for role, language, data sources, and standards.

---

## Objective

Calculate trading multiples for the peer group and derive an implied valuation range for the target company.

---

## Input Requirements

| Required | Source |
|----------|--------|
| Financial data | Output from `02-peer-selection.md` (includes peer data) |
| Target company financials | From `01-target-summary.md` |
| Peer group list | Output from `02-peer-selection.md` |

---

## Pre-Profit Company Guidance

For companies with negative EBITDA/Net Income (like many AI/tech growth companies):

### Method Selection

| Target Status | Primary Method | Avoid |
|---------------|----------------|-------|
| Pre-profit, high growth | EV/Revenue | EV/EBITDA, P/E |
| Pre-profit, low growth | EV/Revenue (low multiple) | All profit-based |
| Early profitable | EV/Revenue + EV/EBITDA | P/E if volatile |
| Mature profitable | All methods | None |

### Growth-Adjusted Multiples

| Growth Rate | Typical EV/Revenue |
|-------------|-------------------|
| <10% | 1.0x - 3.0x |
| 10-30% | 2.0x - 5.0x |
| 30-50% | 4.0x - 8.0x |
| 50-100% | 6.0x - 15.0x |
| >100% | 10.0x - 30.0x+ |

### Outlier Handling

| Situation | Action |
|-----------|--------|
| EV/Revenue > 2x median | Flag as outlier, calculate median without |
| EV/Revenue < 0.5x median | Flag as potential value trap |
| Negative EBITDA peer | Include in EV/Revenue, exclude from EV/EBITDA |
| Single extreme outlier | Report both with/without |

---

## Analysis Checklist

Before calculating:
- [ ] All financial data standardized (currency, period)
- [ ] Negative values flagged for exclusion where appropriate
- [ ] Outliers identified for potential exclusion
- [ ] Calculation formulas documented
- [ ] Pre-profit status identified and appropriate method selected

---

## Section: 밸류에이션 분석 (Valuation Analysis)

### Step 1: Calculate Trading Multiples

#### Enterprise Value Multiples

| Company | Revenue | EBITDA | EBIT | EV | EV/Revenue | EV/EBITDA | EV/EBIT |
|---------|---------|--------|------|-----|------------|-----------|---------|
| Peer 1 | | | | | | | |
| Peer 2 | | | | | | | |
| ... | | | | | | | |
| **Mean** | | | | | | | |
| **Median** | | | | | | | |
| **High** | | | | | | | |
| **Low** | | | | | | | |

#### Equity Multiples

| Company | Net Income | EPS | Stock Price | Market Cap | P/E | P/S |
|---------|------------|-----|-------------|------------|-----|-----|
| Peer 1 | | | | | | |
| Peer 2 | | | | | | |
| ... | | | | | | |
| **Mean** | | | | | | |
| **Median** | | | | | | |
| **High** | | | | | | |
| **Low** | | | | | | |

### Step 2: Apply Multiples to Target

Calculate implied valuation using peer median multiples:

```
EV/Revenue Method:
Target Revenue × Median EV/Revenue = Implied EV
Implied EV - Debt + Cash = Implied Equity Value

EV/EBITDA Method:
Target EBITDA × Median EV/EBITDA = Implied EV
Implied EV - Debt + Cash = Implied Equity Value

P/E Method (if profitable):
Target EPS × Median P/E = Implied Stock Price
Implied Stock Price × Shares = Implied Equity Value
```

### Step 3: Valuation Summary Table

| Method | Metric | Multiple (Median) | Target Value | Implied EV | Implied Equity |
|--------|--------|-------------------|--------------|------------|----------------|
| EV/Revenue | Revenue | x.xx | $XXX M | $XXX M | $XXX M |
| EV/EBITDA | EBITDA | x.xx | $XXX M | $XXX M | $XXX M |
| P/E | EPS | x.xx | $X.XX | - | $XXX M |

---

## Sensitivity Analysis

### Scenario Matrix

Vary key assumptions to show valuation range:

| Scenario | Revenue Growth | EBITDA Margin | EV/Revenue | EV/EBITDA | Implied EV |
|----------|---------------|---------------|------------|-----------|------------|
| Bear | -10% | -2% | Low | Low | |
| Base | 0% | 0% | Median | Median | |
| Bull | +10% | +2% | High | High | |

### Multiple Sensitivity Table

| EV/Revenue | 2.0x | 2.5x | 3.0x | 3.5x | 4.0x |
|------------|------|------|------|------|------|
| Revenue $100M | $200M | $250M | $300M | $350M | $400M |
| Revenue $150M | $300M | $375M | $450M | $525M | $600M |
| Revenue $200M | $400M | $500M | $600M | $700M | $800M |

| EV/EBITDA | 8.0x | 10.0x | 12.0x | 14.0x | 16.0x |
|-----------|------|-------|-------|-------|-------|
| EBITDA $20M | $160M | $200M | $240M | $280M | $320M |
| EBITDA $30M | $240M | $300M | $360M | $420M | $480M |
| EBITDA $40M | $320M | $400M | $480M | $560M | $640M |

---

## Valuation Range Summary

| Method | Low | Mid (Median) | High |
|--------|-----|--------------|------|
| EV/Revenue | $XXX M | $XXX M | $XXX M |
| EV/EBITDA | $XXX M | $XXX M | $XXX M |
| P/E | $XXX M | $XXX M | $XXX M |
| **Blended Range** | **$XXX M** | **$XXX M** | **$XXX M** |

### Blended Valuation Weighting

| Method | Weight | Rationale |
|--------|--------|-----------|
| EV/Revenue | XX% | [Why? e.g., "High-growth, EBITDA negative"] |
| EV/EBITDA | XX% | [Why? e.g., "Standard for industry"] |
| P/E | XX% | [Why? e.g., "Stable profitability"] |

### Qualitative Justification (Why this range?)

<thinking>
Compare Target to the Median peer.
- If Target grows faster -> Should trade at Premium to Median.
- If Target has lower margin -> Should trade at Discount to Median.
- **Conclusion:** "Target warrants a [Premium/Discount] because..."
</thinking>

**Adjustment Rationale:**
- Growth vs Peers: [Faster/Slower]
- Profitability vs Peers: [Higher/Lower]
- Selected Multiple: [Median or Adjusted Median]

---

## Output Format

```markdown
# {Company Name} 밸류에이션 분석

## 1. Trading Multiples 비교

### Enterprise Value Multiples

| 회사 | 매출 ($M) | EBITDA ($M) | EV ($M) | EV/Revenue | EV/EBITDA |
|------|-----------|-------------|---------|------------|-----------|
| Peer 1 | | | | | |
| Peer 2 | | | | | |
...
| **평균** | | | | **x.xx** | **x.xx** |
| **중간값** | | | | **x.xx** | **x.xx** |
| **최고** | | | | x.xx | x.xx |
| **최저** | | | | x.xx | x.xx |

## 2. Target 밸류에이션

| 방법론 | 지표 | 적용 배수 | Target 값 | Implied EV | Implied Equity |
|--------|------|-----------|-----------|------------|----------------|
| EV/Revenue | 매출 | x.xx | $XXX M | $XXX M | $XXX M |
| EV/EBITDA | EBITDA | x.xx | $XXX M | $XXX M | $XXX M |
| P/E | EPS | x.xx | $X.XX | - | $XXX M |

## 3. 민감도 분석

[Sensitivity tables]

## 4. 밸류에이션 범위 요약

| 방법론 | Low | Mid | High |
|--------|-----|-----|------|
| EV/Revenue | $XXX M | $XXX M | $XXX M |
| EV/EBITDA | $XXX M | $XXX M | $XXX M |
| **Blended** | **$XXX M** | **$XXX M** | **$XXX M** |

## 5. 주요 가정 및 제한사항

- [Assumption 1]
- [Assumption 2]
- [Limitation 1]

---
**분석 기준일:** YYYY-MM-DD
**데이터 출처:** [Sources]
```

---

## Calculation Notes

### Exclusion Rules

| Situation | Action |
|-----------|--------|
| Negative EBITDA | Exclude from EV/EBITDA calculation |
| Negative Net Income | Exclude from P/E calculation |
| Outlier (>2 std dev) | Flag and consider exclusion |
| Recent IPO (<1 year) | Note limited trading history |

### Multiple Formatting

- Display multiples to 1 decimal place (e.g., 12.5x)
- Use "NM" (Not Meaningful) for negative or undefined multiples
- Show formulas for transparency

---

## Usage Example

```bash
claude
> "Using prompts/03-valuation-analysis.md, calculate trading multiples and implied valuation for {Target} using the financial data in output/{company}/02-peer-selection.md. Include sensitivity analysis."
```

---

## Next Steps

After completing valuation analysis, proceed to:
- `04-output-format.md` - Format final report and export files
