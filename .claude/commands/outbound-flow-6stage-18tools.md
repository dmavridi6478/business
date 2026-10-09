---
description: Cold IQ's 6-stage, 18-tool outbound flow centered on Claude Code as the campaign-build hub, mapped against this repo's existing outbound skills
argument-hint: [target account list or campaign brief]
---

# Our Full Outbound Flow (6 Stages, 18 Tools)

Source: Cold IQ / Soheil Saeidmehr, "Our full outbound flow — 18 tools, and one place they all report to." A second Cold IQ outbound graphic in this repo (the first is `gtm-outbound-engine`'s 5-layer/14-tool source) — same vendor, a different named tool stack and a different orchestration hub (**Claude Code** here vs. Claude/OpenAI/Cold IQ generically in the earlier one). Both are vendor marketing; treat tool availability/pricing as **[Guessing]** and verify before buying.

## The 6 stages

| # | Stage | Identified tools | Unidentified (icon too small to verify — not guessed) |
|---|---|---|---|
| 1 | Source the accounts | — | 4 icons (yellow/black/blue) — not legible enough to name with confidence |
| 2 | Get the contact data | — | 4 icons (red cube, red heart-shape, black wave, colorful stack) — not legible enough to name with confidence |
| 3 | Build the context | — | 4 icons (purple brackets, black interlock, blue shape, light-blue "S") — not legible enough to name with confidence |
| 4 | Set up the sending infrastructure | Likely HeyReach (orange "H"), Google | 1 blue icon — not legible enough to name with confidence |
| 5 | Build the campaign | **Claude Code** — "copy, sequences, and the load, in one place" | — |
| 6 | Launch it and watch it | **Instantly.ai**, **lemlist** | — |

Per this repo's standing verification discipline (never fabricate a source ID from an illegible icon): stages 1–4 name 14 tools in the source's "18 tools" count, but only Claude Code, likely-HeyReach, Google, Instantly.ai, and lemlist are legible enough to cite by name. The rest are represented here as counts/positions only.

## What the 6 stages map to

Stage 5 (Claude Code as campaign-build hub) is the same architectural claim as `gtm-outbound-engine`'s Orchestration layer and `outbound-sales-system-5stage`'s framing — three separate sources converging on the same idea: **use Claude Code as the single place that reads account/contact/context data and writes the actual outreach copy and sequences**, rather than switching tools mid-build.

| This graphic's stage | This repo's existing skill |
|---|---|
| 1. Source the accounts | `prospecting` (vendored) |
| 2. Get the contact data | `customer-research` (vendored), Clay/Vibe Prospecting MCP (see `gtm-outbound-engine` layer 3) |
| 3. Build the context | `customer-research`, OpenFunnel `deep-research` (see `gtm-outbound-engine` layer 2 for signal sourcing) |
| 4. Set up sending infrastructure | Not currently connected in this account — export and import manually (same gap `gtm-outbound-engine` layer 4 already flags) |
| 5. Build the campaign | Claude Code itself, running `cold-email` (vendored) + the Step 4 prompt in `outbound-sales-system-5stage` |
| 6. Launch and watch | Instantly.ai / lemlist — not connected; `revops` (vendored) for the pipeline-review step once replies come back |

## Plain-text prompt to run stage 5 (the one every source agrees Claude Code owns)

```
Build the outbound campaign for [TARGET SEGMENT / OFFER] in one place:
given this account list [PASTE], this contact data [PASTE], and this
context/signal research [PASTE], write the full first-touch sequence
(3 touches) and organize it as copy + send schedule ready to hand to a
sending tool. Do not invent any personalization not present in the
pasted context.
```

## Gates

Same gates as `gtm-outbound-engine`: lawful basis before sourcing/contacting (GDPR/ePrivacy), human approval before stage 6 launch, deliverability hygiene (SPF/DKIM/DMARC, warm-up, send caps) before volume.

## Related

`gtm-outbound-engine`, `outbound-sales-system-5stage`, `outbound-campaign-brief`, `outbound-pipeline`.
