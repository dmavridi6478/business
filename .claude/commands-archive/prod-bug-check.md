---
description: Review code or a feature against the 5 production-only bugs (race conditions, authorization, N+1 queries, memory leaks, idempotency)
argument-hint: <file path, endpoint, diff or feature description>
---

Use the skill `production-bugs-5`. Target: "$ARGUMENTS".

1. Read `.claude/skills/production-bugs-5/SKILL.md`. If the target is a path or a diff, read it; if it is a feature description, ask for the code or the endpoint list in one short message.
2. For each of the five bugs, answer yes / no / not applicable with the exact line or call that proves it. No guesses: if you cannot see the code path, say "not visible".
3. For each yes, give the smallest fix from the "what to do" column and the test that would catch it (a concurrent-request test, a cross-user access test, a query-count assertion, a repeat-run memory check, a duplicate-request test).
4. Output a table: bug, verdict, evidence, fix, test. Finish with the single highest-risk item to fix first.
