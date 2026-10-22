---
name: copilot-excel-10-prompts
description: The ten best prompts for Copilot for Excel from a graphic curated by Nicolas Boucher (sales trends, CAGR formula, forecast chart, anomalies, 3-year financial model, formula explanation, data validation errors, cash flow review, AR reconciliation, Python churn analysis) as plain text with sheet and column placeholders, plus notes on running them in Claude or Copilot. Use when analysing a workbook with an AI assistant.
---

# 10 best prompts for Copilot for Excel (graphic by Nicolas Boucher)

Source: one graphic with ten numbered titles and prompts. The sheet and column names in the prompts are examples; replace them with your own. They work for Microsoft Copilot in Excel and, with the data pasted or the workbook attached, for Claude. Check every formula and number Claude or Copilot returns; neither is audited software.

1. **Identify key sales trends**: "Analyze the sales data in columns A (Date), B (ProductCategory), and C (Revenue) from Sheet1. Identify and summarize the key sales trends observed over the last 12 months."
2. **Suggest formula for a financial metric**: "I have annual revenue figures in cells B2:B10, representing revenue from Year 1 to Year 9. Suggest an Excel formula to calculate the Compound Annual Growth Rate (CAGR) for this period and place it in cell C1."
3. **Create a forecast chart from historical data**: "Based on the historical monthly expense data in columns A (Month) and B (Expenses) on 'ExpenseSheet', create a forecast chart projecting expenses for the next 6 months."
4. **Highlight data anomalies or outliers**: "Review the 'Transaction_Log' sheet, specifically the 'Amount' column (D2:D500). Highlight any transactions that appear to be significant anomalies or outliers compared to the average transaction value."
5. **Assist in building a financial model**: "Help me build a 3-year profitability projection model in a new sheet. I need input cells for: Year 1 Revenue, Annual Revenue Growth Rate (%), COGS as % of Revenue, and Fixed Operating Expenses. The model should output: Revenue, COGS, Gross Profit, Operating Expenses, and Net Profit for each of the 3 years."
6. **Explain an existing Excel formula**: "Explain the formula currently in cell H25 on the 'ValuationModel' sheet. What does it calculate, and how do the different parts of the formula contribute to the result?"
7. **Identify data validation errors**: "Scan the active worksheet for any cells that currently violate data validation rules. List the cell addresses and the nature of the validation error for each."
8. **Analyze a cash flow statement for issues**: "Analyze the data in the 'Monthly_CF_Statement' sheet, which contains columns for Operating Cash Flow, Investing Cash Flow, and Financing Cash Flow for the last 24 months. Identify any concerning trends or potential cash flow issues."
9. **Assist with data reconciliation**: "I have an 'AR_Ledger' sheet with columns 'InvoiceID', 'Customer', 'Amount' and a 'Bank_Receipts' sheet with 'TransactionID', 'Payer', 'ReceivedAmount'. Help me identify invoices in 'AR_Ledger' that have a matching payment in 'Bank_Receipts' by comparing 'InvoiceID' with 'TransactionID' and 'Amount' with 'ReceivedAmount'. Highlight unmatched AR items."
10. **Generate Python code in Excel for analysis**: "Using Python in Excel, analyze the customer churn data in table 'CustomerData'. Calculate the monthly churn rate and visualize it as a line chart."

## Notes
- **[Certain]** Prompt 4 "outliers compared to the average" is weak for skewed data; ask for median and IQR, or a z-score with the threshold stated.
- **[Likely]** Prompt 3 forecasts from raw history without checking seasonality; ask the tool to state the method and the error range.
- **[Likely]** Prompt 9 matching on amount as well as ID will miss partial payments; add "list partial and duplicate payments separately".
- For rule-based formatting see `excel-conditional-formatting-cheatsheet`, for lookups `lookup-functions-vlookup-hlookup-xlookup`, and for pivots `excel-pivot-tables-finance`. Run one with `/copilot-excel-prompt <1-10>`.
