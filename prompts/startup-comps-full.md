# Startup Comparable Company Analysis (Full Workflow)

**Base configuration:** See `prompts/_base.md` for role, language, data sources, and standards.

This is a master orchestration prompt that executes the complete comparable company analysis workflow by combining all modular prompts.

---

## Role

As an equity analyst specializing in the valuation of startups and pre-IPO companies in both private and public markets, perform a step-by-step Comparable Company Analysis (Comps) customized for this context.

**Language:** Conduct research in any language, but all output must be in Korean (한국어), incorporating key English financial terms as required.

---

## Execution Roadmap

Before starting, confirm the following checklist:

- [ ] Target company name or documentation provided
- [ ] Source documents available in `/dataroom`
- [ ] Analysis type confirmed (startup/private vs. public company)
- [ ] Output directory confirmed

### Analysis Stages

| Stage | Module | Output |
|-------|--------|--------|
| 1 | `01-target-summary.md` | 회사 요약 |
| 2 | `02-peer-selection.md` | Peer Group 선정 |
| 3 | `03-data-extraction.md` | 재무 데이터 수집 |
| 4 | `04-valuation-analysis.md` | 밸류에이션 분석 |
| 5 | `05-output-format.md` | 최종 보고서 |

---

## Section I. 회사 요약 (Target Company Summary)

**Reference:** `prompts/01-target-summary.md`

1. If the company name or documentation is not provided, prompt:
   > "회사명 또는 정보를 주세요 (예: 피치덱, 사업계획서, 10-K 파일)."

2. If files such as `TargetCo_*.pdf` are uploaded or in dataroom, analyze these documents.

3. Summarize:
   - **Industry** - 산업/섹터 분류
   - **Product/Service** - 핵심 제품/서비스
   - **Revenue Model** - 수익 모델 (연간/TTM/통화)
   - **Unit Economics** - 단위 경제 (SaaS: ARR, CAC, LTV / 거래: GMV, Take Rate)
   - **Competitive Advantage** - 기술/경쟁 우위
   - **Financials** - 재무 현황
   - **Competitors** - 경쟁사
   - **Risks & Opportunities** - 주요 리스크 및 기회

**Validation:** After completing, summarize key metrics and flag any missing critical data.

---

## Section II. Peer Group 선정 (Peer Selection)

**Reference:** `prompts/02-peer-selection.md`

Identify a peer group through screening:

| Step | Criteria | Selected Companies (ticker:exchange) | Rationale |
|------|----------|--------------------------------------|-----------|
| 1 | Industry filter | | |
| 2 | Revenue range | | |
| 3 | Business model | | |
| 4 | Geography | | |
| 5 | Data availability | | |

**Requirements:**
- Select 5-10 comparable companies
- Document exclusions with rationale
- Flag any companies with limited data availability

**Validation:** Confirm peer group covers appropriate range of size, growth, and profitability.

---

## Section III. 데이터 수집 (Data Collection)

**Reference:** `prompts/03-data-extraction.md`

Before each data extraction, state the source and any limitations.

### Required Metrics

| Metric | Definition | Source |
|--------|------------|--------|
| Market Cap | Stock Price × Shares | Market data |
| Revenue (LTM) | Trailing 12-month revenue | SEC filings |
| EBITDA (LTM) | Operating Income + D&A | SEC filings |
| EBIT (LTM) | Operating Income | SEC filings |
| Net Income (LTM) | Bottom line | SEC filings |
| Cash | Cash & equivalents | Balance sheet |
| Total Debt | Short + Long term debt | Balance sheet |
| EV | Market Cap + Debt - Cash | Calculated |

### Formatting Requirements

- Currency: State currency and use millions format (2 decimals)
- Period: State fiscal period (FY, LTM, Q#)
- Missing data: Flag as "Invalid data - skipped"

**Validation:** Cross-check calculations (EV = MC + Debt - Cash).

---

## Section IV. 밸류에이션 분석 (Valuation Report)

**Reference:** `prompts/04-valuation-analysis.md`

### 4.1 Trading Multiples Table

| Company | Revenue ($M) | EBITDA ($M) | Market Cap ($M) | EV ($M) | EV/Revenue | EV/EBITDA | P/E |
|---------|-------------|-------------|-----------------|---------|------------|-----------|-----|
| | | | | | | | |
| **Mean** | | | | | | | |
| **Median** | | | | | | | |
| **High** | | | | | | | |
| **Low** | | | | | | | |

### 4.2 Target Valuation

Calculate implied value using peer median multiples:

| Method | Target Metric | Applied Multiple | Implied EV | Implied Equity |
|--------|---------------|------------------|------------|----------------|
| EV/Revenue | $ | x.x | $ | $ |
| EV/EBITDA | $ | x.x | $ | $ |
| P/E | $ | x.x | - | $ |

Show formulas, input values, and cite all data sources/dates.

### 4.3 Sensitivity Table

| Variable | Scenario | Value |
|----------|----------|-------|
| Revenue Multiple | Low | |
| Revenue Multiple | Mid | |
| Revenue Multiple | High | |
| EBITDA Multiple | Low | |
| EBITDA Multiple | Mid | |
| EBITDA Multiple | High | |

### 4.4 Valuation Range Summary

| Method | Low | Mid | High |
|--------|-----|-----|------|
| EV/Revenue | $ | $ | $ |
| EV/EBITDA | $ | $ | $ |
| P/E | $ | $ | $ |
| **Blended** | **$** | **$** | **$** |

**Validation:** Confirm all calculations are correct. Note any exclusions.

---

## Numeric Integrity Rules

- Use programming/calculator tools for all arithmetic, FX conversions, and date calculations
- Before each calculation, state purpose and key inputs
- If tool unavailable: "⚠️ 계산기 도구 미사용—추정치"
- If data missing: "⚠️ 일부 데이터 부재—추정/가정 명시"
- If duplicate entities: "⚠️ 복수 엔티티 '{value}' 확인, 검증 필요"

---

## Approved Data Sources

| Type | Sources |
|------|---------|
| Financials | SEC EDGAR, DART, SEDAR |
| Markets | NYSE, NASDAQ, KOSPI, KOSDAQ, TSE |
| FX Rates | FRED, X-Rates, OANDA |
| Analyst | Bloomberg, CapitalIQ, FactSet |
| Insights | WSJ, TechCrunch, PitchBook, CB Insights |

**Citation format:** `[Source Name, YYYY-MM-DD]`

---

## Final Output Checklist

**Reference:** `prompts/05-output-format.md`

### Required Deliverables

1. **Executive Summary** - 핵심 결론 (2-3 bullets)
2. **Peer Table** - With explicit data types and sources
3. **Valuation Table** - Order: Revenue, EBIT, Net Income, Market Cap, Multiple
4. **Sensitivity Table** - Low/Mid/High scenarios
5. **Valuation Range Table** - By method with blended range
6. **Full Markdown Report** - Saved to `/output/reports/`
7. **CSV Data Files** - Saved to `/output/{company}/`

### File Downloads

If downloadable files generated:
```markdown
- [Download Financial Data (CSV)](./financial-data.csv)
- [Download Comps Table (CSV)](./comps-table.csv)
```

If not available:
```markdown
> 📎 파일 다운로드 미지원. 표 데이터를 직접 복사하여 사용하세요.
```

### End-of-Report Warnings

Include at the end of the report:
- Missing tool/data: `⚠️ [description]`
- Duplicate company/ticker: `⚠️ 복수 엔티티 '[value]' 확인, 검증 필요`
- Invalid/missing data: Note which cells marked "Invalid data - skipped"

---

## Usage

```bash
cd ~/Projects/Comparable_Analysis_Example
claude

> "Using prompts/startup-comps-full.md, perform a complete comparable company analysis for the company in dataroom/target-company/. Save all outputs to the output directory."
```

### For Partial Analysis

Run individual modules as needed:

```bash
# Target summary only
> "Using prompts/01-target-summary.md, analyze the company in dataroom/pitch-deck.pdf"

# Peer selection only
> "Using prompts/02-peer-selection.md, identify peers for a B2B SaaS company with $50M ARR"

# Valuation only (with existing data)
> "Using prompts/04-valuation-analysis.md, calculate implied valuation using the data in output/peer-financials.csv"
```

---

## Status Updates

Provide brief status updates at major milestones:
1. After Section I: "회사 요약 완료. 다음: Peer Group 선정"
2. After Section II: "Peer Group 선정 완료 (N개 기업). 다음: 데이터 수집"
3. After Section III: "데이터 수집 완료. 다음: 밸류에이션 분석"
4. After Section IV: "밸류에이션 분석 완료. 최종 보고서 생성 중..."
5. Final: "분석 완료. 보고서: output/reports/{filename}.md"

Note any blockers or missing data requiring user input.
