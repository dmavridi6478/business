---
description: Score an agent you shipped on 7 lines (tracing, golden set, groundedness, red team, alerts, cost/latency, human review) and pick which of the 7 open-source eval/observability repos fits the two weakest lines.
argument-hint: [agent name or repo path]
---

Use the `agent-eval-repos-7` skill for "$ARGUMENTS". Inspect the agent's code/config if a path is given; otherwise ask. Score each line 0-3 and cite the evidence (file, trace, test) - no evidence means 0. Output the total /21, the two weakest lines, and the single smallest next step for each, naming the repo from the skill's decision guide and its install command. Do not install anything without being asked.
