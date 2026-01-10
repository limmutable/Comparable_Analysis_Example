---
name: financial-modeling
description: Build financial models, create forecasts, and compute valuations (DCF, multiples). Use when working with financial projections, budgets, or valuation analysis.
allowed-tools: Read, Bash, Edit, Write, Glob, Grep
---

# Financial Modeling

## Instructions

When building financial models:

1. **Structure**
   - Separate assumptions from calculations
   - Use clear section headers (Inputs, Calculations, Outputs)
   - Show formulas and logic explicitly

2. **Revenue Modeling**
   - Break down by segment, product, or geography
   - Use driver-based projections (units × price, users × ARPU)
   - Document growth rate assumptions

3. **Expense Modeling**
   - Distinguish fixed vs variable costs
   - Model as % of revenue where appropriate
   - Include operating leverage effects

4. **Cash Flow Projections**
   - Start from Net Income
   - Add back non-cash items (D&A, stock comp)
   - Account for working capital changes
   - Subtract CapEx

5. **Valuation**
   - DCF: Project FCF 5-10 years, apply WACC, calculate terminal value
   - Multiples: Apply EV/EBITDA, P/E, EV/Revenue to projections
   - Show sensitivity analysis on key assumptions

## Output Format

- Use Markdown tables for financial statements
- Include units ($ millions, thousands, etc.)
- Show year-over-year growth rates
- Export detailed models as CSV when requested
