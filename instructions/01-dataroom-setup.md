# Stage 1: Dataroom Setup

Prepare and organize source materials for analysis.

**Previous:** - | **Next:** [Target Analysis](02-target-analysis.md) | **Main:** [Workflow Overview](analysis-workflow.md)

---

## Overview

The `/dataroom` directory contains all source documents for your analysis. Proper organization ensures efficient data extraction and reproducible results.

---

## Supported Document Types

| Document Type | Description | Common Sources |
|---------------|-------------|----------------|
| SEC Filings | 10-K (annual), 10-Q (quarterly), 8-K (current) | [SEC EDGAR](https://www.sec.gov/edgar/searchedgar/companysearch) |
| Korean Filings | 사업보고서, 분기보고서 | [DART](https://dart.fss.or.kr) |
| Earnings Reports | Quarterly releases, investor presentations | Company IR websites |
| Financial Statements | Income statement, balance sheet, cash flow | SEC filings, annual reports |
| Market Data | Stock prices, trading volumes, market cap | Bloomberg, FactSet, Yahoo Finance |
| Private Company Data | Pitch decks, CIMs, unaudited financials, cap tables | Management, VDRs |

---

## Directory Structure

Create this folder structure within `/dataroom`:

```
dataroom/
├── target-company/
│   ├── sec-filings/           # For public companies
│   │   ├── 10-K-2024.pdf
│   │   ├── 10-K-2023.pdf
│   │   └── 10-Q-Q3-2024.pdf
│   ├── financials/            # For private companies
│   │   ├── unaudited-2023.xlsx
│   │   └── projections-2024-2028.xlsx
│   ├── presentations/         # Investor decks, CIMs
│   │   ├── investor-day-2024.pdf
│   │   └── intro-deck-2024.pdf
│   ├── corporate/             # Cap tables, org charts
│   │   └── cap-table.xlsx
│   └── earnings/              # Earnings releases
│       └── Q3-2024-earnings.pdf
│
├── peer-companies/
│   ├── company-a/
│   │   └── 10-K-2024.pdf
│   ├── company-b/
│   │   └── 10-K-2024.pdf
│   └── company-c/
│       └── 10-K-2024.pdf
│
└── market-data/               # Industry data
    ├── trading-comps.csv
    ├── industry-report-2024.pdf
    └── market-statistics.xlsx
```

---

## File Naming Conventions

Use consistent, descriptive file names:

```
[company-ticker]-[document-type]-[period].[ext]

Examples (Public Companies):
- nota-10-K-2024.pdf
- aapl-10-Q-Q3-2024.pdf
- msft-earnings-Q2-2024.pdf

Examples (Private Companies):
- startup-deck-seed-round.pdf
- scaleup-financials-2023.xlsx
- targetco-cim-2024.pdf
```

---

## Downloading SEC Filings

### Manual Download (SEC EDGAR)

1. Go to [SEC EDGAR Company Search](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany)
2. Search by company name or CIK number
3. Filter by filing type (10-K, 10-Q, etc.)
4. Download as PDF or HTML

### Using Claude CLI

```bash
claude
> "Help me find the latest 10-K filing for [Company Name] and provide the SEC EDGAR link"
```

### Korean Filings (DART)

1. Go to [DART](https://dart.fss.or.kr)
2. Search by company name (한글 or English)
3. Filter by 사업보고서 or 분기보고서
4. Download as PDF

---

## Private Company Documents

### Common Document Types

| Document | Contents | Key Data |
|----------|----------|----------|
| Pitch Deck | Business overview, market, traction | Revenue, customers, growth |
| CIM (Confidential Info Memo) | Detailed business description | Full financials, projections |
| Unaudited Financials | Historical P&L, balance sheet | Revenue, EBITDA, margins |
| Projections | Management forecasts | Growth assumptions |
| Cap Table | Ownership structure | Shares, valuation history |

### Quality Considerations

Private company data requires extra validation:

- [ ] Identify GAAP vs. non-GAAP metrics
- [ ] Note "Adjusted EBITDA" add-backs
- [ ] Flag owner/related-party expenses
- [ ] Compare projections to historical growth
- [ ] Verify currency and units

---

## Checklist Before Proceeding

Before moving to Target Analysis:

- [ ] Target company documents organized in `dataroom/target-company/`
- [ ] At least one financial document available (10-K, pitch deck, financials)
- [ ] File names follow naming convention
- [ ] Document dates and periods noted
- [ ] Currency identified (USD, KRW, etc.)

---

## Next Step

→ Proceed to [Target Analysis](02-target-analysis.md)
