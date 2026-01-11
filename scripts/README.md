# Scripts Directory

Utility scripts for document processing and analysis preparation.

## Setup

Before using scripts, run the project setup:

```bash
# From project root
make setup
```

This installs `uv` and all dependencies in an isolated virtual environment.

## Available Scripts

| Script | Description | Make Command |
|--------|-------------|--------------|
| `check_document_size.py` | Check file sizes and estimate token counts | `make check` |
| `extract_sections.py` | Extract specific pages/sections from PDFs | `make extract-pages` |

---

## Usage

> **Important:** Always use `make` commands or `uv run` - never use `python` directly.

### check_document_size.py

Checks document sizes and estimates token counts to help avoid context window limits.

```bash
# Check all files in dataroom
make check

# Check a specific file
make check-file FILE=dataroom/nota/nota-sec.pdf

# Alternative: using uv run
uv run python scripts/check_document_size.py dataroom/
uv run python scripts/check_document_size.py dataroom/nota/nota-sec.pdf --limit 200000
```

**Output Example:**

```
================================================================================
File                                     Size       Est. Tokens  % Limit    Status
================================================================================
nota-sec.pdf                             5.2 MB     1.2M         230.0%    ⚠️  TOO LARGE
pitch-deck.pdf                           2.1 MB     466.7K       93.3%     ✓ OK
================================================================================

⚠️  1 file(s) exceed the token limit.
```

---

### extract_sections.py

Helps extract specific sections from SEC filings to work within context limits.

```bash
# View 10-K section guide
make guide

# View chunking strategies
make strategies

# Get PDF info (page count)
make pdf-info FILE=dataroom/nota/nota-sec.pdf

# Extract specific pages to text file
make extract-pages FILE=dataroom/nota/nota-sec.pdf PAGES=80-120 OUT=.working/nota/financials.txt

# Alternative: using uv run
uv run python scripts/extract_sections.py --guide
uv run python scripts/extract_sections.py dataroom/nota/nota-sec.pdf --info
uv run python scripts/extract_sections.py dataroom/nota/nota-sec.pdf --pages 80-120 --output .working/nota/financials.txt
```

---

## 10-K Section Reference

| Section | Typical Pages | Content |
|---------|---------------|---------|
| Cover & TOC | 1-5 | Basic info |
| Item 1: Business | 6-25 | Business description |
| Item 1A: Risk Factors | 25-45 | Risks |
| **Item 6: Selected Financial** | 45-55 | 5-year summary ★ |
| **Item 7: MD&A** | 55-80 | Management discussion ★ |
| **Item 8: Financials** | 80-130 | Full statements ★ |

★ = Key sections for financial analysis

---

## Recommended Workflow for Large Documents

1. **Check sizes first:**
   ```bash
   make check
   ```

2. **If files exceed limit, extract specific pages:**
   ```bash
   # Extract financial statements (pages 80-120)
   make extract-pages FILE=dataroom/nota/nota-sec.pdf PAGES=80-120 OUT=.working/nota/financials.txt
   ```

3. **Analyze the extracted text:**
   ```bash
   claude
   > "Read .working/nota/financials.txt and extract key financial metrics"
   ```

---

## All Make Commands

```bash
make help           # Show all available commands

# Setup
make setup          # Full setup: uv + venv + dependencies
make install        # Install dependencies only

# Document processing
make check          # Check all document sizes
make check-file FILE=path/to/file.pdf
make guide          # 10-K section guide
make strategies     # Chunking strategies
make pdf-info FILE=path/to/file.pdf
make extract-pages FILE=path PAGES=80-120 OUT=output.txt

# Development
make test           # Run tests
make lint           # Run linter
make clean          # Clean caches
```

---

## Related Documentation

- [Getting Started](../instructions/getting-started.md) - Project setup
- [Target Analysis](../instructions/02-target-analysis.md) - Handling large documents
- [Prompts README](../prompts/README.md) - Prompt templates
