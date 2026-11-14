# Batch 113 prompts (files numbered 117)

Plain text. Nothing here installs, runs or publishes anything.

## 1. Plan an exploratory data analysis

```
Dataset: [what one row represents]. Columns: [list]. Question: [what I want to learn].
Plan an exploratory data analysis in five steps: data understanding (shape, types, missing values, duplicates), univariate (distributions, mean/median/mode, variance, IQR, skewness), bivariate (scatter, correlation), multivariate (heatmap, pair plot), and a short report. Write pandas and seaborn code with my column names. Flag personal data, outliers, leakage and small samples, and say which claims the data cannot support. Do not run anything on data I have not provided.
```

Command: `/eda-plan [dataset, columns, question]`.

## 2. Judge a "too good to be free" repo claim

```
Repo: [owner/name]. The post claims: "[claim]". Read the README and licence. Tell me what is true, what the claim leaves out (hardware, disk, time, coverage), what it replaces and what it does not, and the risk of running it. Do not install anything.
```

Example finding: kimi-k3-in-c does run in 8.24 GB of RAM, but needs a 1.56 TB checkpoint on disk and streams it each step at small RAM sizes, so it is slow.

## 3. Try a free local AWS emulator safely (Floci)

```
I use Docker and test against AWS. Read the Floci README and list: the services it covers, the port, how to point the AWS CLI and my test suite at http://localhost:4566, and which of my services are not covered. Give me a docker compose file, but do not start anything.
```
