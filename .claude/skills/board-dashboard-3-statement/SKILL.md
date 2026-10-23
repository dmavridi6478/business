---
name: board-dashboard-3-statement
description: Specification and build method for a one-page board dashboard driven by the three financial statements - 14 panels (headline numbers, ratios against target, executive summary, free cash flow, revenue and margins, year-end cash, funded-debt covenant, coverage covenant, cash-to-cash waterfall, beyond operations, statement bridges, statement totals, capital structure, cash flow and cycle), the ratio formulas behind them, tie-out checks so projected statements reconcile, and covenant-headroom logic. Use when preparing a board or lender pack, projecting income statement, balance sheet and cash flow together, or reviewing whether a forecast ties out. Run via /board-dashboard. Source - "The Complete Board Dashboard" infographic (Oana Labes, CEO Financial Intelligence Academy); its figures are sample company data and are not reused here.
---

# Board dashboard from the three statements

Source: a one-page dashboard built on sample data. The 14 panel titles and headline sentence patterns are from it; formulas and checks are standard finance practice added here. **No sample figure from the source is a benchmark.**

## Inputs required

Income statement (revenue, direct costs, SG&A, D&A, interest, tax, net income) - balance sheet (cash, receivables, inventory, other current assets, fixed assets, payables, short- and long-term debt, equity) - cash flow (operations, investing, financing) - plan/target values for every ratio - covenant definitions and thresholds from the loan agreement - projection years (the source shows FY2026 to FY2030) and the last actual year.

## The 14 panels

| # | Panel | Content | Sentence pattern from the source |
|---|---|---|---|
| 1 | Headline numbers | Revenue, EBITDA, net income, ending cash for the year; growth vs prior year | "Revenue is projected to grow X%. Cash is projected to end at $Y." |
| 2 | Ratios against target | Profitability, liquidity, solvency, efficiency vs target | "Leverage is projected at A against a B target." |
| 3 | Exec summary | Three statements in three lines each | "FYxx is projected at revenue up X% and EBITDA down Y%." |
| 4 | Free cash flow | Operating cash flow less capex; FCF margin | "Free cash flow is projected at $X." |
| 5 | Revenue and margins | Revenue, EBITDA, net income bars; margin lines through the horizon | "Revenue is projected to reach $X by year N." |
| 6 | Year-end cash | Closing cash per year with a zero line | "Cash is projected to be negative at N year-ends." |
| 7 | Funded debt covenant | Funded debt / EBITDA vs covenant; headroom | "Projected at Nx; the covenant is Mx; headroom is H." |
| 8 | Coverage covenant | Debt service coverage vs covenant; headroom | "Projected at Nx; the covenant is Mx." |
| 9 | Cash-to-cash waterfall | Opening cash -> customers pay -> suppliers -> other -> closing | "Customers are projected to pay $X and suppliers to take $Y." |
| 10 | Beyond operations | Investing and financing items: capex, distributions, debt | "Cash is projected to fall to $X by year end." |
| 11 | Built as a bridge | Each statement bridges to the next (income -> balance sheet -> cash flow) | "Each projected statement ties to the next." |
| 12 | Statement totals | Revenue to net income; total assets and equity | "$X of revenue is projected to become $Y of net income." |
| 13 | Capital structure | Assets vs liabilities and equity; leverage | "Equity is projected at $X on $Y of assets." |
| 14 | Cash flow and cycle | Net income to operating cash; cash conversion cycle days | "$X of net income is projected to become $Y of operating cash." |

## Ratio definitions (state the version used on the page)

Gross margin = gross profit / revenue. Operating margin = operating income / revenue. EBITDA margin = EBITDA / revenue. ROE = net income / average equity. ROIC = NOPAT / invested capital. Current ratio = current assets / current liabilities. Cash conversion cycle = days inventory + days receivable - days payable. Funded debt / EBITDA as defined in the covenant. Leverage ratio here = total liabilities / equity (check: this definition reproduces the source's 8.44x from its own totals; confirm the company's definition). Inventory turnover = COGS / average inventory. Receivables turnover = revenue / average receivables. FCF = operating cash flow - capex. Debt service coverage = cash available for debt service / (interest + scheduled principal), per the covenant text.

## Tie-out checks (run before any number is shown)

1. Net income on the income statement equals the starting line of the cash flow statement.
2. Closing cash on the cash flow statement equals balance-sheet cash.
3. Assets equal liabilities plus equity in every period.
4. Change in each working-capital line matches the cash flow adjustments.
5. Covenant ratios use the contract definition, not the dashboard definition.
6. Headroom = covenant limit - projected value (or the reverse for minimums); a negative headroom is shown in red and written in the sentence.

Any failed check stops publication: the panel is replaced by "does not tie - see list".

## Output

A one-page HTML dashboard from `design-templates` (`board-dashboard-gold`) or an XLSX via the `xlsx` skill, plus a half-page "what the board must decide" list. Every figure carries its source cell or file. Projections are labelled projections; scenarios (base/low/high) named.

Pairs with: `ceo-kpi-framework`, `strategic-finance-maturity`, `profitability-ratios`, `kpi-dashboard-design`, `saas-growth-efficiency-metrics`, `ceo-reporting-skill`.

## Keywords
board dashboard, three statement model, covenant headroom, free cash flow, cash conversion cycle, lender pack
