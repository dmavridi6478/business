---
name: excel-conditional-formatting-cheatsheet
description: The Daily Excel Tricks conditional formatting cheat sheet (five rule families, eight practical uses, pitfalls and best practices) plus a note that the file named Ultimate Excel Data Cleaning Cheat Sheet actually contains this sheet, so the data cleaning sheet is missing from the upload.
---

# Conditional Formatting cheat sheet

Source: an infographic from "Daily Excel Tricks". **File-name mismatch:** the upload file is named "The Ultimate Excel Data Cleaning Cheat Sheet" but its content is this Conditional Formatting sheet. The data-cleaning sheet was not provided.

## What it is
Cells change how they look based on rules you define (values, text, dates or formulas).

## Rule types
| Family | Rules |
|---|---|
| Value-based | Greater than, less than, between; top or bottom values; above or below average |
| Text-based | Text contains; specific words; blanks and non-blanks |
| Comparison | Duplicate values; unique values |
| Visual scaling | Data bars, colour scales, icon sets |
| Logic-based | Custom formulas that return TRUE or FALSE |

## 8 practical uses
1. Highlight text matches. 2. Highlight values above or below a threshold. 3. Highlight duplicates. 4. Compare budget versus actuals. 5. Highlight top and bottom performers. 6. Rank values from best to worst. 7. Use icons for status. 8. Apply custom formula rules.

## Pitfalls and best practices
Pitfalls: too many colours, too many rules, poor contrast, ignoring rule priority. Best practice: format only when it adds clarity, prefer subtle fills, keep rules simple and intentional, review and clean up rules regularly.

## Formulas that cover most cases (Home, Conditional Formatting, New Rule, Use a formula)
- Overdue: `=AND($D2<TODAY(),$E2<>"Done")`
- Variance over 10 percent: `=ABS($C2-$B2)/$B2>0.1`
- Duplicate in a column: `=COUNTIF($A:$A,$A2)>1`
- Whole row for a status: `=$E2="Blocked"`
Apply to a range that matches the first row of the formula, and anchor columns with `$`.

Practice sheets: `Artifacts/business/pm-roadmap-and-excel-practice.xlsx` (Roadmap and CF Practice tabs). Use `/excel-rule-pick`.
