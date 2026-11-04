---
description: Run the weekly GTM loop - signal, enrich, write, send (approval-gated), review - for one segment
argument-hint: <segment or campaign>
---

Use the `gtm-team-roles-revops-boundary` skill. Input: "$ARGUMENTS"

Run Workflow B (GTM weekly loop). Steps 1-3 and 5 are drafts. At step 4 STOP: present the send list, a send cap, bounce-rate and inbox-placement checks, and wait for explicit human approval. Never send. Use gtm-outbound-engine and scripts/clean_leads.py for list cleaning.
