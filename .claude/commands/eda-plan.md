---
description: Plan an exploratory data analysis of a dataset in the five MLTUT steps and write runnable pandas/seaborn code for your columns - plans and code only, runs nothing on data you have not provided
argument-hint: [what the dataset is, its columns, and the question you want answered]
---

Input: "$ARGUMENTS". If empty, ask for the dataset, its columns and the question.

Use `.claude/skills/eda-cheat-sheet-mltut/SKILL.md`.

1. State what one row represents and the question. Flag personal data and ask before any column such as income or gender is plotted or shared.
2. Give the five steps for these columns: understanding (shape, types, missing, duplicates), univariate, bivariate, multivariate, reporting.
3. Write the code with the user's column names; separate cleaning from the final save.
4. Name the likely traps: outliers, leakage, small samples, collinearity, causal claims.
5. Run code only on a file the user gave you. End with `Not checked:` for anything not seen in the data.
