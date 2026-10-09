---
description: Score URLs or pasted page copy on Gartner's four AEO diagnostic metrics (extractability, entity attribute coverage, citation rate, citation quality) — unmeasurable metrics are marked, not guessed
argument-hint: <entity> <url or pasted copy>
---

Use the `aeo-diagnostic-metrics` skill. Input: "$ARGUMENTS"

1. Confirm the entity and 1–5 URLs (fetch them with the fetch skill or WebFetch if given; otherwise use pasted copy).
2. Score answer extractability 0–5 per URL with quoted evidence.
3. Build the entity attribute list, then report % coverage per URL.
4. Citation rate and quality: measure only with a supplied prompt set and real citations. Otherwise print the prompt-set template and write NOT MEASURED.
5. Give a scorecard, five prioritised fixes and an explicit "not measured" list.
