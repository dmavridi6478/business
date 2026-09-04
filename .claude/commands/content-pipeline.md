---
description: Run the 7-role AI content team pipeline (researcher, hook writer, script writer, designer, analyst, manager, publisher) on a content cycle — draft stages run automatically, publishing always stops for explicit approval.
argument-hint: [niche/topic, or "next cycle" to use the last research brief]
---

Given the niche/topic (or existing opportunity) described in "$ARGUMENTS" (ask if not provided):

1. **Research** — run `content-researcher` to produce ranked content opportunities.
2. **Hook** — run `content-hook-writer` on the top opportunity (or the one the user picks, if several were surfaced) to produce ranked hook options.
3. **Script** — run `content-script-writer` on the chosen hook to produce the full script/caption.
4. **Design** — run `content-designer` to specify (and where this repo's design skills support it, produce) the visuals the finished script needs.
5. **Schedule** — run `content-manager` to slot the finished piece into the content calendar.
6. **Stop.** Present the finished piece (script, visuals, proposed schedule slot) and ask explicitly whether to publish, and to which platform/account/time. Do not run `content-publisher` without that explicit go-ahead for this specific piece — a scheduled calendar slot from step 5 is a plan, not authorization.

If `content-analyst` has prior performance data available, have `content-researcher` and `content-hook-writer` check it before generating new opportunities/hooks in steps 1-2, so the pipeline actually learns from what's already worked rather than starting cold every cycle.

Any stage can be run standalone outside this command (e.g. "write a hook for this" invokes just `content-hook-writer`) — this command is for running the full cycle in sequence.
