---
description: Write a jq filter for a JSON task, run it on your sample, and show the command with its real output
argument-hint: [what you want from the JSON] [path to a sample file, or paste a sample]
---

Use the skill `jq-json-cookbook`. Input: "$ARGUMENTS".

1. Read `.claude/skills/jq-json-cookbook/SKILL.md` and run `jq --version`.
2. If no sample is given, ask for one; do not invent the structure.
3. Write the filter, run it on the sample, and show the exact command and the real output. If it fails, show the error and fix it; never present an untested filter.
4. Pass any user value with `--arg`, never by string concatenation. State the assumptions (field names, null handling).
