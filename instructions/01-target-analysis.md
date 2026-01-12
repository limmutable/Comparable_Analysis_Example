# Stage 1: Target Company Analysis

Analyze and extract financial data from the target company.

**Previous:** [Dataroom Setup](00-dataroom-setup.md) | **Next:** [Peer Selection](02-peer-selection.md) | **Main:** [Workflow Overview](analysis-workflow.md)

---

## Overview

This stage extracts key financial metrics and business context from the target company's source documents.

**Prompt Template:** `prompts/01-target-summary.md`

---

## Quick Start

```bash
claude
> "Using prompts/01-target-summary.md, analyze the company in dataroom/target-company/10-K-2024.pdf"
```

---

## What You'll Learn

By completing this stage, you will understand:

1. **How to handle large documents** - 10-K filings can be 300+ pages
2. **What data to extract** - Revenue, EBITDA, Net Income, etc.
3. **How to validate data** - Sanity checks to catch errors
4. **How to structure output** - Standard format for next stages

---

## Key Concepts

### Document Types

| Source | Typical Use | Data Quality |
|--------|-------------|--------------|
| 10-K (Annual Report) | Public companies | Audited, reliable |
| 10-Q (Quarterly) | Public companies | Reviewed, recent |
| Pitch Deck | Private companies | Unaudited, verify |
| Financial Statements | Private companies | May need normalization |

### What to Extract

Focus on these categories:

1. **Business Overview** - Industry, products, revenue model
2. **Financial Metrics** - Revenue, EBITDA, Net Income, Cash, Debt
3. **Unit Economics** - For SaaS: ARR, CAC, LTV; For transactions: GMV, Take Rate
4. **Risks & Opportunities** - Key factors affecting valuation

> **Reference:** See [Financial Data Points](shared-standards.md#financial-data-points) for detailed metric definitions.

---

## Handling Large Documents

Most 10-K filings exceed LLM context limits. Use these strategies:

| Strategy | When to Use | Effort |
|----------|-------------|--------|
| Page-range reading | Know which pages you need | Low |
| Pre-extract with scripts | Large files, multiple reads | Medium |
| Section-by-section | Deep analysis needed | High |

> **Reference:** See [Large Document Handling](shared-standards.md#large-document-handling) for detailed commands.

### Quick Example

```bash
# Check if file is too large
uv run python scripts/check_document_size.py dataroom/company/10-K.pdf

# If TOO LARGE, extract specific pages
uv run python scripts/extract_sections.py dataroom/company/10-K.pdf --pages 80-120 --output .working/company/financials.txt
```

---

## Common Mistakes

| Mistake | Why It Happens | How to Avoid |
|---------|----------------|--------------|
| Reading entire 10-K | Token limit exceeded | Check size first, use page ranges |
| Wrong fiscal year | Mixed up FY vs calendar | Verify fiscal year end date |
| Missing EBITDA | Not calculated | EBITDA = EBIT + D&A |
| Units mismatch | Millions vs thousands | Check column headers carefully |

---

## Validation

Before moving to Stage 2, verify:

- [ ] All key metrics extracted with sources
- [ ] Units are consistent (all in millions or all in thousands)
- [ ] Fiscal period is clearly noted
- [ ] Business overview is complete

> **Reference:** See [Data Validation Rules](shared-standards.md#data-validation-rules) for sanity checks.

---

## Output

Save to `output/{company-name}/01-target-summary.md`

```markdown
# {Company Name} 회사 요약

**분석일:** YYYY-MM-DD
**데이터 출처:** [Source file]

## 1. 사업 개요
[Industry, products, revenue model, target market]

## 2. 재무 현황
| Metric | Value | Period | Source |
|--------|-------|--------|--------|
| Revenue | $XXX M | FY2024 | [10-K, p.XX] |
| EBITDA | $XXX M | FY2024 | [Calc] |
...

## 3. 주요 리스크
- [Risk 1]
- [Risk 2]
```

---

## Next Step

→ Proceed to [Peer Selection](02-peer-selection.md)
