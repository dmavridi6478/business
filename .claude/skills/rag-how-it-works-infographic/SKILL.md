---
name: rag-how-it-works-infographic
description: The "How RAG works" animated infographic (retrieval augmented generation) as a step list covering indexing, embedding, vector database, retriever, generator and the with and without RAG example, with practical failure modes. Use as a one-page explainer beside rag-pipeline-architecture and rag-implementation.
---

# How RAG works (animated infographic)

Source: an animated GIF with two panels. Frames were read; the animation only highlights the flow.

## Panel 1, the pipeline
- **Indexing:** a database is passed through an **embedding model** to make **vectors**, which are indexed into a **vector database** (with an endpoint).
- **1 Retriever:** the user's **text query** becomes a **vector embedding**, then a **similarity search** returns the closest chunks.
- **2 Generator:** the query plus the **extracted context** go to the **language model**, which writes the **search output**.

## Panel 2, the worked example
- Query: why OpenAI's CEO was dismissed and rehired in days (a past news event).
- **Without RAG:** the model says it cannot comment on future events and lacks the information.
- **With RAG:** documents are chunked and embedded, three relevant chunks are retrieved, combined with the question into one prompt ("Combine context and prompts"), and the model answers from them.

## What the graphic leaves out
- **[Certain]** Chunk size, overlap and embedding choice decide whether the right chunk is found; most RAG failures are retrieval failures, not generation failures.
- **[Likely]** The model can still ignore or misread the retrieved chunks; ask for quotes and source IDs.
- **[Likely]** Retrieved text can carry prompt-injection instructions; treat it as data (see `prompt-injection-defense`).
- Build with `rag-pipeline-architecture`, `rag-implementation`, `embedding-strategies`, `vector-index-tuning`, `hybrid-search-implementation`.
