---
name: rag-variants-compared
description: 'Plain comparison of Hybrid RAG, Graph RAG, Corrective RAG and Adaptive RAG - pipeline stages, when each fits, cost and failure modes - with a decision rule for choosing one. Use when the user designs a retrieval-augmented assistant over documents, asks which RAG type to use, or reviews a RAG pipeline. Source: "Hybrid RAG vs Corrective RAG vs Adaptive RAG" video infographic (@shiva.bytes, Sivasankar Natarajan).'
---

# RAG variants compared

The source is an 11-second infographic video with three visible panels (Hybrid, Graph, Corrective). **Adaptive RAG is in the title but has no panel**, so its row below is general knowledge, not from the video.

| Variant | Pipeline as drawn in the video | Idea | Use when | Main risk |
|---|---|---|---|---|
| Hybrid RAG | External sources -> graph generator -> user query -> graph DB (context 2) -> vectorisation -> vector DB -> prompt enhancement -> response generator -> output | Merge different retrieval methods (here graph + vector) so answers are accurate and context-rich | Questions mix exact terms and meaning; documents have entities and links | Two indexes to build and keep in sync |
| Graph RAG | Same stages with the graph DB as the knowledge store | Organise knowledge as graph structures, enabling multi-agent workflows with memory and parallel execution | Multi-hop questions ("which suppliers share a director?") | Graph extraction is costly and can be wrong |
| Corrective RAG | External sources -> user query -> vectorisation -> **grade** -> query analyser -> **web search** -> vector DB -> prompt enhancement -> response generator -> output | Detect bad retrieval, then correct it (re-query, search the web) before answering | Corpus is incomplete or stale; wrong answers are costly | Extra latency; web results need source checks |
| Adaptive RAG (not drawn) | Router decides per query: no retrieval, single-step, or multi-step | Spend retrieval effort only where the query needs it | Mixed easy/hard traffic; cost control | Router mistakes send hard questions down the cheap path |

Stage numbers in the image are small and partly blurred; treat the order above as approximate and check against the original before publishing it.

## Decision rule (my view)
1. Start with plain vector RAG plus a small evaluation set (30 real questions with known answers). Do not add a variant until you can show where plain RAG fails.
2. Failures are missing or stale facts -> Corrective. Failures are multi-hop or entity questions -> Graph or Hybrid. Failures are cost on easy queries -> Adaptive.
3. Measure retrieval hit rate and answer accuracy separately; most "RAG problems" are chunking and metadata problems.

Related skills: `rag-implementation`, `rag-pipeline-architecture`, `agent-platform-rag-engine-management`. Command: `/rag-pick`. Agent for review: `rag-pipeline-reviewer`.

## Keywords
RAG, hybrid, graph, corrective, adaptive, retrieval, vector database, knowledge graph
