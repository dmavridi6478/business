---
description: Audit CLAUDE.md size, enabled connectors, scheduled tasks and attachments against the 22 token-saving rules and report PASS / FAIL / CANNOT MEASURE
argument-hint: [optional: path to a CLAUDE.md, default ./CLAUDE.md]
---

Use the `claude-token-rules-22` skill. Target: "$ARGUMENTS" (default: ./CLAUDE.md)

1. Run `wc -w` and `wc -l` on the target. Pass = ≤ 2,000 words and ≤ 200 lines. Show the numbers and the margin.
2. List connectors enabled in this session (ListConnectors) and flag any unused for the stated task.
3. List scheduled routines (list_triggers) and flag any firing more often than daily.
4. Tell the user which rules cannot be measured from here (chat habits, effort setting, model choice).
5. Output a table: rule number, PASS/FAIL/CANNOT MEASURE, evidence. No invented token counts.
