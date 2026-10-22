---
name: excel-data-model-blueprint
description: The "Excel Data Model" infographic (Daily Excel Tricks) as a step list for loading tables into the Excel data model through Power Pivot or Power Query, building relationships, DAX measures and PivotTables over several sources, with notes on edition limits and when it replaces VLOOKUP. Use when a workbook needs more than one table.
---

# Excel's Data Model, the blueprint (Daily Excel Tricks infographic)

## Concept
A **Data Model** is a relational engine inside the workbook: several tables (for example Sales, Products, Customers) joined by relationships, queried by PivotTables and DAX measures. The graphic says it "replaces complex formulas" such as VLOOKUP and INDEX/MATCH for multi-table analysis.

## Two ways in
1. **Add tables**: format each range as a Table, go to Power Pivot, choose **Add to Data Model**.
2. **Load via queries**: Get Data (Power Query), Transform and Load To..., choose **Connection only** and tick **Add this data to the Data Model**.

## Core capabilities on the graphic
- Create relationships between tables (one-to-many on a key).
- Build DAX measures, for example `[Total Sales] = SUM(Sales[Amount])`.
- Use multiple data sources in one model (Excel, SQL, files, web).
- Customize PivotTable behaviour and formatting (sort, filter, custom).
- Analyze very large datasets efficiently (millions of rows).

## Cautions
- **[Certain]** The graphic repeats the "customize PivotTable behavior" card twice; treat it as one capability.
- **[Likely]** Power Pivot and the full Data Model are not available in every Excel edition (check yours); Excel for the web has limits.
- **[Likely]** The Data Model replaces lookups only for pivot-style analysis; row-level formulas on a single sheet still use XLOOKUP. See `lookup-functions-vlookup-hlookup-xlookup`, `excel-pivot-tables-finance`.
- Check each relationship's key for duplicates, otherwise measures double count.
