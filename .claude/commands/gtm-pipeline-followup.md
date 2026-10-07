---
description: Follow-up and QBR trigger: Pipeline step of the Growth Today Claude GTM set
argument-hint: [inputs, e.g. company name]
---

Run this GTM task (Follow-up and QBR trigger). Connectors needed: HubSpot, Gong, Slack. Use only the connectors that are actually available; for any that are not, say so and continue with pasted data.

Task: Review my open pipeline in HubSpot. Pull the latest Gong call for each deal, flag anything stalled over 14 days, draft a next-step follow-up for each, and update the deal stage in HubSpot. Post a summary of at-risk deals in Slack.

Inputs from the user (replace bracketed items): "$ARGUMENTS".

Rules: show the planned writes (CRM updates, Slack posts, calendar links, email drafts) and wait for approval before doing them; emails are drafts only; never send or contact anyone.
