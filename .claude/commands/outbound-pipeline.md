---
description: Run the 5-step outbound pipeline inside Claude Code — enrich, clean, score ICP on signals, personalise 1:1, prepare for sender — with GDPR and human-approval gates
argument-hint: [ICP / target description] or [path to a lead CSV]
---

Use the `gtm-outbound-engine` skill. Target: "$ARGUMENTS"

0. GATES FIRST: confirm with me (a) the lawful basis for processing (EU legitimate-interest test done?), (b) the sending domain is separate from the main domain with SPF/DKIM/DMARC, (c) the daily send cap. Do not proceed without answers.
1. PULL & ENRICH: if I gave an ICP, pull accounts/contacts via the connected prospecting MCP (Clay, Vibe Prospecting or OpenFunnel — check which are authorised). Show the estimated cost before any paid enrichment and wait for my OK. If I gave a CSV, skip to 2.
2. CLEAN: run `python3 .claude/skills/gtm-outbound-engine/scripts/clean_leads.py <in> <out> --report <report>` and show the report. Drop free-mail and invalid rows from the send list.
3. SIGNALS & SCORE: for each account, find one dated trigger signal (hiring, funding, tech change, news) with a source URL. Score with the skill's ICP rubric. Keep Tier A and B only.
4. PERSONALISE: draft a 3-touch sequence per Tier A contact with the skill's step-4 prompt. Every personal line cites its signal. Drafts only.
5. PREPARE FOR SENDER: produce a CSV formatted for [Instantly / Smartlead / Outreach] and a summary: counts per tier, signals found, sample of 3 sequences. Do NOT send. Hand to `outbound-campaign-brief` for my approval and send cap.
