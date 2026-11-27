---
name: llm-app-tools-5
description: Five open-source projects for LLM apps from a @dotdevs carousel (vLLM, Langfuse, LiteLLM, promptfoo, llama.cpp) with card figures and licences, how they fit together, and the licence catch on "MIT core, paid enterprise features"; plus five tiny web tools (tldraw, readme.so, Shields.io, Hoppscotch, Omatsuri) and a free "idea to App Store" workflow (Pineflow). Use when choosing serving, tracing, gateway, evaluation or local-run tools for an LLM product.
---

# Five LLM-app projects, five tiny tools (Batch 135)

Card figures only; repo pages were not read this session.

## A. Five projects for LLM apps (@dotdevs)

| Project | Card says | Card stars | Licence (card) | Job in the stack |
|---|---|---|---|---|
| vLLM (`vllm-project/vllm`) | High-throughput, memory-efficient LLM serving | 97,115 | Apache-2.0 | Serve an open model to many users on GPUs |
| Langfuse (`langfuse/langfuse`) | Trace, evaluate and debug your LLM app | 37,585 | MIT core, paid enterprise features | Observability and evals |
| LiteLLM (`BerriAI/litellm`) | 100+ LLM providers through one OpenAI-style API | 63,474 | MIT core, paid enterprise features | Gateway: one API, key and spend control |
| promptfoo (`promptfoo/promptfoo`) | Test and compare prompts and models; red-team agents | 27,412 | MIT | Evaluation before shipping |
| llama.cpp (`ggml-org/llama.cpp`) | Run language models on your own hardware, little setup | 135,608 | MIT | Local and edge inference |

**How they fit:** app, then LiteLLM (routing, keys, budgets), then vLLM (your own GPUs) or a hosted provider; Langfuse records traces; promptfoo runs regression tests on prompts and models before each release; llama.cpp covers laptops and small devices.

**Catches**
- "MIT core, paid enterprise features": features such as SSO, audit logs or advanced access control may sit behind a paid licence. Check the repo's enterprise folder and licence file before depending on one.
- A gateway holds all your provider keys: treat it as a high-value target, restrict network access, and log spend.
- Tracing stores prompts and outputs: those can contain personal data; set retention and masking.
- Serving open models needs GPU capacity and ops skill; hosted APIs may be cheaper at low volume.
- Compare with `agent-frameworks-5` (building agents) and `trending-three-nov23` (magpie, another gateway).

## B. Five tiny tools ("save you hours every week", @dotdevs)
| Tool | Does |
|---|---|
| tldraw (tldraw.com) | Sketch the flow before you build it: infinite canvas whiteboard |
| readme.so | Build a clean README from section templates |
| Shields.io | Badges for repos (dynamic and static) |
| Hoppscotch (hoppscotch.io) | Test any API in the browser |
| Omatsuri (omatsuri.app) | Gradients, shadows, SVG helpers and other browser tools |

Care: web tools that take an API key or code (Hoppscotch) should be given test keys only; paste no secrets into a hosted tool you have not vetted.

## C. "Free vibe coding workflow" (Pineflow)
A card promotes "Idea to App Store, 11 chapters, no sign-up" at stackpine.app/pineflow. Not opened; unverified. Treat as a tutorial, not a guarantee of an App Store approval.

Run with `/trial-repo <owner/repo>`. Related: `oss-alternatives`, `ai-ecosystem-map`, `trace-to-training-data`, `quantized-export`, `agent-frameworks-5`, `startup-stack-2gb-ram`.
