---
name: gtm-ops-diagnostic
description: Run the GTM Ops Diagnostic Framework (Union Square Consulting, "the CRO's playbook for diagnosing and prioritising GTM ops for the highest revenue impact") - a 7-step method that scores seven GTM areas against four maturity levels (Fundamentals, Adoption, Optimization, Amplification), colours a heatmap, flags danger zones and turns the reds into a roadmap. Use when revenue is flat or leaky and you need to know which part of the go-to-market engine to fix first, or when auditing pipeline, inbound, outbound, ABM, partners, renewals or expansion.
---

# GTM Ops Diagnostic Framework

Source: Union Square Consulting infographic (Interview Guidelines.zip). The infographic's diagnostic questions are printed too small to read at the resolution supplied, so the **questions below are written for this repo** to fit each area x level cell. The structure, scoring and interpretation rules are the infographic's.

## Step 1 - Understand the efficiency pyramid
Fix from the bottom. You cannot optimise what you do not execute, and you cannot amplify what you have not optimised.

| Level | Meaning |
|---|---|
| **Fundamentals** | The process is defined, documented and owned; ICP and personas exist; people and tools support execution |
| **Adoption** | The team is trained; there is reporting and accountability; management reviews regularly; the process is executed consistently |
| **Optimization** | Ops and management analyse GTM data on a schedule; insight reaches leadership; there is a regular rhythm for decisions |
| **Amplification** | AI-powered forecasting, automated account-health signals, intent-driven prioritisation |

## Step 2 - Pick the focus area (decision tree)
"What improvement will impact revenue most?"
- **New business acquisition** - bottleneck in generating pipeline (Outbound, Inbound, Partner/Channel, ABM/Allbound) or in closing (Pipeline management).
- **Improving net revenue retention** - bottleneck in reducing churn (Renewals) or expanding customers (Expansion).
Then ask where GTM ops can help: people, process or systems.

## Step 3 - Answer the diagnostic questions
Seven areas: **Pipeline Management, Inbound, Outbound, ABM/Allbound, Partners/Channel, Renewals, Expansion** x four levels = 28 cells. Score each cell with the traffic light:
- GREEN - strong yes (we can show the evidence)
- YELLOW - somewhat (it happens for some of the business, or is not consistent)
- RED - no (the process is absent or the question cannot be answered)

Starter question per level (adapt the noun to the area):
1. Fundamentals: "Is there a documented, owned [area] process that the team can find and name?"
2. Adoption: "Do the people who should follow the [area] process follow it, and does a manager inspect it weekly?"
3. Optimization: "Do we review [area] metrics on a fixed cadence and change something because of what they show?"
4. Amplification: "Do we use automation or AI in [area] to prioritise, forecast or trigger action - and have we measured that it helps?"

## Step 4 - Heatmap
Rows = areas, columns = Fundamentals, Adoption, Optimization, Amplification; each cell G/Y/R. Template: `design-templates` > `gtm-heatmap-navy.html`.

## Step 5 - Interpret and prioritise
- Fix **Fundamentals first**: a red here beats any red above it.
- Then Adoption, then Optimization, then Amplification.
- **Danger zones** (the infographic's warning): a Green or Yellow at Optimization or Amplification sitting on a Red or Yellow Fundamentals. Teams buy tools and AI on top of undefined process. If everything is yellow, the usual cause is that nothing has been committed to fully - "dabbling without mastering."

## Step 6 - Roadmap
Turn the reds, in pyramid order, into a dated roadmap: initiative, owner, effort, expected revenue effect, due date. One initiative per red cell; do not schedule more than your team can finish this quarter.

## Step 7 - Integrate planning and metrics
Tie each initiative to a measurable metric (conversion rates, NRR, CAC payback) and a shared cadence: build an annual plan with both top-down and bottom-up targets, and revisit the roadmap quarterly against performance.

## Procedure for Claude
1. Ask for the 7 areas that apply (skip any the business does not run) and one line of evidence per cell. Do not accept "I think so" as green.
2. Score, build the heatmap as a table, list danger zones, order the reds, draft the roadmap.
3. Say plainly what you could not score for lack of evidence. Do not invent metrics.

Command: `/gtm-diagnostic`.

## Keywords
GTM ops, RevOps, diagnostic, heatmap, efficiency pyramid, pipeline, NRR, CRO, Union Square Consulting
