---
name: revops-vs-gtm-who-owns-the-crm
description: The "RevOps vs GTM, who owns the CRM" graphic by Guerlain Nerestan comparing how a revenue operations team and a go-to-market team work (trigger to done, stack, alerts, what they build, scorecard) with the tools named for each side and the shared MCP layer. Use to split ownership and metrics between RevOps and GTM engineering.
---

# RevOps vs GTM, who owns the CRM (Guerlain Nerestan graphic)

Source: one infographic, "where the work splits, and where it collides". Opinion graphic; no data behind it.

| Dimension | RevOps | GTM |
|---|---|---|
| 1 Trigger to done | Starts with a record change; ends with a clean, routed record; changes with sign-off; breaks when a rep skips a field | Starts with a buying signal; ends with a live sequence; tweaked every week; breaks when data goes stale |
| 2 Stack | Default, Salesforce, Fivetran, BigQuery, HubSpot, Ergo, DealHub, Omni, QuotaPath, Zapier | Exa, UserGems, Vector, Clay, FullEnrich, Octave, Unify, Instantly, Gojiberry, n8n |
| Shared layer | MCP: "every tool, one agent" | same |
| 3 What pings them | #revops-help: forecast won't tie out, deal stuck 45 days, lead sent to wrong rep | #outbound-alerts: bounce rate over 5%, inbox flagged as spam, signal feed went quiet |
| 4 What they build | A pipeline with gates: lead matched, rep routed, stage checked, forecast rolled up | A weekly loop: signal, enrich, write, send |
| 5 Scorecard | Forecast variance; speed-to-lead; pipeline coverage; close-date slippage | Positive reply rate; signal-to-meeting rate; cost per meeting; inbox placement |

## How to use it
- Give each side one owner and its four metrics; put the CRM field list under RevOps change control, and let GTM write only to named fields or a staging object.
- **[Likely]** Collisions happen at enrichment writes: GTM tools overwrite fields RevOps relies on; add a source and timestamp per field.
- **[Certain]** Spam and bounce metrics on the GTM side (bounce over 5%) are deliverability limits; breaching them harms the sending domain for the whole company.
- Related: `revops`, `gtm-6-levels-growth-today`, `gtm-2026-then-vs-now-stack`, `gtm-outbound-engine`.
