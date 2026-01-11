---
name: pdf-parser
description: Prepare documents for analysis by checking sizes, extracting pages from large PDFs, and organizing files in .working/ directory. Use before analyzing 10-K filings, SEC documents, or any large PDF that may exceed context limits.
allowed-tools: Read, Bash, Glob, Grep, Write
user-invocable: true
trigger: prepare documents, extract pages, check file size, prep for analysis
---

# PDF Parser Skill

Handles large PDF files by checking sizes and extracting relevant pages to `.working/` directory.

## Quick Reference

| Command | Purpose |
|---------|---------|
| `uv run python scripts/prep_documents.py check {company}` | Check if documents need preparation |
| `uv run python scripts/prep_documents.py prep {company}` | Auto-extract using default ranges |
| `uv run python scripts/check_document_size.py {file}` | Check single file size |

## Workflow

### Step 1: Check Status

```bash
uv run python scripts/prep_documents.py check {company}
```

**If files exist in `.working/{company}/`**: Report available files, skip extraction unless `--force`.

### Step 2: Size Check

Run for each source PDF:
```bash
uv run python scripts/check_document_size.py dataroom/{company}/{file}.pdf
```

**Decision:**
- **OK** (< 500K tokens): Read directly, no extraction needed
- **TOO LARGE**: Proceed to extraction

### Step 3: Extract (if needed)

Use auto-extraction:
```bash
uv run python scripts/prep_documents.py prep {company}
```

Or extract specific pages:
```bash
uv run python scripts/extract_sections.py dataroom/{company}/{file}.pdf --pages 80-130 --output .working/{company}/{file}-80-130.txt
```

**Common page ranges for US 10-K:**
- Pages 1-30: Cover, TOC, Business description
- Pages 45-60: Selected financial data
- Pages 80-130: Financial statements

**Common page ranges for Korean SEC Filing (증권신고서):**
- Pages 1-30: 표지, 목차
- Pages 100-150: 사업 내용
- Pages 150-200: 재무 정보
- Pages 250-320: 재무제표

### Step 4: Verify & Report

After extraction, verify files exist and report:

```markdown
## Document Preparation Complete

**Company:** {company}
**Source:** dataroom/{company}/{file}.pdf

### Files Ready
| File | Pages | Est. Tokens |
|------|-------|-------------|
| .working/{company}/{file}-1-30.txt | 1-30 | ~XX K |
| .working/{company}/{file}-80-130.txt | 80-130 | ~XX K |

### Next Steps
1. Read `.working/{company}/{file}-1-30.txt` for company overview
2. Read `.working/{company}/{file}-80-130.txt` for financial data
3. Use `prompts/01-target-summary.md` for full analysis
```

## Page Range Reference

### US 10-K Structure

| Pages | Section | Content |
|-------|---------|---------|
| 1-10 | Cover | Basic info, TOC |
| 6-30 | Item 1 | Business description |
| 30-50 | Item 1A | Risk factors |
| 45-60 | Item 6 | Selected financial data |
| 55-80 | Item 7 | MD&A |
| 80-130 | Item 8 | Financial statements |

### Korean 증권신고서 Structure

| Pages | Section | Content |
|-------|---------|---------|
| 1-30 | 표지/목차 | Basic info |
| 30-100 | 회사 개요 | Company overview |
| 100-150 | 사업 내용 | Business details |
| 150-250 | 재무 정보 | Financial information |
| 250-350 | 재무제표 | Financial statements |

## Output Locations

Per `prompts/05-output-format.md`, save analysis outputs to:

```
output/
├── {company-name}/
│   ├── 01-company-summary.md
│   ├── 02-peer-selection.md
│   ├── 03-financial-data.md
│   ├── 03-financial-data.csv
│   ├── 04-valuation-analysis.md
│   └── 04-comps-table.csv
└── reports/
    └── {company-name}-comps-report-{YYYY-MM-DD}.md
```

## Validation Checklist

Before analysis, verify:
- [ ] Source PDF exists in `dataroom/{company}/`
- [ ] Working files created in `.working/{company}/`
- [ ] Each working file < 500K tokens
- [ ] Key sections extracted (financials, business description)
