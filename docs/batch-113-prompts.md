# Batch 109 prompts in plain text (file numbered 113)

Copy and paste. Fill each [bracket]. The 15 Excel and PowerPoint prompts are also in `.claude/skills/excel-ppt-prompts-15/SKILL.md` and, with a Copy button, in `Artifacts/templates/prompt-sheet-green.html`.

## A. Excel and PowerPoint prompts (15) - `/excel-ppt-prompt [1-15]`
1. I'm working in Excel with two sheets: one has sales order and order amount, the other has sales orders with customer names and dates. I need a formula to fetch the customer name in the first sheet using sales order as the key. Give me the exact formula and explain how to use it.
2. I have annual revenue figures in [CELL RANGE], representing revenue from [YEAR 1] to [YEAR 2]. Give me the exact Excel formula to calculate Compound Annual Growth Rate (CAGR) for this period, place it in [CELL], and explain how each part of the formula works.
3. Explain the formula currently in cell [CELL] on the '[SHEET NAME]' tab. What does it calculate, and how do the different parts of the formula contribute to the result?
4. I'm the finance manager of a [COMPANY TYPE]. Build a scenario planning model for [NUMBER] products with pricing, growth, and churn assumptions. Build this for [TIME PERIOD] with formulas and dynamic assumptions. Add a graph comparing outcomes and include an assumptions tab so I can change variables easily.
5. Scan this workbook for suspicious formulas, inconsistent ranges, or broken links across all tabs. Define suspicious as [e.g. 'formulas referencing deleted sheets, hardcoded values inside formula cells, or ranges that don't match the column header']. Flag anything meeting that bar before I share it with [STAKEHOLDER], listed by severity.
6. Build a DCF model for a [INDUSTRY] business. Include a [YEARS]-year revenue and cost projection, WACC input, terminal value calculation, and an output cell showing enterprise value. Put all key assumptions on a separate, clearly labeled inputs tab so they're easy to change without touching formulas.
7. Review the '[SHEET NAME]' tab, specifically the '[COLUMN]' column ([RANGE]). Highlight any transactions more than [X] standard deviations (or [X]%) from the average value, and explain why each flagged item stands out.
8. Help me build a [X]-year profitability projection model in a new sheet. Add input cells for Year 1 Revenue, Annual Revenue Growth Rate, COGS as % of Revenue, and Fixed Operating Expenses on a separate assumptions tab so I can adjust them easily. Output Revenue, COGS, Gross Profit, Operating Expenses, and Net Profit for each year.
9. Based on the historical [METRIC] data in columns [A] and [B] on '[SHEET NAME]', create a forecast chart projecting [METRIC] for the next [NUMBER] months.
10. Analyze the [METRIC] data in columns [A], [B], and [C] from '[SHEET NAME]'. Identify and summarize the key trends observed over the last [TIME PERIOD].
11. Act as a presentation strategist. Generate a [NUMBER]-slide outline for a presentation titled [TITLE]. The objective is to [OBJECTIVE]. Suggest a slide title and key bullet points for each slide.
12. Write the content for a PowerPoint slide discussing [TOPIC]. The audience is [AUDIENCE]. Keep it concise, in bullet points (max 5), and highlight [KEY POINTS]. Suggest a relevant chart type to visualize this.
13. Take the following text from our [REPORT TYPE]: [PASTE TEXT]. Summarize this into 3-4 key bullet points suitable for a PowerPoint slide. The tone should be [TONE].
14. Generate content for a PowerPoint slide presenting a SWOT analysis for [ENTITY/PRODUCT]. List 2-3 points for each category (Strengths, Weaknesses, Opportunities, Threats) relevant to its financial viability and market position.
15. Rewrite the following PowerPoint slide content to be more concise and impactful for an executive audience. Original content: '[PASTE EXISTING TEXT]'. Focus on direct language and clear takeaways.

## B. Command prompts (written by me; the images contain no other prompts)
```
/ai-tool-pick turn webinars into LinkedIn posts for a B2B audience
```
```
/repo-vet volcengine/OpenViking
```
```
/agent-stack-plan an agent that researches competitors weekly, remembers past findings and writes a report; runs on my laptop; used only by me
```
