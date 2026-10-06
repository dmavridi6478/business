---
description: 'Choose between plain, Hybrid, Graph, Corrective and Adaptive RAG for a use case using the decision rule - start plain, add a variant only where an evaluation set shows failure.'
argument-hint: '<use case: documents, question types, what goes wrong today>'
---

Use the `rag-variants-compared` skill for "$ARGUMENTS". Ask once for document type and size, typical questions and current failures if missing. Recommend one variant with the reason, the cheapest test that would prove it, and the evaluation set to build first (30 real questions with known answers). Say plainly when plain vector RAG is enough. Note that Adaptive RAG was not drawn in the source video.
