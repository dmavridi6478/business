---
description: Grill a plan or decision in rounds over a design tree - all unblocked questions per round, each with a recommended answer (Matt Pocock's grilling skill)
argument-hint: <the plan, decision or idea to stress-test>
---

Use the skill `grilling` (vendored from mattpocock/skills, MIT). Input: "$ARGUMENTS".

Follow the skill exactly: build the design tree, ask every currently unblocked question in one numbered round with a recommended answer, wait, recompute the frontier, repeat. Look up facts yourself; ask the user only for decisions. Do not act on the plan until the user confirms shared understanding. For the one-question-at-a-time variant use `/grill-me`.
