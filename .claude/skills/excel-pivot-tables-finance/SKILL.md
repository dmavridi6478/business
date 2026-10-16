---
name: excel-pivot-tables-finance
description: The 16 PivotTable ribbon features from a BojanFin infographic (Options, Field List, Refresh, Change Data Source, Move, Select, Clear, Fields Items and Sets, Solve Order, PivotChart, Slicer, Timeline, Active Field, Field Settings, Group Selection, Group Field) with what each does and a finance workflow. Use when building or checking a pivot report.
---

# Pivot Tables for Finance (16 features)

Source: one infographic by Bojan Radojicic (BojanFin.com); the footer promotes a paid "Modeling and FP&A Programs: 10h Video, 70+ Sheets". Descriptions below are summarised from the tiles.

| Feature | What it does |
|---|---|
| Options | Opens the PivotTable Options dialog: layout and formatting, totals and filters, display, printing, alt text |
| Field List | Panel to assign fields to Filters, Columns, Rows and Values |
| Refresh | Updates the pivot from the source so analysis reflects the latest data |
| Change Data Source | Expands or changes the source range without rebuilding the pivot |
| Move PivotTable | Relocates the pivot within or to another worksheet |
| Select | Selects the whole pivot, or labels only, or values only, for formatting or copying |
| Clear | Removes fields, filters and resets the pivot to its original state |
| Fields, Items and Sets | Calculated fields, calculated items and named sets for custom summaries |
| Solve Order | Controls the order when several calculated items or fields interact |
| PivotChart | A chart linked to and updated with the pivot |
| Slicer | Clickable filter buttons |
| Timeline | A visual date filter (months, quarters, years) |
| Active Field | Shows the field you have selected |
| Field Settings | Changes the calculation (sum, count, average) and layout of a field |
| Group Selection | Combines selected items into a custom group |
| Group Field | Groups numbers or dates (months, quarters, age ranges) |

## Finance workflow
1. Keep source data as a clean table (one header row, no merged cells, no subtotals); a table range grows with new rows.
2. Rows: account or cost centre; Columns: month; Values: Sum of amount; Timeline for the period.
3. Group dates to quarters, add a slicer for entity or scenario, then a PivotChart.
4. After any data change use Refresh; after adding rows outside a table use Change Data Source.
5. Check the pivot total against a trial balance or `SUMIFS` before sharing. Calculated items can double count; check Solve Order.

Practice: `Artifacts/business/pm-roadmap-and-excel-practice.xlsx` has a small budget-versus-actual table with `SUMIFS` summaries (openpyxl cannot create a real pivot, so build one from that table in Excel).
