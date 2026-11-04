---
name: fpna-budget-actual-forecast
description: Budget-to-actual-to-forecast workflow (build, sign off, save down, actualize, compare) with one rolling forecast beside a locked budget, and a chooser for eight variance views (donut, waterfall, column, cutoff, bar, line, table, KPI). Use when setting up monthly variance reporting, choosing how to present a variance to a board or a department head, or reviewing a forecast that quietly drifts from the budget.
---

# From budget to actual to forecast

Source: a finance infographic (Batch 122, "From Budget to Actual to Forecast: one budget, a rolling forecast, a monthly comparison"). It carries a promotion for a spreadsheet add-in at the bottom ("rolls your forecast forward in a few clicks"); that line is an advert, not method. The method below stands without any tool.

## The process (five steps)

| Step | What happens | Control to add |
|---|---|---|
| 1. Build | First pass of the budget, department by department | One owner per line; one set of drivers (headcount, price, volume) in one place |
| 2. Sign off | Management and the board approve it, or both | Record who approved, on what date, against which version |
| 3. Save down | A separate, locked version of the approved budget | Write-protect it. If someone can edit it, it is not a budget, it is a second forecast |
| 4. Actualize | Each month, actuals replace the forecast months | Close the month first; load actuals from the ledger, not from a re-keyed export |
| 5. Compare | Where were you on the budget? Where are you on the forecast? | Always show both gaps side by side |

## One budget, one rolling forecast

The graphic's table has three rows over twelve months:

- **Budget v1** (saved down, never touched).
- **Rolling forecast** = actuals for closed months, then forecast for the open months. It starts equal to the budget and moves every month.
- **Variance** = actual minus budget for closed months (the graphic's red numbers).

Two traps the graphic leaves out:

1. **Sign convention.** Decide once whether a positive variance is favourable or adverse and apply it to revenue and cost lines differently. A revenue shortfall and a cost overrun are both adverse, but one is negative and the other positive in "actual minus budget". Mixed signs are the commonest source of a wrong board slide.
2. **Rolling forecast hides slippage.** If you only ever show actual versus the latest forecast, a bad year looks fine. Keep the actual versus the locked budget on the same page.

## Eight ways to show the variance (pick one per audience)

| View | Best for (from the graphic) | Use it when | Avoid it when |
|---|---|---|---|
| Donut | How much of the budget has been used | One number: share used or left | There is more than one category |
| Waterfall | Explains exactly what drove the gap | A board wants the bridge from budget to actual | More than about eight steps |
| Column | Sort largest first; big lines lead | Comparing departments | Time series |
| Cutoff | The cleanest read on over versus under | One threshold such as budget | No clear threshold |
| Bar | The biggest misses jump right out | Ranking departments by variance | Few departments (a table is shorter) |
| Line | Analysing trends | Run-rate drift across months | A single month |
| Table | Every figure, nothing hidden | Finance review, audit trail | A board without time to read it |
| KPI | Number plus trend in tiny space | Executive dashboard header | Anything needing explanation |

Rule of thumb: boards get the waterfall and a KPI row; department heads get the bar chart and the table; finance keeps the table as the source and everything else is derived from it.

## Variance commentary standard

For every line above the materiality threshold (for example 5 percent and a currency amount, both, not either) write: what happened, why, whether it repeats, and the action with an owner and a date. A variance with no cause is a question, not a result.

## Checks before it goes out

- Actuals tie to the ledger and the closing trial balance.
- The locked budget has not changed since sign-off (compare a hash or a copy).
- The forecast months are labelled as forecast on every chart.
- Currency, period and entity are on the page.

Run with `/variance-views <your categories and the audience>`. Related: `board-dashboard-3-statement`, `kpi-scorecard`, `kpi-dashboard-design`, `startup-financial-modeling`, `finance:variance-analysis`, `agentic-council:finance-variance-analysis`, `data-storytelling`.
