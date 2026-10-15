---
description: Grill a plan in rounds and, as terms and decisions settle, write them into GLOSSARY.md and docs/adr/ (grilling + domain-modeling skills)
argument-hint: <the plan or design to sharpen>
---

Use the skills `grilling` and `domain-modeling` together (both vendored from mattpocock/skills, MIT). Input: "$ARGUMENTS".

Run the grilling rounds. Whenever a term is resolved, update `GLOSSARY.md` immediately (glossary only, no implementation detail); offer an ADR only when the decision is hard to reverse, surprising without context, and a real trade-off. Create files lazily. Show the user each file change before moving on.
