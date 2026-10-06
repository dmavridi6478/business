---
name: ai-engineer-roadmap-2026
description: 'The 8-step AI engineer roadmap for 2026 (Python, maths, machine learning, generative AI, LLM fundamentals, RAG, AI agents, multi-agent systems), what to learn at each step, six capstone projects, and a 12-week pacing with a portfolio check. Use when someone asks how to become an AI engineer, wants a study plan, or is choosing what to learn next. Source: @the.wealth.lab carousel; course providers are not named in the source and none are invented here.'
---

# AI engineer roadmap 2026

Order from the carousel: **Python -> Maths -> Machine learning -> Generative AI -> LLMs -> RAG -> Agents -> Multi-agent.** Slides 3 (ML), 6 (RAG), 8 (AutoGen) were read in the batch; the carousel's course names are not visible, so providers are left blank on purpose.

| Step | Topic | Learn | Proof you can show |
|---|---|---|---|
| 1 | AI Python for beginners | Fundamentals, data structures, functions, OOP; use AI assistants to speed up and get feedback; small automation scripts | 3 scripts in a repo |
| 2 | Maths behind AI | Linear algebra, calculus, probability; vectors, matrices, gradients, optimisation | Gradient descent by hand in NumPy (see `scripts/ml/deep_spirals.py`) |
| 3 | Machine learning | Supervised and unsupervised learning; classification, regression, clustering, NLP, time series; evaluate on real datasets | One model with a held-out test score |
| 4 | Generative AI for everyone | How generative systems work; use cases; prompt-engineering basics | Prompt set with before/after outputs |
| 5 | LLM fundamentals | Training and deployment, tokenisation, embeddings, fine-tuning, alignment; GPT, Claude, Gemini, open models | Token-cost comparison of two models |
| 6 | RAG | End-to-end pipeline: ingestion, embeddings, vector DBs, retrieval strategies, evaluation; assistants over custom knowledge | RAG over your own documents with an eval set (`rag-variants-compared`) |
| 7 | AI agents | Reasoning, planning, tool use, memory, external data; agent architectures | One agent with 2 tools and a log |
| 8 | Multi-agent (AutoGen-style) | Design patterns, communication, orchestration, delegation | A 3-agent workflow with a human approval step |

**Final challenge (from the source):** AI chatbot; RAG knowledge assistant; AI research agent; content automation system; multi-agent workflow; AI SaaS application.

## Pacing (my suggestion, 12 weeks, about 8 h/week)
Weeks 1-2 steps 1-2 - 3-4 step 3 - 5 steps 4-5 - 6-7 step 6 - 8-9 step 7 - 10 step 8 - 11-12 one capstone, public and documented.

## Honest critique
- The roadmap is course-shopping order, not hiring order. Employers screen on shipped projects; step 2 can be shortened if you start from step 6 and learn maths when a bug demands it.
- Roadmaps that end at "build an AI SaaS" skip evaluation, cost and security. Add an eval set and a cost log to every project.
- The same account also sells a digital store; treat the carousel as marketing, not a curriculum audit.

Related: `ai-engineering-portfolio`, `rag-variants-compared`, `agent-stack-power-ups`, `claude-skill-tutor-25` (to study each step).

## Keywords
AI engineer, roadmap, learning path, Python, RAG, agents, AutoGen, portfolio
