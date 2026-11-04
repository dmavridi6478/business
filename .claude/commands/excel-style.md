---
description: Format a tracker to match your spreadsheet style: apply a style guide of fonts, colours, number formats and structure
argument-hint: [the file path or pasted table, and your style rules or a reference sheet]
---

Input: $ARGUMENTS

Use the `xlsx` skill.

1. If I gave a reference sheet, extract its rules (fonts, header fill, number and date formats, column widths, freeze panes, validation). If not, ask for them or propose a plain default and wait.
2. Apply them to the tracker without changing any value or formula. Keep formulas live; fix only formatting.
3. Report what changed and anything you could not match. Save to a new file, never over the original.
