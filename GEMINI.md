# Project Instructions

## Overview
This project serves as an educational example for performing comparable financial analysis.

## Analysis Workflow (5 Stages)

| Stage | Instruction | Prompt | Description |
|-------|-------------|--------|-------------|
| 0 | `00-dataroom-setup.md` | - | Organize source documents |
| 1 | `01-target-analysis.md` | `01-target-summary.md` | Analyze target company |
| 2 | `02-peer-selection.md` | `02-peer-selection.md` | Select peers + extract data |
| 3 | `03-valuation.md` | `03-valuation-analysis.md` | Calculate valuation multiples |
| 4 | `04-output-reports.md` | `04-output-format.md` | Generate final reports |

**Utility Prompts:** Files prefixed with `_` (e.g., `_base.md`, `_extract-financials.md`) are reusable components referenced by other prompts.

**Full Workflow:** Use `prompts/startup-comps-full.md` to run all stages end-to-end.

## Development Rules

- **Educational Materials**: All instructions and how-to guides must be drafted in the `/instructions` directory.
- **Educational Scripts**: All scripts designed for educational purposes must be placed in the `/scripts` directory.
- **Source Code**: All non-educational source code (for the underlying development and tooling of this project) must remain in the `/src` directory. Students are not expected to interact with this directory.
- **Outputs**: There is no front-end or website development. All automated outputs should be in Markdown, CSV, or simple text file formats.
