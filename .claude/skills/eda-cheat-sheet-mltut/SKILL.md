---
name: eda-cheat-sheet-mltut
description: The two-page MLTUT infographic "Exploratory Data Analysis (EDA)" turned into a working method - the five steps (data understanding, univariate, bivariate, multivariate, insights and reporting), the statistics and charts for each, the page's pandas/seaborn code made runnable, and the checks the sheet omits (missing values, duplicates, outliers, leakage, sample size, correlation is not causation, privacy). Use when starting analysis of a new CSV, teaching EDA, or asking an agent to explore a dataset before modelling.
---

# Exploratory data analysis, five steps

Source: one two-page infographic credited "Created by MLTUT": a flow of five stages and a code page. The stages, measures and chart names below are the sheet's; the "Add" column and the checks are mine.

| Step | Sheet says | Measures and charts | I would add |
|---|---|---|---|
| 1. Data understanding | Summary, info, data types | `head()`, `info()`, `describe()` | Row and column counts, missing values per column, duplicate rows, units, what one row represents |
| 2. Univariate | Distributions, statistics | Mean, median, mode; variance, standard deviation, IQR; skewness, kurtosis; histogram, box plot, bar chart | Outliers by IQR rule, rare categories, impossible values |
| 3. Bivariate | Relationships, correlations | Scatter plot, correlation | Spearman for non-linear data; group comparisons; confounders |
| 4. Multivariate | Patterns, interactions | Correlation heatmap, pair plot | Collinearity before modelling; pair plots get unreadable beyond about 8 columns |
| 5. Insights and reporting | Conclusions, visualisations | Key numbers, saved clean data | State the question first; list limits; do not claim causes |

## The sheet's code, made runnable

The sheet assumes columns `age`, `income` and `gender` in `data.csv`. Replace them with your own.

```python
import pandas as pd, numpy as np, seaborn as sns, matplotlib.pyplot as plt
df = pd.read_csv("data.csv")

# 1. understanding
print(df.head()); df.info(); print(df.describe(include="all"))
print(df.isna().sum()); print("duplicates:", df.duplicated().sum())

# 2. univariate
sns.histplot(df["age"], kde=True, bins=30); plt.show()
sns.countplot(x="gender", data=df); plt.show()

# 3. bivariate
sns.scatterplot(x="age", y="income", hue="gender", data=df); plt.show()
corr = df.select_dtypes(include=np.number).corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f"); plt.show()

# 4. multivariate
sns.pairplot(df.select_dtypes(include=np.number)); plt.show()
sns.boxplot(x="gender", y="income", data=df); plt.show()

# 5. report
print("Average age:", df["age"].mean())
print("Age-income correlation:", df[["age", "income"]].corr().iloc[0, 1])
print("Most common gender:", df["gender"].mode()[0])
```

Notes on the sheet's code: it calls `plt.show()` after every plot, which blocks in scripts; the closing `to_csv('cleaned_data.csv')` writes data you have not cleaned, so clean first or rename the file. I did not run this against a dataset.

## Checks the sheet leaves out

- **Leakage:** a column that encodes the answer makes any later model look great.
- **Sample size and bias:** how were the rows collected, who is missing?
- **Privacy:** a column such as gender or income is personal data; share only aggregates and follow the rules that apply to you.
- **Correlation is not causation.** A heatmap shows association only.

## Use

`/eda-plan [dataset description]` writes the plan and the code for your columns without running anything on data you have not provided. Related: `data-storytelling`, `claude-data-use-cases`, `python-patterns`.
