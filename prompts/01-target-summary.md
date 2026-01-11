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

## Pre-flight Check (REQUIRED)

**Before reading any PDF, you MUST check for large files:**

### Step 1: Check for Pre-extracted Files

```bash
# First, check if .working/{company}/ has pre-extracted text files
ls .working/

# If files exist, use them directly (PREFERRED)
# Example: .working/nota/financials-150-200.txt
```

### Step 2: If No Pre-extracted Files, Check File Size

```bash
uv run python scripts/check_document_size.py dataroom/{company}/{file}.pdf
```

### Step 3: Handle Based on Size

| Status | Action |
|--------|--------|
| **OK** (< 500K tokens) | Read the PDF directly |
| **TOO LARGE** (> 500K tokens) | Extract pages first (see below) |

### Step 4: Extract Pages for Large Files

```bash
# Extract specific page ranges to .working/
uv run python scripts/extract_sections.py dataroom/{company}/{file}.pdf --pages 80-120 --output .working/{company}/{file}-80-120.txt

# Then read the extracted text file instead
```

---

## Handling Large Documents

> **CRITICAL:** Never attempt to read a full 10-K/증권신고서 directly. Always use pre-extracted files from `.working/` or extract pages first.

### Recommended Extraction Ranges for 10-K/증권신고서

| Section | Pages | Extract Command |
|---------|-------|-----------------|
| Cover & Overview | 1-30 | `uv run python scripts/extract_sections.py ... --pages 1-30` |
| Financial Summary | 45-55 | `uv run python scripts/extract_sections.py ... --pages 45-55` |
| Financial Statements | 80-130 | `uv run python scripts/extract_sections.py ... --pages 80-130` |
| Risk Factors | 150-200 | `uv run python scripts/extract_sections.py ... --pages 150-200` |

### Key 10-K Sections

| Section | Pages | Priority |
|---------|-------|----------|
| Item 6: Selected Financial | 45-55 | 5-year summary |
| Item 8: Financial Statements | 80-130 | Full financials |
| Item 7: MD&A | 55-80 | Context |
| Item 1: Business | 6-25 | Overview |

---

## Analysis Checklist

Before starting, confirm:
- [ ] **Pre-extracted files checked** in `.working/{company}/`
- [ ] **File size verified** (< 500K tokens) OR pages extracted
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

## Output File Location

**IMPORTANT:** Save the output to the correct location following the project structure:

```
output/{company-name}/01-target-summary.md
```

For example:
- `output/nota/01-target-summary.md`
- `output/target-company/01-target-summary.md`

> See `prompts/04-output-format.md` for full output directory structure.

---

## Output Format

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
**분석 기준일:** YYYY-MM-DD
```

---

## Usage Examples

### Example 1: Using Pre-extracted Files (Recommended)

```bash
# If .working/nota/ already has extracted files:
claude
> "Using prompts/01-target-summary.md, analyze Nota using the files in .working/nota/"

# Or be specific:
> "Read .working/nota/cover.txt and .working/nota/financials-150-200.txt to create a company summary for Nota"
```

### Example 2: Small PDF (< 500K tokens)

```bash
# First check size
uv run python scripts/check_document_size.py dataroom/target-company/pitch-deck.pdf

# If OK, read directly
claude
> "Using prompts/01-target-summary.md, analyze dataroom/target-company/pitch-deck.pdf"
```

### Example 3: Large PDF (Extract First)

```bash
# Step 1: Check size (will show TOO LARGE)
uv run python scripts/check_document_size.py dataroom/nota/nota-sec.pdf

# Step 2: Extract key sections
uv run python scripts/extract_sections.py dataroom/nota/nota-sec.pdf --pages 1-30 --output .working/nota/nota-sec-1-30.txt
uv run python scripts/extract_sections.py dataroom/nota/nota-sec.pdf --pages 150-200 --output .working/nota/nota-sec-150-200.txt

# Step 3: Analyze extracted files
claude
> "Using prompts/01-target-summary.md, analyze Nota using .working/nota/nota-sec-1-30.txt and .working/nota/nota-sec-150-200.txt"
```

---

## Next Steps

After completing target summary, proceed to:
- `02-peer-selection.md` - Select comparable companies and extract their financial data
