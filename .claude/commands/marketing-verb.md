---
description: Run one of the 50 marketing verbs (RESEARCH, HOOK, DEDUPE, DISPROVE ...) with the verb contract - source, output format, check
argument-hint: <VERB> [what to apply it to] | menu
---

Use the `claude-marketing-50-verbs` skill. Input: "$ARGUMENTS"

1. If the input is empty or "menu", print the 50 verbs grouped by the skill's pairing list and ask which job the user needs. Stop.
2. Match the first word to a verb row. If none matches, name the 3 closest verbs and ask.
3. Ask ONE batched question for any missing contract part: source data, output format, check.
4. Run the verb using its prompt starter. Report counts of rows or sources read. Mark every inferred item "inferred".
5. Keep anything outward-facing as a draft; do not send or publish.
