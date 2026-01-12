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

## Pre-flight Check

> **Reference:** See `instructions/shared-standards.md#large-document-handling` for detailed commands.

1. Check for pre-extracted files in `.working/{company}/`
2. If none exist, run: `uv run python scripts/check_document_size.py dataroom/{company}/{file}.pdf`
3. If **TOO LARGE**, extract pages first before reading

---

## Analysis Sections

### 1. 사업 개요 (Business Overview)

| Item | Description |
|------|-------------|
| **Industry** | Primary industry/sector classification |
| **Product/Service** | Core offerings and value proposition |
| **Revenue Model** | How the company generates revenue |
| **Target Market** | Customer segments and geographic focus |

### 2. 재무 현황 (Financial Snapshot)

<thinking>
Extract and validate:
- Gross Profit < Revenue? (Must be true)
- EBITDA < Gross Profit? (Usually true)
- For private companies, search for "Adjusted EBITDA" or "Non-GAAP" metrics
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

*For SaaS/subscription:*
| Metric | Value | Source |
|--------|-------|--------|
| ARR/MRR | | |
| Customer Count | | |
| ARPU | | |
| LTV/CAC | | |

*For transaction businesses:*
| Metric | Value | Source |
|--------|-------|--------|
| GMV/TPV | | |
| Take Rate | | |

### 4. 경쟁 우위 (Competitive Advantage)

- **Technology Edge:** Proprietary technology, patents, IP
- **Market Position:** Market share, brand recognition
- **Barriers to Entry:** Network effects, switching costs, scale

### 5. 경쟁사 (Competitors)

| Competitor | Description | Differentiation |
|------------|-------------|-----------------|
| | | |

### 6. 주요 리스크 및 기회 (Risks & Opportunities)

**Risks:**
-
-

**Opportunities:**
-
-

---

## Output

**Save to:** `output/{company-name}/01-target-summary.md`

```markdown
# {Company Name} 회사 요약

**분석일:** {YYYY-MM-DD}
**데이터 출처:** {Source files}

---

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
```

---

## Next Steps

→ Proceed to `02-peer-selection.md`
