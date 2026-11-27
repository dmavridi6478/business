---
name: excel-ppt-prompts-10
description: Ten prompts for Excel and PowerPoint run with Copilot or Claude so the assistant edits the file directly (waterfall chart, rolling 12-month dashboard, data validation checker, three-way match, KPI scorecard, board-ready P&L, intercompany elimination, slide logic checker, executive one-pager, assumption sensitivity heat map), with a review checklist for each. Use for finance reporting and board-pack work.
---

# Best prompts for Excel and PPT (10)

Source: an infographic by Nicolas Boucher (Batch 118). Quoted verbatim; replace the [BRACKETS]. "Run these inside Excel or PowerPoint with Copilot or Claude, so the assistant can edit your file directly."

| # | Name | Prompt (verbatim) | Check before you trust it |
|---|---|---|---|
| 1 | Waterfall chart builder | Build a waterfall chart in a new sheet showing the bridge from [START VALUE] to [END VALUE]. Bars for: [DRIVER 1], [DRIVER 2], [DRIVER 3]. Color positive bars [COLOR] and negative bars [COLOR]. | Drivers sum exactly to end minus start; add a check cell |
| 2 | Rolling 12-month dashboard | Build a rolling 12-month dashboard on a new tab. Pull revenue, gross margin %, EBITDA, and headcount from the data in [SHEET NAME]. Update automatically as I add new months to the source data. | Test by adding a month; confirm ranges roll and margin % is recomputed, not averaged |
| 3 | Data validation checker | Scan the '[SHEET NAME]' tab for cells that violate data validation rules. List the cell address, the expected format, and what is currently there. Group by column. | Spot-check five flagged and five unflagged cells |
| 4 | Three-way match formula | Build formulas to match PO numbers in [SHEET 1] to invoice numbers in [SHEET 2] to payment references in [SHEET 3]. Flag every row where the amounts do not match within [TOLERANCE]. | State the tolerance and currency; test with a known mismatch and a missing key |
| 5 | KPI scorecard builder | Build a KPI scorecard tab with [NUMBER] metrics. For each: actual, target, variance, variance %, and a RAG status (red/amber/green based on [THRESHOLDS]). Pull actuals from [SHEET NAME]. | Define whether "lower is better" per metric; check division by zero |
| 6 | Board-ready P&L formatter | Reformat the raw P&L in [SHEET NAME] to match the board template layout. Apply currency formatting, freeze the header row, bold the subtotals, and add a print area for A4 landscape. | Totals unchanged before and after; print preview |
| 7 | Intercompany elimination helper | In [SHEET NAME], identify all intercompany transactions between [ENTITY 1] and [ENTITY 2]. Sum the balances and build elimination entries in a new tab with debit, credit, account, and entity columns. | Debits equal credits; an accountant reviews before posting |
| 8 | Slide logic checker | Review the slide deck attached. For each slide, confirm: does the title match the content, is there one clear message, and is the data traceable to a named source? Flag every gap. | It lists gaps; you decide the fixes |
| 9 | Executive one-pager builder | Build a one-page summary slide for [TOPIC]. Include: headline number, 3 key drivers, 1 risk, and 1 recommendation. All in under [X] words. Board-ready format. | Headline number ties to the model; word count met |
| 10 | Assumption sensitivity summary | Build a summary table showing how [OUTPUT METRIC] changes when [ASSUMPTION 1] moves from [LOW] to [HIGH] and [ASSUMPTION 2] moves from [LOW] to [HIGH]. Format as a heat map with green/red shading. | Recompute two corners by hand; confirm the table is formulas, not pasted values |

## Rules (added)
- **Work on a copy.** An assistant that edits your file directly can overwrite formulas; keep the original and use version history.
- **Formulas, not pasted values.** Ask for live formulas and named ranges so the file stays auditable.
- **Do not paste confidential or personal data** into an assistant your organisation has not approved.
- **Tie out.** Totals before and after, sums of drivers, debits equal credits, headline equals model.
- **Financial and accounting outputs (3, 4, 6, 7) need a qualified human review** before they reach a board or an auditor; the assistant can be confidently wrong.

## Related
`xlsx`, `pptx`, `board-dashboard-3-statement`, `finance-ai-prompts`, `kpi-scorecard`, `finance:variance-analysis`, `finance:reconciliation`, `financial-analysis:audit-xls`. Run one with `/excel-ppt-prompt <1-10> <details>`.
