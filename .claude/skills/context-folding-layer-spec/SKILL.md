---
name: context-folding-layer-spec
description: The four-page terminal-screenshot prompt "Build a persistent context-management layer for coding agents" (@wavaai.feeds) turned into a checked reference - the two operating modes, the layered architecture (kernel, wire codecs, host server, adapters), the data model and hard invariants, the per-turn pipeline, the four tools (context_compress, context_restore, context_search, context_status), optional helpers, proxy and storage requirements, clients, 17 acceptance tests and verification rules - with a critique (scope, security of a trusted-CA proxy, unverified client list, no benchmarks) and a staged build plan. Use when someone wants to build or evaluate a context-folding proxy or plugin for Claude Code, Codex or similar agents, or wants the honest chat-only (Mode B) workflow.
---

# Context folding layer: spec reference (@wavaai.feeds, four pages)

Source: four screenshots of a long prompt in a terminal. I read every page from rendered crops; the full condensed text is in `docs/batch-119-prompts.md`. Section numbers below are the prompt's. The critique and the staged plan are my additions. Nothing was built or run.

## What it asks for

A layer between coding agents and model APIs where the model writes summaries of finished history, the layer folds those ranges out of the live context, keeps every original, and lets the agent search and restore them exactly. Its own honest scope (section 1): it does **not** enlarge the model's native context window; the benefit is that less history is resent each turn while the full history stays recoverable. Token savings, window sizes and summary quality are "things to measure and report, not guarantees".

## The structure

| Section | Content |
|---|---|
| 0 Operating mode | **Mode A build** (can write files, run code, route traffic or register tools). **Mode B behaviour-only** (chat model, no tools): say plainly you cannot intercept requests, enlarge the window, persist state or restore text; write structured handoff summaries, keep a numbered ledger of summarised topics, ask the user to paste originals back; never call a summary "compressed and restorable" and never claim a restore happened unless a real tool returned the bytes |
| 1 Goal | Proxy or in-host plugin; stable refs like `m00042`; compress, restore, search and status tools; model-written summary blocks in tiers T1 to T3; persisted originals; byte-stable resent prefix so provider prompt caching keeps hitting |
| 2 Architecture | **Kernel** (pure library, no I/O, never calls a model); **wire codecs** (Anthropic Messages, OpenAI Chat Completions, OpenAI Responses over HTTP and WebSocket, Gemini; lossless; unknown parts in a sidecar; unparseable bodies pass through); **host server**; **host adapters** |
| 3 Data model, invariants | CoreMessage, CompressionBlock (tier 1 to 3), CompressionState. Refs and ids minted once and never reused; folding marks rows inactive and never deletes; compress then restore(full) returns the originals exactly; protected tools and their paired results never folded; tool-call and tool-result pairs never split; signed or encrypted reasoning never rewritten; tool-call arguments forwarded byte-exact |
| 4 Per-turn pipeline | reconcile ids, assign refs, sync blocks (young to old after 5 survivals), prune, retrieval store, absorb, deterministic crush, filters, recommend ranges, nudge, emergency truncate, render refs. Defaults: preserve 3 recent messages or 5000 tokens, min range 5000 tokens, summary 50 to 20000 chars; nudge growth step about 50K tokens, first-sight at 0.45 of the limit, emergency at 0.95; no age-based deletion |
| 5 Tools | Fixed names `context_compress`, `context_restore`, `context_search`, `context_status`; optional `context_cache`, `context_absorb`, `context_retrieve`. Schemas per wire, top-level plain object with no oneOf/anyOf/allOf. Lenient compress parser that salvages complete entries and drops half-written ones. Search over summaries and originals (substring, BM25, fuzzy, hybrid). Text-trigger fallback for hosts without tools. A standing system prompt that keeps paths, errors, decisions with their reasons and open objectives verbatim and drops verbose logs |
| 6 Optional helpers (default off) | forced distillation, lossless crush strategies that fail open, output-steering levels, external summariser chain that never silently falls back to the main model |
| 7 Host server | `contextd` CLI (start, export, sessions, storage gc, pack, doctor, cache diff, selftest); config precedence env > file > default; request pipeline with a decompression-bomb guard (413) and byte budgets; tool loop executes context tools locally; prompt-cache stability (cache_control breakpoints, ledger, collapse warning); session identity; SQLite WAL storage with checksums and optional AES-256-GCM; failure handling (429 governor, runaway-stream terminator); security (loopback-only admin, masked logs, opt-in body dumps, lazily generated CA); web panel; updates by tarball with no lifecycle scripts; opt-in telemetry |
| 8 Clients | cert-MITM launcher for many CLIs; base-URL rewrite for others; in-process for two; native plugins and MCP for Codex, Claude Code, opencode, pi and others. "An MCP or tool surface alone is NOT enough"; native compaction should be disabled or gated |
| 9 Acceptance tests | 17 deterministic, hermetic tests with mock upstreams (refs never reused, exact restore, protected pairs, parser salvage, schema shapes, nudge behaviour, cache-stable prefix, search in folded text, persistence across restart, no client-visible tool calls, security, text triggers, both modes pass) |
| 10 Verification | Snapshot-table storage and prompt packages are optional design directions; MySQL is test-only, SQLite is production; external summary needs its own security review; exact parity with any existing tool is not claimed. Deliver plan, implementation, tests, install guide and limitations; if infeasible, build the closest honest subset |

## Critique (my additions)

- **Scale.** This is months of engineering for a team, not a prompt. A single session cannot responsibly deliver all of sections 7 and 8; the prompt itself says to build the closest honest subset.
- **Security of the cert-MITM launcher.** Installing a local certificate authority so a proxy can read and rewrite every client's HTTPS traffic is a high-impact trust change. It exposes API keys and all prompts to that process. Do it only on a machine and for clients you control, scope the CA tightly, never run it on shared or production hosts, and prefer base-URL rewrite or plugin modes.
- **Terms of service.** Rewriting client requests may conflict with a provider's or client's terms or request signing; the prompt's first paragraph says to respect them. Check before shipping.
- **Quality risk.** Summaries replace history: a bad summary loses information the model needs. Exact restore mitigates this only if the agent knows to search and restore. Measure task success, not just tokens.
- **Unverified client list.** About twenty clients are named with integration styles. Verify each against its current version; I verified none.
- **No evidence.** The screenshots contain no benchmark, repo or result. Treat savings claims as hypotheses.
- **Source.** The prompt is credited to a watermark only (@wavaai.feeds); no author, licence or repo is given. Reuse of the prompt text is under whatever terms its author intended: ask before republishing it verbatim.

## Staged plan if you actually build it

1. Kernel library with the data model and invariants, plus tests 1 to 5 and 10 (no network, no model).
2. One wire codec (Anthropic Messages) and the four tools with the lenient parser; tests 6, 7.
3. SQLite persistence and the search/restore loop; tests 12, 13.
4. A loopback proxy for one client via base-URL rewrite, tests 11, 14, 15; measure cache hits and token use on real sessions.
5. Only then consider more codecs, the panel and the nudge tuning. Skip the MITM launcher unless you have a clear need.

## Use

`/context-layer-plan [your agent, host and constraints]` writes a plan; the `context-layer-planner` agent writes it to a file. Mode B (chat only) users can use the handoff-ledger workflow in section 0 and nothing else. Related: `strategic-compact`, `context-budget`, `claude-api` prompt-caching notes, `context-management-context-manager` agent.
