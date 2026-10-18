---
description: Run one of the 10 Copilot for Excel prompts (trends, CAGR, forecast, anomalies, financial model, formula explanation, validation errors, cash flow, AR reconciliation, Python churn) on the workbook or data I give
argument-hint: "[prompt number 1-10] [file or pasted data]"
---

Use the skill `copilot-excel-10-prompts`.

Input: $ARGUMENTS

If no number from 1 to 10 was given, list the ten titles and ask which to run. Otherwise take that prompt, and:
1. Ask me in one short question for the file or pasted data and the real sheet, column or cell names if they differ from the examples; do not invent data.
2. Run it on my data. Show the formulas or code used, the cells they read, and any assumption.
3. Verify the result with a second method (for example a spot check of three rows) and say what you checked.
4. Never overwrite my original sheet; work on a copy or a new sheet.
