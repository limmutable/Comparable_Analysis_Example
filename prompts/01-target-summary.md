# Target Company Summary Prompt

**Base configuration:** See `prompts/_base.md` for role, language, data sources, and standards.

---

## Objective

Analyze the target company's business model, financials, and competitive position to establish context for valuation analysis.

---

## Input Requirements

| Required | Description |
|----------|-------------|
| Company Name | Name or ticker of the target company |
| Source Documents | At least one of: pitch deck, 10-K, business plan, CIM |

**If missing:** Prompt user with "회사명 또는 정보를 주세요 (예: 피치덱, 사업계획서, 10-K)."

---

## Handling Large Documents

> ⚠️ If the document exceeds context limits, use page-range reading.

### For 10-K Filings (100-300 pages)

**Option 1: Chunked Reading**
```bash
# Step 1: Company overview
> "Read pages 1-25 of [file] and summarize the business"

# Step 2: Financial data
> "Read pages 45-55 of [file] and extract Selected Financial Data (Item 6)"

# Step 3: Full financials
> "Read pages 80-120 of [file] and extract financial statements (Item 8)"
```

**Option 2: Targeted Query**
```bash
> "In [file], find ONLY: Revenue, EBITDA, Net Income, Total Debt, Cash for FY2023.
   Search in Item 6 or Item 8."
```

### Key 10-K Sections

| Section | Pages | Priority |
|---------|-------|----------|
| Item 6: Selected Financial | 45-55 | ★★★ 5-year summary |
| Item 8: Financial Statements | 80-130 | ★★★ Full financials |
| Item 7: MD&A | 55-80 | ★★ Context |
| Item 1: Business | 6-25 | ★ Overview |

---

## Analysis Checklist

Before starting, confirm:
- [ ] Company name/ticker identified
- [ ] Source documents located in dataroom
- [ ] Document type identified (public filing vs. private materials)
- [ ] Fiscal year end / reporting period noted

---

## Section: 회사 요약 (Company Summary)

Analyze source documents and produce the following summary:

### 1. 사업 개요 (Business Overview)

| Item | Description |
|------|-------------|
| **Industry** | Primary industry/sector classification |
| **Product/Service** | Core offerings and value proposition |
| **Revenue Model** | How the company generates revenue |
| **Target Market** | Customer segments and geographic focus |

### 2. 재무 현황 (Financial Snapshot)
 
 <thinking>
 Extract the following metrics.
 **Validation Logic:**
 - check if Gross Profit < Revenue
 - check if EBITDA < Gross Profit (usually)
 - If Private Company: Search for "Adjusted EBITDA" or "Non-GAAP" metrics and note them clearly.
 </thinking>
 
 | Metric | Value | Period | Source (File, Page) |
 |--------|-------|--------|----------------------|
 | Revenue | $ | FY/TTM | |
 | Gross Profit | $ | FY/TTM | |
 | EBITDA | $ | FY/TTM | |
 | Net Income | $ | FY/TTM | |
 | Total Assets | $ | Period | |
 | Total Debt | $ | Period | |
 | Cash | $ | Period | |
 
 ### 3. 단위 경제 (Unit Economics)
 
 *For SaaS/subscription businesses:*
 | Metric | Value | Source |
 |--------|-------|--------|
 | ARR/MRR | | |
 | Customer Count | | |
 | ARPU | | |
 | CAC | | |
 | LTV | | |
 | LTV/CAC | | |
 
 *For transaction businesses:*
 | Metric | Value | Source |
 |--------|-------|--------|
 | GMV/TPV | | |
 | Take Rate | | |
 | Transaction Count | | |
 | Average Order Value | | |
 
 ### 4. 기술/경쟁 우위 (Competitive Advantage)
 
 - **Technology Edge:** Proprietary technology, patents, IP
 - **Market Position:** Market share, brand recognition
 - **Barriers to Entry:** Network effects, switching costs, scale
 
 ### 5. 경쟁사 (Competitors)
 
 <thinking>
 Scan for "Competition" or "Peers" section in the documents.
 If direct competitors are not listed, infer from industry reports or "Market" section.
 </thinking>
 
 | Competitor | Description | Differentiation |
 |------------|-------------|-----------------|
 | | | |
 | | | |
 | | | |
 
 ### 6. 주요 리스크 및 기회 (Risks & Opportunities)
 
 **Risks:**
 -
 -
 -
 
 **Opportunities:**
 -
 -
 -

---

## Output Format

```markdown
# {Company Name} 회사 요약

## 1. 사업 개요
[Summary paragraph]

| 구분 | 내용 |
|------|------|
| 산업 | |
| 제품/서비스 | |
| 수익 모델 | |
| 타겟 시장 | |

## 2. 재무 현황
[Financial snapshot table]

## 3. 단위 경제
[Unit economics table if applicable]

## 4. 경쟁 우위
[Bullet points]

## 5. 경쟁사
[Competitor table]

## 6. 리스크 및 기회
[Bullet points]

---
**데이터 출처:** [Source, Date]
**분석 기준일:** YYYY-MM-DD
```

---

## Usage Example

```bash
claude
> "Using the prompt template in prompts/01-target-summary.md, analyze the company in dataroom/target-company/pitch-deck.pdf"
```

---

## Next Steps

After completing target summary, proceed to:
- `02-peer-selection.md` - Select comparable companies
- `03-data-extraction.md` - Extract detailed financial data
