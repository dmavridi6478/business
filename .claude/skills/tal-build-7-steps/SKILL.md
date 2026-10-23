---
name: tal-build-7-steps
description: Seven-step workflow for building a target account list (TAL) that goes below the "industry and size" filter - lookalike search from best customers, product tags, company keywords, minimum department headcount, buyer-role presence, a relevance-score cutoff, and email enrichment with a per-company cap. Use when someone builds an outbound list, a 10,000-row export that "looks finished", or asks how to qualify accounts before outreach. Run via /build-tal. Source Jan Rasmussen (arrel.ai) infographic; steps are vendor-neutral, one claim is not.
---

# Build a TAL in 7 steps

Source: "How to Build a TAL in 7 Steps" (Jan Rasmussen, arrel.ai). The graphic contrasts **what everyone does** (filter by industry, headcount 50-200, location, export, get 10,000 rows that look finished) with the workflow below the waterline.

| # | Step | Do this | Check |
|---|---|---|---|
| 1 | Lookalike search | Name your best customers; add their domains as lookalikes; each match gets a relevance score | 5-10 real customers, not aspirational logos |
| 2 | Quick view | Open quick view on a top match and push its product tag into the live search | Tag describes what they buy or build, not their industry |
| 3 | Company keywords | Use keywords, not industry: industry filters read tags too; up to 300 include and exclude terms (tool limit shown) | Exclusions listed (e.g. "brokerage", "lending" in the example) |
| 4 | Department headcount | Require a department that can implement, e.g. IT with at least 5 people | Minimum is justified by who implements your product |
| 5 | Role presence | Filter for the role you sell to, then find people inside those companies | Buyer exists at the account, not just the company |
| 6 | Relevance score | Set your cutoff before you scroll; scores fall as you go (example: 97 on page 1, 90 by page 100) | Cutoff written down; stop at it |
| 7 | Email enrichment | Export with a per-company cap | See caution |

## Caution on step 7

The graphic says emails are verified at export, catch-all addresses are included, and you should not re-verify them. That is the vendor's claim. Catch-all domains accept any address, so an accepted check does not prove a person exists there. [Likely] Send a small test batch, watch bounces, and apply the pre-send gate in `/gtm-weekly-loop` before any volume. Contacts are personal data: record your lawful basis (see `gtm-outbound-engine`).

## How to use with this repo

- Targets and brief: `/icp`, `outbound-campaign-brief`.
- Enrichment and signals: `lead-intelligence`, `gtm-outbound-engine`.
- Outreach drafts: `cold-email`, `/colddm`. Drafts only; the human sends.
- The workflow is also drawn in `Artifacts/operations/workflows-batch-113.html` (workflow 1).
- The tool is a paid product (Arrel). Nothing here requires it; steps 1-6 can be done with any firmographic database that supports lookalikes, keyword filters and headcount by department.
