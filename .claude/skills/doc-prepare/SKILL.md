---
name: doc-prepare
description: Prepare documents for analysis by checking sizes, extracting pages from large PDFs, and organizing files in .working/ directory. Use before analyzing 10-K filings, SEC documents, or any large PDF that may exceed context limits.
allowed-tools: Read, Bash, Glob, Grep, Write
user-invocable: true
trigger: prepare documents, extract pages, check file size, prep for analysis
---

# Document Preparation Skill

Automatically handles large PDF files by checking sizes and extracting relevant pages to `.working/` directory.

## When to Use

- Before analyzing any SEC filing (10-K, 증권신고서)
- When you encounter "exceeds context window" errors
- When starting analysis of a new company
- When user says "prepare", "extract", or "analyze [company]"

## Automated Workflow

When invoked, execute these steps automatically:

### Step 1: Identify Target Company

```
Parse the user's request to identify:
- Company name (e.g., "nota", "target-company")
- Specific file if mentioned
```

### Step 2: Check for Existing Working Files

```bash
# Check if .working/{company}/ already has files
ls -la .working/{company}/ 2>/dev/null || echo "No working files found"
```

**If files exist:** Report available files and ask if re-extraction is needed.

### Step 3: Locate Source Documents

```bash
# Find PDF files in dataroom
ls -la dataroom/{company}/*.pdf 2>/dev/null
```

### Step 4: Check File Sizes

```bash
# Run size check on each PDF
make check-file FILE=dataroom/{company}/{file}.pdf
```

**Decision Logic:**
- If **✓ OK** (< 500K tokens): File can be read directly
- If **⚠️ TOO LARGE**: Proceed to extraction

### Step 5: Extract Key Sections (for large files)

For 10-K / 증권신고서 filings, extract these sections:

```bash
# Cover and overview (company description)
make extract-pages FILE=dataroom/{company}/{file}.pdf PAGES=1-30

# Financial summary (Item 6 equivalent)
make extract-pages FILE=dataroom/{company}/{file}.pdf PAGES=45-60

# Financial statements (Item 8 equivalent)
make extract-pages FILE=dataroom/{company}/{file}.pdf PAGES=80-130

# Risk factors and detailed financials
make extract-pages FILE=dataroom/{company}/{file}.pdf PAGES=150-200

# Additional sections if needed
make extract-pages FILE=dataroom/{company}/{file}.pdf PAGES=200-250
make extract-pages FILE=dataroom/{company}/{file}.pdf PAGES=250-300
```

### Step 6: Report Results

After extraction, provide a summary:

```markdown
## Document Preparation Complete

**Company:** {company}
**Source:** dataroom/{company}/{file}.pdf ({total_pages} pages, {size})

### Files Ready for Analysis

| File | Pages | Size | Tokens (est.) |
|------|-------|------|---------------|
| .working/{company}/{file}-1-30.txt | 1-30 | XX KB | ~XX K |
| .working/{company}/{file}-80-130.txt | 80-130 | XX KB | ~XX K |
| ... | ... | ... | ... |

### Recommended Next Steps

1. For company overview:
   > "Read .working/{company}/{file}-1-30.txt and summarize the business"

2. For financial analysis:
   > "Read .working/{company}/{file}-80-130.txt and extract key metrics"

3. For full analysis:
   > "Using prompts/01-target-summary.md, analyze {company} using files in .working/{company}/"
```

## Usage Examples

### Example 1: Prepare a New Company

```
User: "Prepare nota for analysis"

Claude: [Executes workflow automatically]
1. Checks .working/nota/ - finds existing files
2. Reports available files
3. Asks if re-extraction needed
```

### Example 2: Fresh Extraction

```
User: "Extract pages 150-250 from nota SEC filing"

Claude: [Runs extraction]
make extract-pages FILE=dataroom/nota/nota-sec.pdf PAGES=150-250
```

### Example 3: Full Prep for New Company

```
User: "Prepare target-company for comparable analysis"

Claude: [Full workflow]
1. Checks .working/target-company/ - empty
2. Finds dataroom/target-company/10-K-2024.pdf
3. Checks size - 1.2M tokens (TOO LARGE)
4. Extracts key sections automatically
5. Reports ready files
```

## Page Range Reference

### US 10-K Filing

| Section | Pages | Content |
|---------|-------|---------|
| 1-10 | Cover, TOC | Basic info |
| 6-30 | Item 1 | Business description |
| 30-50 | Item 1A | Risk factors |
| 45-60 | Item 6 | Selected financial data |
| 55-80 | Item 7 | MD&A |
| 80-130 | Item 8 | Financial statements |

### Korean 증권신고서 (SEC Filing)

| Section | Pages | Content |
|---------|-------|---------|
| 1-30 | 표지, 목차 | Basic info |
| 30-100 | 회사 개요 | Company overview |
| 100-150 | 사업 내용 | Business details |
| 150-250 | 재무 정보 | Financial information |
| 250-350 | 투자위험요소 | Risk factors |

## Integration with Analysis

After preparation, use with analysis prompts:

```bash
# Target company summary
> "Using prompts/01-target-summary.md, analyze {company} using .working/{company}/"

# Peer selection
> "Using prompts/02-peer-selection.md, identify peers for {company}"

# Full comparable analysis
> "Using prompts/startup-comps-full.md, perform analysis on {company}"
```
