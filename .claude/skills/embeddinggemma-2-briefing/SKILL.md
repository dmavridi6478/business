---
name: embeddinggemma-2-briefing
description: Briefing notes on a card series about "EmbeddingGemma 2" (740M multimodal, 270M text-only, Apache 2.0). UNVERIFIED: a web search found EmbeddingGemma (308M) and Gemini Embedding 2, not these figures. Source: @codenameposhan.
---

# EmbeddingGemma 2 (as claimed by the cards, 6 Oct 2026) - unverified
**Check first:** a web search did not confirm "EmbeddingGemma 2", the 740M/270M sizes, or the benchmark numbers. It did find EmbeddingGemma (308M, text, under 200 MB RAM quantised) and Gemini Embedding 2 (multimodal, public preview 10 March 2026). Treat everything below as the card author's claims and verify against Google's model card and Hugging Face before use.
**Claims:** one embedding space for text, code, images, video and audio; 270M text-only, 740M full multimodal (adds a 170M vision and 300M audio encoder); Apache 2.0 open weights on Hugging Face and Kaggle; 8K token context; about 191 MB active RAM (text, quantised) and about 567 MB (multimodal); vectors 6x smaller by truncating 768 to 128 dimensions; 5.5 min of audio, 29 images or 58 video frames in one 8K context; MTEB Code 78.68 (+9.92 over v1), text barely moved; truncation cost: multilingual MTEB falls from 61.36 to 57.89 at 128 dims; run in bfloat16 or float32 because float16 gives NaN.
**Build ideas on the card:** local RAG, media search, code search, runs on transformers, sentence-transformers, MLX, vLLM, llama.cpp, Ollama, LM Studio, transformers.js. Related repo skills: `rag-implementation`, `embedding-strategies`, `vector-index-tuning`.
