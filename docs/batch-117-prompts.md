# Batch 117 prompts (plain text; replace [brackets])

## Choose an analytics tool (`/analytics-tool-pick`)
Our team is [SIZE], our data lives in [WAREHOUSE / SPREADSHEETS / CRM], the people who will use it are [ROLES], and the data is [SENSITIVITY]. From Power BI Copilot, Tableau Pulse, ThoughtSpot, Julius AI, Domo, Omni, Looker, Sisense, Zoho Analytics and Polymer, recommend one primary and one fallback, say what must exist first (data model or semantic layer), list the data-protection questions to ask the vendor, and give a two-week trial with ten questions whose answers I can check against SQL.

## Check an AI analytics answer
You answered: [ANSWER]. Show the exact query or steps used, the definition of each metric, the date range and filters, and the row counts. Then give me three ways this could be wrong (join fan-out, double counting, wrong definition) and one query to test each.

## Metric definitions for a semantic layer
Write official definitions for [REVENUE, CHURN, LTV, ARR] for [COMPANY TYPE]: formula, source table and column, inclusion and exclusion rules, time grain, owner, and the version number. Mark any definition that needs a decision from finance.

## Operations stack (`/ops-stack-pick`)
Business: [TYPE, SIZE, COUNTRY, BUDGET]. Choose one tool each for docs and knowledge, automation, contracts and money, and meetings. For each: why, the consent or data-protection rule, the approval step, and what to automate first. Note that the source list is published by one of its own vendors.

## Explain attention (`/attention-demo`)
Explain how attention is trained using the 16-line numpy script from the part-31 video, at [BEGINNER / INTERMEDIATE] level. Use query, key and value, show how training moves the query of "it" toward pet keys, and state three things the script simplifies compared with a real transformer.
