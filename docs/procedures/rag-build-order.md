# Procedure: RAG Build Order

## When this applies

Building or debugging a Retrieval-Augmented Generation (RAG) system.
Backs the `rag-pipeline-architecture` skill's core discipline: write the
index first, then read evidence — don't build or debug the query pipeline
against an unfinished or unvalidated index.

## Steps

1. **Build the indexing pipeline completely before touching the query
   pipeline.** Ingest the real source documents, chunk them, embed the
   chunks, and load them into the vector DB. Don't start wiring up the
   question → answer path until this exists end to end.

2. **Validate the index before querying it.** Spot-check a sample of
   actual chunks: do they read as coherent, self-contained units? Is
   important content split awkwardly across chunk boundaries? Fixing
   chunking after the query pipeline is built means re-validating
   everything downstream too — cheaper to catch it now.

3. **Only then build the query pipeline**: embed the question with the
   *same* embedding approach used for indexing, run similarity search,
   and select top-K chunks.

4. **Test retrieval in isolation before adding generation.** For a set of
   known questions with known correct source chunks, confirm the search
   step actually returns those chunks in the top-K. If retrieval alone
   isn't returning the right evidence, no amount of prompt engineering on
   the generation side will fix it — diagnose and fix retrieval before
   layering an LLM on top of it.

5. **Add the augment + generate step last.** Build the prompt (context +
   ask), send to the LLM, and check that the answer actually cites/uses
   the retrieved evidence rather than answering from the model's own
   training knowledge. An answer that ignores the retrieved context is a
   generation-layer bug, not a retrieval bug — diagnose separately from
   step 4.

6. **When answers are wrong, diagnose in this order, not randomly**:
   chunk quality → retrieval quality → generation/grounding. Per
   `rag-pipeline-architecture`'s quality model (chunk quality × retrieval
   quality), a broken multiplier on either factor caps the whole system —
   check the earliest stage first, since a downstream fix can't compensate
   for an upstream failure.

7. **Re-validate the index whenever source documents change materially**,
   not just at initial build — a RAG system's index is a snapshot, and a
   stale index silently degrades retrieval quality without an obvious
   error to signal it.
