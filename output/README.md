# Output Directory

This directory contains **final analysis outputs and reports**.

## Directory Structure

```
output/
├── {company-name}/          # Company-specific analysis outputs
│   ├── 01-company-summary.md
│   ├── 02-peer-analysis.md
│   ├── 03-valuation.md
│   └── ...
├── reports/                 # Cross-company reports and summaries
│   └── comparable-analysis.md
└── README.md                # This file
```

## File Naming Convention

| Stage | Filename | Description |
|-------|----------|-------------|
| 2 | `01-company-summary.md` | Target company financial summary |
| 3 | `02-peer-analysis.md` | Peer company comparison |
| 4 | `03-valuation.md` | Valuation multiples and implied value |
| 5 | `04-final-report.md` | Complete analysis report |

## Notes

- **Intermediate files** (pre-extracted PDFs) go in `/.working/`, not here
- **Source documents** remain in `/dataroom/`
- Output files should include citations: `[File Name, Page X]`
- Korean language for narrative, English for financial terms

## Example

See `nota/01-company-summary.md` for a sample output format.
