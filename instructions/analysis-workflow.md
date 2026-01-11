# Analysis Workflow Guide

This guide explains the end-to-end process for conducting comparable financial analysis—from preparing source materials to generating final reports.

---

## Table of Contents

1. [Preparing Source Materials](#1-preparing-source-materials)
2. [Reading and Parsing Data](#2-reading-and-parsing-data)
3. [Creating Analysis Prompts](#3-creating-analysis-prompts)
4. [Performing Analysis](#4-performing-analysis)
5. [Structuring Output](#5-structuring-output)
6. [Generating Reports](#6-generating-reports)

---

## 1. Preparing Source Materials

Source materials are stored in the `/dataroom` directory. This section covers how to organize and prepare documents for analysis.

### 1.1 Supported Document Types

| Document Type | Description | Common Sources |
|---------------|-------------|----------------|
| SEC Filings | 10-K (annual), 10-Q (quarterly), 8-K (current events) | [SEC EDGAR](https://www.sec.gov/edgar/searchedgar/companysearch) |
| Earnings Reports | Quarterly earnings releases, investor presentations | Company IR websites |
| Financial Statements | Income statement, balance sheet, cash flow statement | SEC filings, annual reports |
| Market Data | Stock prices, trading volumes, market cap | Financial data providers |
| Private Company Data| Pitch decks, CIMs, Unaudiated financials, Cap tables | Company management, VDRs |

### 1.2 Organizing the Dataroom

Create a logical folder structure within `/dataroom`:

```
dataroom/
├── target-company/
│   ├── sec-filings/
│   │   ├── 10-K-2024.pdf
│   │   ├── 10-K-2023.pdf
│   │   └── 10-Q-Q3-2024.pdf
│   ├── earnings/
│   │   └── Q3-2024-earnings.pdf
│   └── presentations/
│       └── investor-day-2024.pdf
├── private-target/
│   ├── financials/
│   │   ├── unaudited-2023.xlsx
│   │   └── projections-2024-2028.xlsx
│   ├── presentations/
│   │   ├── intro-deck-2024.pdf
│   │   └── management-presentation.pdf
│   └── corporate/
│       └── cap-table.xlsx
├── peer-companies/
│   ├── company-a/
│   │   └── 10-K-2024.pdf
│   ├── company-b/
│   │   └── 10-K-2024.pdf
│   └── company-c/
│       └── 10-K-2024.pdf
└── market-data/
    └── trading-comps.csv
```

### 1.3 File Naming Conventions

Use consistent, descriptive file names:

```
[company-ticker]-[document-type]-[period].pdf

Examples:
- nota-10-K-2024.pdf
- aapl-10-Q-Q3-2024.pdf
- msft-earnings-Q2-2024.pdf
- startup-deck-seed-round.pdf
- scaleup-financials-2023.xlsx
```

### 1.4 Downloading SEC Filings

**Manual Download:**
1. Go to [SEC EDGAR](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany)
2. Search by company name or CIK number
3. Filter by filing type (10-K, 10-Q, etc.)
4. Download the filing as PDF

**Using Claude CLI:**
```bash
claude
> "Help me find and download the latest 10-K filing for [Company Name]"
```

---

## 2. Reading and Parsing Data

Once materials are in the dataroom, extract the relevant financial data for analysis.

### 2.1 Key Data Points to Extract

**From Income Statement:**
- Revenue / Net Sales
- Cost of Goods Sold (COGS)
- Gross Profit
- Operating Expenses (SG&A, R&D)
- Operating Income (EBIT)
- Interest Expense
- Net Income
- Earnings Per Share (EPS)
- Shares Outstanding

**From Balance Sheet:**
- Cash and Cash Equivalents
- Total Assets
- Total Debt (Short-term + Long-term)
- Shareholders' Equity
- Book Value Per Share

**From Cash Flow Statement:**
- Operating Cash Flow
- Capital Expenditures (CapEx)
- Free Cash Flow
- Depreciation & Amortization

**Market Data:**
- Current Stock Price
- Market Capitalization
- Enterprise Value

### 2.2 Using Claude to Parse Documents

Start Claude in the project directory and ask it to read and extract data:

```bash
cd ~/Projects/Comparable_Analysis_Example
claude

# Parse a specific SEC filing
> "Read the 10-K filing at dataroom/nota-sec.pdf and extract the key financial metrics from the most recent fiscal year"

# Extract specific data points
> "From the 10-K in the dataroom, extract: Revenue, EBITDA, Net Income, Total Debt, and Cash for the last 3 fiscal years"

# Create a structured summary
> "Parse the financial statements from dataroom/nota-sec.pdf and create a summary table with Income Statement, Balance Sheet, and Cash Flow highlights"
```

### 2.3 Data Validation Checklist

After extracting data, verify:

- [ ] Numbers match between different sections of the filing
- [ ] Units are consistent (millions, thousands, etc.)
- [ ] Fiscal year end dates are correct
- [ ] Per-share figures use correct share count
- [ ] EBITDA calculation is consistent (Operating Income + D&A)

### 2.4 Handling Multiple Companies

When analyzing peer companies, create a standardized extraction template:

> "For each company in dataroom/peer-companies/, extract the following metrics and create a comparison table: Revenue, EBITDA, EBITDA Margin, Net Income, Total Debt, Cash, and calculate Enterprise Value"
```

### 2.5 Handling Private Company Data (Unstructured)

Private companies often provide messy or incomplete data.

**Scanning Intros/Decks:**
```bash
> "Read the pitch deck at dataroom/private-target/presentations/intro-deck-2024.pdf. Summarize the business model, key customers, and any mentioned financial milestones."
```

**Parsing Unaudited Financials (Excel/PDF):**
```bash
> "Read dataroom/private-target/financials/unaudited-2023.xlsx. Extract the historical P&L and reformat it into a standard Income Statement. Note which line items might need adjustment (e.g., 'Owner's Personal Expenses')."
```

**Validating Projections:**
```bash
> "Compare the management projections in dataroom/private-target/financials/projections.xlsx with historical growth rates. Flag any aggressive assumptions."
```

---

## 3. Creating Analysis Prompts

Effective prompts produce better analysis. Store reusable prompts in the `/prompts` directory.

### 3.1 Prompt Structure

A well-structured analysis prompt includes:

```markdown
## Context
[Background on the company/industry being analyzed]

## Objective
[Specific goal of the analysis]

## Data Sources
[List of documents to reference]

## Required Outputs
[Expected deliverables and format]

## Constraints
[Any limitations or specific requirements]
```

### 3.2 Example Prompts

**Comparable Company Analysis Prompt:**

```markdown
## Context
Analyzing [Target Company] in the [Industry] sector to determine fair valuation.

## Objective
Perform a comparable company analysis using public market trading multiples.

## Data Sources
- Target company 10-K: dataroom/target-company/10-K-2024.pdf
- Peer company filings in dataroom/peer-companies/

## Required Outputs
1. Peer selection rationale (5-7 comparable companies)
2. Trading multiples table (EV/Revenue, EV/EBITDA, P/E)
3. Statistical summary (mean, median, high, low)
4. Implied valuation range for target company

## Constraints
- Use LTM (Last Twelve Months) financials
- Exclude companies with negative EBITDA from EV/EBITDA analysis
- Note any adjustments made for one-time items
```

**Financial Statement Analysis Prompt:**

```markdown
## Context
Deep-dive analysis of [Company Name] financial health and performance.

## Objective
Analyze profitability, liquidity, and leverage trends over the past 3 years.

## Data Sources
- dataroom/[company]/10-K-2024.pdf
- dataroom/[company]/10-K-2023.pdf
- dataroom/[company]/10-K-2022.pdf

## Required Outputs
1. Profitability analysis (margins, ROE, ROIC)
2. Liquidity analysis (current ratio, quick ratio, cash conversion cycle)
3. Leverage analysis (Debt/EBITDA, interest coverage)
4. Year-over-year trend commentary

## Constraints
- Highlight any significant changes (>10% YoY)
- Flag potential concerns or red flags
```

### 3.3 Saving Prompts

Save reusable prompts as Markdown files:

```bash
# Create a prompts file
cat > prompts/comparable-analysis.md << 'EOF'
# Comparable Company Analysis Prompt

## Context
...
EOF
```

---

## 4. Performing Analysis

Use Claude's built-in skills, custom scripts, and tools to execute the analysis.

### 4.1 Using Claude Skills

This project includes two financial analysis skills that activate automatically:

| Skill | When to Use | Example Prompts |
|-------|-------------|-----------------|
| `financial-analysis` | Comparable comps, financial statement analysis, valuation multiples | "Create a comp table for tech companies" |
| `financial-modeling` | DCF models, forecasts, projections | "Build a 5-year DCF model" |

**Invoking Skills:**

```bash
claude

# Financial Analysis skill activates automatically
> "Analyze the SEC filing in dataroom/nota-sec.pdf and create a comparable company analysis"

# Financial Modeling skill activates automatically
> "Using the data from the 10-K, build a DCF valuation model with 5-year projections"
```

### 4.2 Step-by-Step Analysis Workflow

**Step 1: Initial Document Review**
```bash
> "Read dataroom/nota-sec.pdf and provide a summary of the company's business, key financial metrics, and any notable items"
```

**Step 2: Peer Selection**
```bash
> "Based on the company profile, suggest 5-7 comparable public companies in the same industry with similar business models and size"
```

**Step 3: Data Extraction**
```bash
> "Extract the following metrics for the target company and each peer: Revenue, EBITDA, Net Income, Total Debt, Cash, Market Cap. Calculate Enterprise Value for each."
```

**Step 4: Calculate Multiples**
```bash
> "Calculate trading multiples for each company: EV/Revenue, EV/EBITDA, P/E. Create a comp table showing all companies with mean, median, high, and low statistics."
```

**Step 5: Valuation Analysis**
```bash
> "Apply the median multiples from the peer group to the target company's financials. Provide an implied valuation range."
```

### 4.3 Using Scripts (Optional)

For repetitive calculations, use Python scripts in `/scripts`:

```bash
# Run a calculation script
python scripts/calculate_multiples.py --input dataroom/financials.csv --output output/multiples.csv
```

### 4.4 Combining Multiple Data Sources

```bash
> "Combine the financial data from all 10-K filings in the dataroom and create a consolidated peer comparison. Use the market data in dataroom/market-data/trading-comps.csv for current stock prices."
```

---

## 5. Structuring Output

All analysis outputs should be saved to the `/output` directory in structured formats.

### 5.1 Output Directory Structure

```
output/
├── [company-name]/
│   ├── financial-summary.md
│   ├── comp-table.csv
│   ├── valuation-analysis.md
│   └── dcf-model.csv
└── reports/
    └── [company-name]-analysis-[date].md
```

### 5.2 Standard Output Formats

**Markdown (.md)** - For narrative analysis and formatted tables:
- Executive summaries
- Investment thesis
- Detailed commentary
- Tables with formatting

**CSV (.csv)** - For numerical data and spreadsheet compatibility:
- Financial data extracts
- Comp tables
- Model outputs
- Time series data

### 5.3 Table Formatting Standards

**Markdown Tables:**

```markdown
| Company | Revenue ($M) | EBITDA ($M) | EV/Revenue | EV/EBITDA |
|---------|-------------:|------------:|-----------:|----------:|
| Target  |        1,200 |         180 |       4.2x |     28.0x |
| Peer A  |        2,500 |         400 |       3.8x |     23.8x |
| Peer B  |          800 |         120 |       5.0x |     33.3x |
| **Mean**|              |             |   **4.3x** | **28.4x** |
| **Median**|            |             |   **4.2x** | **28.0x** |
```

**CSV Format:**

```csv
Company,Revenue_M,EBITDA_M,EV_Revenue,EV_EBITDA
Target,1200,180,4.2,28.0
Peer A,2500,400,3.8,23.8
Peer B,800,120,5.0,33.3
```

### 5.4 Saving Outputs with Claude

```bash
> "Save the comp table to output/nota/comp-table.csv"

> "Create a financial summary and save it to output/nota/financial-summary.md"
```

---

## 6. Generating Reports

Combine analysis outputs into comprehensive reports.

### 6.1 Report Structure

A complete analysis report should include:

```markdown
# [Company Name] - Comparable Analysis Report

## Executive Summary
- Key findings (2-3 bullet points)
- Implied valuation range
- Investment recommendation

## Company Overview
- Business description
- Key products/services
- Recent developments

## Financial Highlights
- Revenue and growth trends
- Profitability metrics
- Balance sheet strength

## Peer Group Analysis
- Peer selection criteria
- Comparable companies overview
- Trading multiples comparison

## Valuation Analysis
- Methodology
- Comp table with statistics
- Implied valuation range
- Sensitivity analysis

## Risks and Considerations
- Key risks
- Data limitations
- Market factors

## Appendix
- Detailed financial data
- Data sources
- Methodology notes
```

### 6.2 Generating Reports with Claude

**Full Report Generation:**
```bash
> "Generate a complete comparable analysis report for the company in dataroom/nota-sec.pdf. Include executive summary, financial highlights, peer comparison, and valuation analysis. Save to output/reports/nota-analysis.md"
```

**Report from Existing Analysis:**
```bash
> "Combine the financial summary from output/nota/financial-summary.md and the comp table from output/nota/comp-table.csv into a formatted analysis report. Save to output/reports/nota-final-report.md"
```

### 6.3 Exporting to CSV

For spreadsheet analysis, export numerical data:

```bash
> "Export the peer comparison data to CSV format with columns: Company, Ticker, Revenue, EBITDA, Net Income, Market Cap, EV, EV/Revenue, EV/EBITDA, P/E. Save to output/nota/peer-comparison.csv"
```

### 6.4 Report Quality Checklist

Before finalizing a report, verify:

- [ ] All numbers are sourced and accurate
- [ ] Units are clearly labeled ($ millions, etc.)
- [ ] Calculations are correct and reproducible
- [ ] Peer selection is justified
- [ ] Assumptions are documented
- [ ] Risks and limitations are disclosed
- [ ] Report date and data freshness are noted

---

## Quick Reference

### Common Claude Commands

| Task | Command |
|------|---------|
| Read a filing | `"Read dataroom/[file].pdf and summarize key financials"` |
| Extract data | `"Extract revenue, EBITDA, and net income from the 10-K"` |
| Create comp table | `"Create a comparable company analysis table"` |
| Calculate multiples | `"Calculate EV/EBITDA and P/E multiples for these companies"` |
| Build DCF model | `"Build a DCF valuation model with 5-year projections"` |
| Generate report | `"Generate a full analysis report and save to output/"` |
| Export to CSV | `"Export the data to CSV format"` |

### Key Metrics Reference

See `.claude/skills/financial-analysis/key-metrics.md` for formulas and definitions of:
- Valuation multiples (EV/EBITDA, P/E, EV/Revenue)
- Profitability ratios (margins, ROE, ROIC)
- Liquidity ratios (current ratio, quick ratio)
- Leverage ratios (Debt/EBITDA, interest coverage)

---

## Next Steps

After completing your analysis:

1. Review outputs in `/output` directory
2. Validate calculations against source documents
3. Share reports with stakeholders
4. Archive source materials for future reference

For additional guidance, see other documents in the `/instructions` directory.
