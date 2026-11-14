---
description: Produce a build sheet for one of the 8 AI automation blueprints (voice agent, lead gen, UGC spy, faceless video, content agent, FAQ bot, YouTube ideas, avatar) on n8n or Make.com
argument-hint: [blueprint number or name] [n8n | make]
---

Use the `ai-automation-blueprints` skill. Build target: "$ARGUMENTS".

If no blueprint is named, show the pick-order table and ask which one. If no platform is named, default to n8n.

Produce a build sheet with these sections, in this order:

1. **Fit check** — two lines: is this blueprint right for my business, and what would I build instead if not. Be direct.
2. **Legal / compliance check** — GDPR, ePrivacy, EU AI Act transparency, platform ToS risks specific to this blueprint. State what must be in place before go-live.
3. **Accounts & credentials** — every account and API key needed, with the paid tier required.
4. **Node map** — numbered table: # | Node | Platform module/node name | Input | Output | Error handling.
5. **AI node prompt** — the system prompt, filled in for my business where you know it, `{{placeholders}}` where you do not.
6. **Human gate** — where a human approval step goes, and why.
7. **Cost estimate** — per 100 runs, split by platform operations vs. API costs. Mark every figure as an estimate and name the pricing page to verify it.
8. **Test plan** — 5-record dry run, spend cap, and the three failure cases to test.
9. **Next step** — if n8n, hand the node map to `n8n-agent-builder` for the JSON skeleton.
