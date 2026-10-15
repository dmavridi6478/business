---
description: Choose between VLOOKUP, HLOOKUP, XLOOKUP and INDEX/MATCH for a spreadsheet and write the formula with exact match, a safe column index and a not-found fallback
argument-hint: <what to find, where the table is, Excel version or Google Sheets>
---

Use the skill `lookup-functions-vlookup-hlookup-xlookup`. Input: "$ARGUMENTS".

1. Ask only for what is missing: the key, the table's layout (keys in the first column or first row?), and the spreadsheet app and version.
2. Recommend one function using the skill's picking rule; write the formula with exact match (`FALSE` or `0`), the column or row index derived with `MATCH` rather than typed, and a not-found fallback (`IFERROR` or XLOOKUP's `if_not_found`).
3. Name the traps that apply (duplicate keys, text vs numbers, trailing spaces, older Excel without XLOOKUP).
4. If building a workbook here to be recalculated, follow the `xlsx` skill: INDEX/MATCH live, XLOOKUP only as text. Point to `Artifacts/business/lookup-functions-practice.xlsx` for a worked example.
