---
name: excel-ppt-prompts-15
description: The 15 "Best Prompts for Excel/PPT tasks" in full plain text - Excel formula lookup, CAGR, explain a formula, scenario planning, workbook audit, DCF, anomaly detection, profitability model, forecast chart, trend summary, presentation outline, slide content, report-to-slide summary, SWOT slide, slide rewrite - with the placeholders each needs and the workbook that implements the numeric ones. Use when someone needs a ready prompt for a spreadsheet or slide task, or wants the finance models built as a real workbook.
---

# Best prompts for Excel and PowerPoint tasks (15)

Source: a Google Sheets screenshot of a prompt library. Replace each [bracket]. The numeric tasks (1, 2, 4, 6, 7, 8, 9) are implemented as formulas in `Artifacts/business/finance-models-starter.xlsx`.

1. Excel Formula Lookup
```
I'm working in Excel with two sheets: one has sales order and order amount, the other has sales orders with customer names and dates. I need a formula to fetch the customer name in the first sheet using sales order as the key. Give me the exact formula and explain how to use it.
```
2. CAGR Formula Builder
```
I have annual revenue figures in [CELL RANGE], representing revenue from [YEAR 1] to [YEAR 2]. Give me the exact Excel formula to calculate Compound Annual Growth Rate (CAGR) for this period, place it in [CELL], and explain how each part of the formula works.
```
3. Explain an Existing Formula
```
Explain the formula currently in cell [CELL] on the '[SHEET NAME]' tab. What does it calculate, and how do the different parts of the formula contribute to the result?
```
4. Scenario Planning Model
```
I'm the finance manager of a [COMPANY TYPE]. Build a scenario planning model for [NUMBER] products with pricing, growth, and churn assumptions. Build this for [TIME PERIOD] with formulas and dynamic assumptions. Add a graph comparing outcomes and include an assumptions tab so I can change variables easily.
```
5. Workbook Audit
```
Scan this workbook for suspicious formulas, inconsistent ranges, or broken links across all tabs. Define suspicious as [e.g. 'formulas referencing deleted sheets, hardcoded values inside formula cells, or ranges that don't match the column header']. Flag anything meeting that bar before I share it with [STAKEHOLDER], listed by severity.
```
6. DCF Model Builder
```
Build a DCF model for a [INDUSTRY] business. Include a [YEARS]-year revenue and cost projection, WACC input, terminal value calculation, and an output cell showing enterprise value. Put all key assumptions on a separate, clearly labeled inputs tab so they're easy to change without touching formulas.
```
7. Anomaly Detector
```
Review the '[SHEET NAME]' tab, specifically the '[COLUMN]' column ([RANGE]). Highlight any transactions more than [X] standard deviations (or [X]%) from the average value, and explain why each flagged item stands out.
```
8. Profitability Model Builder
```
Help me build a [X]-year profitability projection model in a new sheet. Add input cells for Year 1 Revenue, Annual Revenue Growth Rate, COGS as % of Revenue, and Fixed Operating Expenses on a separate assumptions tab so I can adjust them easily. Output Revenue, COGS, Gross Profit, Operating Expenses, and Net Profit for each year.
```
9. Forecast Chart Builder
```
Based on the historical [METRIC] data in columns [A] and [B] on '[SHEET NAME]', create a forecast chart projecting [METRIC] for the next [NUMBER] months.
```
10. Trend Summary
```
Analyze the [METRIC] data in columns [A], [B], and [C] from '[SHEET NAME]'. Identify and summarize the key trends observed over the last [TIME PERIOD].
```
11. Presentation Outline
```
Act as a presentation strategist. Generate a [NUMBER]-slide outline for a presentation titled [TITLE]. The objective is to [OBJECTIVE]. Suggest a slide title and key bullet points for each slide.
```
12. Slide Content Draft
```
Write the content for a PowerPoint slide discussing [TOPIC]. The audience is [AUDIENCE]. Keep it concise, in bullet points (max 5), and highlight [KEY POINTS]. Suggest a relevant chart type to visualize this.
```
13. Report-to-Slide Summarizer
```
Take the following text from our [REPORT TYPE]: [PASTE TEXT]. Summarize this into 3-4 key bullet points suitable for a PowerPoint slide. The tone should be [TONE].
```
14. SWOT Slide Generator
```
Generate content for a PowerPoint slide presenting a SWOT analysis for [ENTITY/PRODUCT]. List 2-3 points for each category (Strengths, Weaknesses, Opportunities, Threats) relevant to its financial viability and market position.
```
15. Slide Rewrite for Impact
```
Rewrite the following PowerPoint slide content to be more concise and impactful for an executive audience. Original content: '[PASTE EXISTING TEXT]'. Focus on direct language and clear takeaways.
```

## Use well
- Prompts 3, 5, 7, 9 and 10 need the real workbook open or attached; without it a model can only guess at your cells.
- For 4, 6 and 8 ask for assumptions on a separate tab and check every formula yourself before sharing; a model that runs is not a model that is right.
- Use `/excel-ppt-prompt [1-15]` to print one with its inputs list.
