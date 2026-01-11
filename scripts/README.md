# Scripts Directory

Utility scripts for document processing and analysis preparation.

## Setup

Before using scripts, run the project setup:

```bash
make setup
```

This installs `uv` and all dependencies in an isolated virtual environment.

## Available Scripts

| Script | Description |
|--------|-------------|
| `check_document_size.py` | Check file sizes and estimate token counts |
| `extract_sections.py` | Extract specific pages/sections from PDFs |
| `prep_documents.py` | Prepare company documents for analysis |
| `compile_report.py` | Compile analysis files into final report |

---

## Usage

### check_document_size.py

Checks document sizes and estimates token counts to help avoid context window limits.

```bash
# Check all files in dataroom
uv run python scripts/check_document_size.py dataroom/

# Check a specific file
uv run python scripts/check_document_size.py dataroom/nota/nota-sec.pdf

# With custom token limit
uv run python scripts/check_document_size.py dataroom/nota/nota-sec.pdf --limit 200000
```

**Output Example:**

```
================================================================================
File                                     Size       Est. Tokens  % Limit    Status
================================================================================
nota-sec.pdf                             5.2 MB     1.2M         230.0%    TOO LARGE
pitch-deck.pdf                           2.1 MB     466.7K       93.3%     OK
================================================================================

1 file(s) exceed the token limit.
```

---

### extract_sections.py

Extracts specific sections from SEC filings to work within context limits.

```bash
# View 10-K section guide
uv run python scripts/extract_sections.py --guide

# View chunking strategies
uv run python scripts/extract_sections.py --strategies

# Get PDF info (page count)
uv run python scripts/extract_sections.py dataroom/nota/nota-sec.pdf --info

# Extract specific pages to text file
uv run python scripts/extract_sections.py dataroom/nota/nota-sec.pdf --pages 80-120 --output .working/nota/financials.txt
```

---

### prep_documents.py

High-level document preparation workflow.

```bash
# Check a company's document status
uv run python scripts/prep_documents.py check nota

# Prepare documents (auto-extract if needed)
uv run python scripts/prep_documents.py prep nota

# Force re-extraction
uv run python scripts/prep_documents.py prep nota --force

# Show status of all companies
uv run python scripts/prep_documents.py status
```

---

### compile_report.py

Compiles all analysis files for a company into a comprehensive final report.

```bash
# Compile report for a company
uv run python scripts/compile_report.py nota

# With custom output path
uv run python scripts/compile_report.py nota --output output/custom-report.md
```

**Output Example:**

```
Available files: summary, peers, financials, valuation
Report compiled successfully: output/reports/nota-comps-report-2026-01-12.md
```

**What it does:**
- Reads all analysis files from `output/{company}/`
- Combines them into a single comprehensive report
- Saves to `output/reports/{company}-comps-report-{date}.md`

---

## 10-K Section Reference

| Section | Typical Pages | Content |
|---------|---------------|---------|
| Cover & TOC | 1-5 | Basic info |
| Item 1: Business | 6-25 | Business description |
| Item 1A: Risk Factors | 25-45 | Risks |
| **Item 6: Selected Financial** | 45-55 | 5-year summary |
| **Item 7: MD&A** | 55-80 | Management discussion |
| **Item 8: Financials** | 80-130 | Full statements |

---

## Recommended Workflow for Large Documents

1. **Check sizes first:**
   ```bash
   uv run python scripts/check_document_size.py dataroom/
   ```

2. **If files exceed limit, extract specific pages:**
   ```bash
   uv run python scripts/extract_sections.py dataroom/nota/nota-sec.pdf --pages 80-120 --output .working/nota/financials.txt
   ```

3. **Analyze the extracted text:**
   ```bash
   claude
   > "Read .working/nota/financials.txt and extract key financial metrics"
   ```

---

## Related Documentation

- [Getting Started](../instructions/getting-started.md) - Project setup
- [Target Analysis](../instructions/02-target-analysis.md) - Handling large documents
- [Prompts README](../prompts/README.md) - Prompt templates
