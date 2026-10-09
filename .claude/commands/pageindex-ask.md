---
description: Ask questions of a long PDF with PageIndex (vectorless, reasoning-based RAG) and verify every answer against the cited pages.
argument-hint: <path-to-pdf> "<question>"
---

Document: $1 · Question: $2

Use the `pageindex` skill (`.claude/skills/pageindex/SKILL.md`).

1. **Data gate.** Before indexing, ask me whether this document may be sent to a third-party LLM provider (confidential, patient, client or unpublished material needs an explicit yes). If no, stop and suggest a local model or the vendor's VPC option.
2. Confirm `pip show pageindex` works and that an LLM key is present in the environment (never print it, never write it to a file). If not, give me the install/key steps and stop.
3. Index the PDF in local mode and ask the question. If the PDF is scanned (no text layer), say so and suggest OCR first — do not proceed with garbage.
4. Return: the answer, then **every cited page/node** with a short verbatim quote from the PDF.
5. Open the cited pages yourself and check the answer against them. State "verified" or list the mismatch. Never present an answer you could not trace to a page.
6. End with: tokens/cost if available, and anything the index could not see (tables rendered as images, figures).
