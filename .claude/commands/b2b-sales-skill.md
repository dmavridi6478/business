---
description: Run one of the 50 B2B sales steps (ICP to expansion) on your deal facts, routed to the right stage and existing skill, as a draft
argument-hint: [stage or skill number/title, and your deal facts]
---

Use the agent `b2b-sales-stage-router` to pick the step, then load the matching full skill `b2b-sales-NN-<slug>` (the 50 are indexed in `b2b-sales-standard` and `claude-skills-b2b-sales-50-map`) and follow it with the shared rules in `b2b-sales-standard`. Input: "$ARGUMENTS".

If no stage or facts are given, show the seven stages and ask. Support every claim with a line the user pasted, or mark it "assumption". Do not draft anything to send without saying it needs approval.
