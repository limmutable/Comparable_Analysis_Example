# Output Directory

This directory contains **final analysis outputs and reports**.

## Directory Structure

```
output/
├── {company-name}/          # Company-specific analysis outputs
│   ├── 01-target-summary.md
│   ├── 02-peer-selection.md  # Includes peer financial data
│   ├── 02-peer-data.csv
│   ├── 03-valuation-analysis.md
│   ├── 03-comps-table.csv
│   └── ...
├── reports/                 # Cross-company reports and summaries
│   └── {company}-comps-report-{date}.md
└── README.md                # This file
```

## File Naming Convention

| Stage | Filename | Description |
|-------|----------|-------------|
| 1 | `01-target-summary.md` | Target company financial summary |
| 2 | `02-peer-selection.md` | Peer group selection + financial data |
| 2 | `02-peer-data.csv` | Peer financial data export |
| 3 | `03-valuation-analysis.md` | Valuation multiples and implied value |
| 3 | `03-comps-table.csv` | Comps table export |
| 4 | `reports/{company}-comps-report-{date}.md` | Complete analysis report |

## Notes

- **Intermediate files** (pre-extracted PDFs) go in `/.working/`, not here
- **Source documents** remain in `/dataroom/`
- Output files should include citations: `[File Name, Page X]`
- Korean language for narrative, English for financial terms

## Example

See `nota/01-target-summary.md` for a sample output format.
