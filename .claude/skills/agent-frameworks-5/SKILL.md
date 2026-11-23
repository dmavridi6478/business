---
name: agent-frameworks-5
description: Chooser for five open-source AI agent frameworks from a @dotdevs carousel (Agno, PydanticAI, CrewAI, LangGraph, smolagents) with the card's job line, licence and star figure for each, when to pick which, what each can touch, and a safe first-trial plan. Also covers the "8 free GitHub replacements for 8 subscriptions" video (what was new versus already in this library). Use when choosing a framework to build an agent in Python.
---

# Five agent frameworks (Batch 133, 23 November 2026)

Stars and licences are as printed on the cards; repo pages were not re-read this session (fetch rate-limited), so re-check before quoting.

| Framework | Card job line | Stars (card) | Licence (card) | Pick it when |
|---|---|---|---|---|
| Agno (`agno-agi/agno`) | Agents with memory, tools and knowledge in Python | 43,232 | Apache-2.0 | You want one Python package with memory and knowledge built in |
| PydanticAI (`pydantic/pydantic-ai`) | Agents with typed outputs | 21,266 | MIT | You already use Pydantic and want validated, typed results |
| CrewAI (`crewAIInc/crewAI`) | Role-based agents that work together on a task | 61,059 | MIT | The problem maps to roles (researcher, writer, reviewer) |
| LangGraph (`langchain-ai/langgraph`) | Stateful agent workflows as a graph | 45,102 | MIT | You need control over branching, loops, retries and saved state |
| smolagents (`huggingface/smolagents`) | Small library for agents that write and run code | 30,427 | Apache-2.0 | You want a minimal codebase to read end to end |

## How to choose
1. **Fixed steps, auditable:** LangGraph.
2. **Typed data in and out:** PydanticAI.
3. **Role-play teams, fast demo:** CrewAI.
4. **Memory and knowledge out of the box:** Agno.
5. **Smallest thing you can read in an afternoon:** smolagents.
[Guessing] Star counts show attention, not fit; try the same small task in two before committing.

## Care
- **Code-writing agents (smolagents)** execute generated code: run only in a sandbox or container, never with your credentials in the environment.
- **Tool access** is the risk in all five: give each agent the narrowest tools, read-only where possible, and require approval before sends, writes or spend.
- **Telemetry and cloud add-ons:** several vendors sell hosted platforms beside the open library; check what is sent where before enabling.
- **Fast-moving APIs:** pin versions.

## First-trial plan
Pick one task (for example summarise five web pages into a table with sources). Build it in the two most plausible frameworks, in a throwaway virtual environment, with a spend cap on the model key. Compare lines of code, failure handling and traces. Keep one.

## The "8 free GitHub replacements" video (@valeridoesai)
Eight tools replace eight subscriptions: OpenWhispr (Wispr Flow), Cal.diy (Calendly), Chatwoot (Intercom), AppFlowy (Notion), Cap (Loom), VoiceStudio (ElevenLabs), OpenSEO (Semrush). Frames show 7 of the 8 named. Already in this library: OpenWhispr, AppFlowy, Cap, VoiceStudio, OpenSEO. Added in `oss-alternatives`: Chatwoot and Cal.diy. Caveats: "free" means free licence, not free to run: you host, secure, back up and update them; VoiceStudio-style voice cloning needs consent from the voice owner; the video's "bill drops to almost $0" ignores your time and server costs. No audio transcript was available; claims come from on-screen text only.

Related: `langchain-architecture`, `ai-ecosystem-map`, `ai-agents-for-beginners`, `build-ai-agent-10-minutes`, `oss-alternatives`, `trial-repo`.
