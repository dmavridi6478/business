---
name: lookup-functions-vlookup-hlookup-xlookup
description: VLOOKUP vs HLOOKUP vs XLOOKUP from the "Your CFO Guy" (Josh Aharonoff, 2024) infographic - syntax, arguments, pros and cons for each - plus the traps the graphic leaves out (approximate match is the default, hard-coded column numbers, first-match-only), the INDEX/MATCH fallback, and a practice workbook whose formulas reproduce the graphic's four example results. Use when choosing or writing a spreadsheet lookup.
---

# VLOOKUP vs HLOOKUP vs XLOOKUP

Source: one infographic, "Vlookup vs Hlookup vs Xlookup", (c) Josh Aharonoff 2024, YourCFOGuy.com; its worksheet link (yourcfoguy.com/vlookup-vs-hlookup-vs-xlookup) was not fetched. Transcribed 15 October 2026. Practice file: `Artifacts/business/lookup-functions-practice.xlsx` (formulas written for this repo; recalculated, 0 errors).

Definition on the graphic: a lookup function searches for a value in a table or range and retrieves corresponding information from that location.

| | VLOOKUP | HLOOKUP | XLOOKUP |
|---|---|---|---|
| Syntax | `=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])` | `=HLOOKUP(lookup_value, table_array, row_index_num, [range_lookup])` | `=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])` |
| What it does | Searches the first column of a range and returns a value from the same row | Searches the first row of a range and returns a value from the same column | Searches one array and returns from a matching array or range |
| Pros (graphic) | Easy for vertical lookups; works in every Excel version | Easy for horizontal lookups; works in every version | Searches in any direction; optional default value if no match |
| Cons (graphic) | Vertical only; search column must be first in the range | Horizontal only; inefficient on large datasets | Newer Excel versions only; syntax a bit complex |

`range_lookup`: TRUE (the default) = approximate match, FALSE = exact. XLOOKUP's optional arguments: `if_not_found` (value to return), `match_mode` (exact, less, etc.), `search_mode` (first-to-last or last-to-first).

Example results shown (all reproduced in the practice file): Revenue for Mar-23 = 35,254 (VLOOKUP); COGS for Mar-23 = 5,587 (HLOOKUP); Gross Profit for Mar-23 = 29,667 and Net Income for Apr-23 = 44,722 using one and a nested XLOOKUP.

## What the graphic leaves out

1. **VLOOKUP and HLOOKUP default to approximate match.** Omit the fourth argument on unsorted data and you can get a wrong number with no error. Write `FALSE` (or `0`) every time unless you truly want a sorted-range lookup.
2. **A typed column number breaks silently** when someone inserts a column. Derive it: `MATCH("Mar-23", header_row, 0)` as the third argument (workbook row "column found by MATCH").
3. **First match only.** Duplicate keys return the first row; check keys are unique before trusting any lookup.
4. **Text that looks the same but is not:** trailing spaces, numbers stored as text, dates vs text headers. In the practice file the month headers are text on purpose.
5. **XLOOKUP availability:** Excel for Microsoft 365 and Excel 2021 and later, and Google Sheets. Excel 2019 and earlier do not have it; a file using it shows `#NAME?` there. For shared files with old versions, use **INDEX/MATCH**: `=INDEX(values, MATCH(row_key, row_labels, 0), MATCH(col_key, col_labels, 0))`.
6. **XLOOKUP modes (Excel documentation):** `match_mode` 0 exact (default), -1 exact or next smaller, 1 exact or next larger, 2 wildcard; `search_mode` 1 first-to-last (default), -1 last-to-first, 2 or -2 binary search (sorted data only).
7. **Label oddity in the graphic's table:** its "Net Income" equals Net Operating Income *minus* "Net Other Income" in every month, so that row behaves as other expense. The practice file keeps the printed labels and documents this.

## Picking one

New file, everyone on current Excel or Google Sheets: XLOOKUP. Shared with older Excel, two-way lookups, or lookups left of the key: INDEX/MATCH. VLOOKUP/HLOOKUP only to read or maintain existing models.

**Repo rule:** when building workbooks here that get recalculated with LibreOffice, do not write live XLOOKUP formulas (see the `xlsx` skill); use INDEX/MATCH and show XLOOKUP as text. Use `/lookup-formula`.
