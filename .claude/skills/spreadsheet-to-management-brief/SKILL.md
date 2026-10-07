---
name: spreadsheet-to-management-brief
description: Turn a spreadsheet into a one-page management brief with two prompts, a second-pass test and five checks (@earchoe 9-slide series); also how to sell it as a monthly reporting pack.
---

# Spreadsheet to management brief
Rule: AI is the accelerator. Your source, judgement and verification create the value. Flow: INPUT (real source + context) -> THINK (structure, compare, test) -> OUTPUT (useful work product) -> VERIFY (human check before action).

Give the model: the business question, time period, metric definitions, the sheet with clear column names. Vague input gives vague output.

**Prompt 1 - movement detection**
Analyse this spreadsheet for the question: [BUSINESS QUESTION]. First describe the columns and identify missing, duplicated or suspicious values. Then calculate the metrics that answer the question. Show the formulas or logic used. Do not silently change the data.

**Prompt 2 - management brief**
Create a one-page management brief: headline finding -> supporting numbers -> trend or comparison -> possible explanations -> risks -> recommended next checks. Label correlation as correlation. Do not claim causation unless the data supports it.

**Second pass (test the numbers):** ask what it assumed; ask what is missing; ask it to attack its own answer (weak claims, contradictions, edge cases); verify facts, figures, policies, prices.

**Five checks:** define the business question; inspect the data before interpreting; show calculation logic; validate surprising numbers; separate evidence from explanation.

**Offer:** monthly reporting packs for small businesses: raw spreadsheet -> cleaned checks -> KPI summary -> decision brief. Sell a defined result, a repeatable process and a clear quality check - not "I know how to prompt AI". See `data-cleanup-brief-service`.
