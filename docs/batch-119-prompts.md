# Batch 115 prompt (files numbered 119)

Plain-text transcription of the four-page terminal prompt (watermark @wavaai.feeds). Light-edited for line breaks; wording otherwise as shown. Nothing here installs or runs anything. Before reusing it, read the critique in `.claude/skills/context-folding-layer-spec/SKILL.md`.

```
Build a persistent context-management layer for coding agents. The model writes summaries of history it has finished using. The layer folds those ranges out of the live context, keeps every original, and lets the agent search the folded history and restore it exactly when it needs detail again.

Write the code yourself from this behavioral spec. Respect the authentication, request signing, rate limits, and terms of service of every model provider and client you integrate with.

## 0. Pick an operating mode first and state it
MODE A: BUILD. Use this mode if you can write files, run code, and route the agent's model traffic, or if you can register tools in the host. Build the infrastructure described below.
MODE B: BEHAVIOR-ONLY. Use this mode if you are only a chat model with no tools, no proxy, and no storage. Then:
- Say plainly that you cannot intercept requests, enlarge your native context window, persist state, or restore original text after it leaves your context.
- Only offer what is real. You can write structured handoff summaries that follow the summary rules in section 5, keep a numbered ledger of the topics you summarized, and ask the user to paste back original material when exact detail is needed.
- Never describe a summary you wrote as "compressed and restorable." Never claim a restore happened unless a real tool returned the original bytes.
Neither mode enlarges the model's native context window. The benefit is that less history is resent each turn while the full history stays recoverable on demand.

## 1. Product goal and honest scope
Ship a system that:
1. sits between coding agents and model APIs, either as a local proxy or as an in-host plugin;
2. gives every addressable message a stable reference such as m00042;
3. gives the model tools (or text triggers) to compress, restore, search, and check status;
4. replaces folded ranges with model-written summary blocks that form a multi-tier hierarchy (T1 -> T2 -> T3);
5. persists all originals and state so restoration is exact, including after restarts;
6. keeps the resent prefix byte-stable so the provider's prompt cache keeps hitting.
Token savings, minimum workable window sizes, session length, and summary quality are things to measure and report. None of them is an acceptance criterion or a guarantee.

## 2. Architecture (layered)
- Kernel: pure library, no I/O, no network, no host imports, zero runtime dependencies. Input: canonical messages, CompressionState, config, token count. Output: transformed messages, new state, a structured nudge decision, and a content store. The kernel never calls a model. The summary text is an input.
- Wire codecs: lossless conversion between each provider body and canonical messages, in both directions: Anthropic Messages, OpenAI Chat Completions, OpenAI Responses (HTTP and WebSocket), and Google Gemini. Unknown parts ride a sidecar so the round trip is byte-faithful. A detector classifies a body, and an unparseable body passes through untouched.
- Host server: HTTP proxy, request pipeline, session identity, storage, tool execution loop, streaming rewrite, admin/status API, and web panel.
- Host adapters: thin per-client plugins and launchers.

## 3. Kernel data model
CoreMessage: id, role (user | assistant | system | tool), contentType (text | tool-call | tool-result | reasoning), text, toolName, toolCallId, plus media references.
CompressionBlock: blockId (b0, b1...), runId, tier 1|2|3, optional topic, summary, directMessageIds, effectiveMessageIds, directBlockIds (consumed child blocks), createdAt, survivedCount, generation young|old, active.
CompressionState: blocks, messageRefs {byRaw, byRef}, dead refs, checkpoints, nudge baselines/anchors, per-message tokenSnapshot, stats (tokensCompressed, compressionCount), and nextBlockId/nextRunId. All of it is plain serializable data, and the host owns persistence.
Hard invariants:
- A ref number (mNNNNN) and a content-hash message id are minted once and NEVER reused, even after the message is folded or dies.
- Folding marks rows inactive. It never physically deletes originals.
- Compress then context_restore(full) restores the original messages exactly.
- Protected tools and their paired results are hard-excluded from folds.
- Tool-call and tool-result pairs are never split.
- Signed or encrypted reasoning blocks are never rewritten and are never fold inputs.
- Tool-call arguments are forwarded byte-exact.

## 4. Per-turn pipeline (processTurn)
Run an ordered, composable node pipeline each turn, in this order: reconcile live ids -> assign refs -> sync blocks (survival counting, young->old promotion after promotionThreshold=5) -> prune (rebuild view) -> content-cached retrieval store -> absorb/hide -> deterministic crush -> absorb prompt -> message filters -> hide consumed compress calls -> recommend ranges -> nudge inject -> emergency truncate -> render refs.
- Prune. Drop messages covered by active blocks. Insert each block's rendered summary (id like ctx_summary_bN, header "[Compressed conversation section]") at its earliest covered position, using a pair-safe anchor. Always keep the session's FIRST user message verbatim, even when it is covered, because strict providers require a user turn.
- Ref tags. Annotate addressable messages with an inline tag holding ref, approximate tokens, and type, for example <ctx tokens="2.1K" type="tool:bash">m00175</ctx>. A timestamp attribute is optional. Render strategies are all | text-only (proxy default: never inject into tool args or results) | none. The token count is frozen at first render so the bytes stay stable.
- Unit projection. One function alone decides foldability: widen boundaries, carve out carriers/media/protected zones, check turn integrity, and check emptiness. The recommend side and the apply side MUST use this same function, so a range that is advertised is never rejected on apply.
- Recommend. Report compressible ranges, excluding covered messages and the preserved-recent zone. Suggested defaults: preserveRecentMessages 3, preserveRecentTokens 5000, minCompressRange 5000 tokens, summary length 50-20000 chars.
- Nudges (structured decision; the host renders the text):
  - Growth-gated cadence: a flat ~50K-token growth step that does not scale with the window. It is a user knob.
  - First-sight bypass: a session that arrives with enough ready mass gets nudged once usage reaches minContextLimitPct (0.45).
  - The growth baseline resets after a successful compress, which prevents re-fire loops.
  - Emergency at 0.95.
  - Tier-2/Tier-3 distillation triggers are based on token mass (default 1.5x the growth step). Count triggers are effectively off (1000/2000).
  - Phantom-pressure guard: wait for a real usage sample, but for at most 2 estimate-only rounds.
  - Text forms: soft or strong.
- Emergency truncation. The last safety valve for huge visible tool outputs near the limit. It never touches summaries, and it has a terminal escape after 3 attempts.
- No age-based GC. Old-generation blocks are batch-merged into higher-tier summaries, never dropped.

## 5. The tools (model-facing surface)
Expose these names, and keep them fixed: context_compress, context_restore, context_search, context_status. Optional: context_cache, context_absorb, context_retrieve. Provide schemas in each wire shape (Anthropic input_schema, OpenAI function.parameters, Responses flat, Gemini scalar-safe). The top level must be a plain object schema with no oneOf/anyOf/allOf, because Anthropic rejects those.

context_compress. One string field, content, carries ALL ranges in one call. Each block opens with a header line "mSTART-mEND optional topic" followed by its summary. The parser must be lenient: array/object forms, startId/startRef spellings, JSON fences, trailing commas, raw newlines, single quotes, gateway-stringified args, a single object where an array belongs, and salvage of complete entries from a truncated stream. A half-written entry is dropped, never guessed. Diagnostics are returned as data. Apply validates the refs, allocates blocks, consumes nested blocks into higher tiers, reports blocksCreated/tokensCompressed/errors, and refuses ranges that are entirely protected.

context_restore {blockId, full?, toFile?}. By default, go up one tier (a T2 block returns its T1 summaries; a leaf returns its originals). full:true returns the original messages. toFile writes the output to a file instead of inflating context. Large outputs (>~10K chars) go to a temporary file with a bounded retention reaper. Accept b5, B05, or 5.

context_search {query, limit=5}. Search both block summaries (active and inactive) and original message text. Each hit carries kind, ref, owning blockId, role, tokens, score, and a preview. That gives the agent a cheap loop: search, then restore only the block it needs. Use a pluggable registry: substring, BM25, fuzzy, hybrid, and an optional semantic search, all with zero dependencies.

context_status {scope?, view?, tool?, sort?, limit?, archiveDetail?}. Report context usage, blocks by tier, compressible ranges, and the nudge state. Recompute it live on every call, never from a stale cache.

context_cache {detail: summary|full} (read-only). Show the prompt-cache ledger: hits and misses split into new content, compression re-pay, and upstream TTL or client rewrite, plus per-fold breakeven.

context_retrieve {ref} (opt-in, content-cached retrieval). On arrival, store tool results above a threshold (4000 tokens) once and replace them with a deterministic placeholder that shows kind, size, head preview, and ref. Retrieval returns the original IN THE TOOL RESULT, wrapped and labeled as untrusted data. Neutralize closing tags in the body. Exports above 4000 tokens go to a host file the model pages through. Retrieval is idempotent and first-write-wins.

Text-trigger protocol, for hosts that cannot declare tools: <ctx_compress>{json}</ctx_compress>, <ctx_status></ctx_status>, <ctx_search>{json}</ctx_search>, <ctx_restore>{json}</ctx_restore>. The model emits the marker alone and stops. The proxy executes it, strips it from what the user sees, and continues. Hybrid mode makes compress a text trigger while the other tools are functions.

Standing system prompt (write your own wording). It should:
- explain the tags and tell the model never to echo them;
- explain the tools;
- say to compress by need, not by percentage;
- say that summaries are self-contained and record PAST state labeled as history;
- KEEP VERBATIM: full paths with line numbers, signatures and the critical code lines, exact errors, numbers and mechanisms, decisions with their "because," constraints, exact values, short user quotes only with their ref (otherwise mark them as paraphrased), "Open objectives:" with refs carried forward at every tier, goal evolution, the purpose of each action, open TODOs, anchor refs, and media URLs/file ids;
- DROP: verbose logs, duplicate reads, spent exploration, and dead ends, each reduced to a one-line lesson;
- for every dropped item, add a one-line content description;
- give a priority order: goal/intent/constraints > decisions > artifacts > findings > lessons;
- ask for dense bullets under thematic headers.
Add separate T2 distill and T3 condense rules. Overriding these four load-bearing rule sets requires acknowledgeRisk=true. Surface text (section headers, tool descriptions) can be overridden freely through prompt packs (default and lean, plus project > user > builtin directories), and outputs with no overrides must stay byte-identical. Language preservation is opt-in.

## 6. Optional deterministic helpers (default OFF)
- absorb: forced distillation of large tool results.
- crush strategies: lossless json-fold, comment-trimming code-trim, and log-select, where every distinct ERROR/FAIL line survives. Each strategy must be pure and deterministic and must fail open.
- Output steering: turn classification and verbosity levels L0-L4, with effort only ever clamped downward.
- External summary: an ordered failover chain of separate summarizer models with deadlines and concurrency caps. It never silently falls back to the main model, and its reports never leak keys, URLs, or history.
- Model-owned session rules.

## 7. Host server / proxy (MODE A)
- CLI. contextd start [--port --host --debug --config --passthrough]. Suggested ports: 8787 for a manual start; launcher-spawned instances use a separate base port with a +1 ladder on EADDRINUSE and a sticky record.
- Commands: export [id] [--full|--jsonl] (Markdown handoff of summaries plus originals); sessions ls|rm|archive|restore|foreign-blocks; storage gc [--days N] [--dry-run]; pack install|remove|list; doctor [--fix]; cache diff <dumps>; selftest; --version.
- Config: XDG paths with a context-management.json file. A single knob resolver applies env > config file > default, so leaf modules never read env directly. Compress settings merge in three levels: global -> provider -> model. A providers table holds upstream recipes. Context windows come from a live model registry, with a bundled snapshot as the floor.
- Request pipeline: triage admin routes; decode content with a decompression-bomb guard (413); enforce receive/decode/send byte budgets; strip inbound render markers per wire (ordered spec table); detect the wire and run a per-wire prepare step: canonicalize -> kernel fold -> rebuild -> inject system prompt, tools, and nudge where the wire requires them; relay upstream; rewrite the SSE or JSON stream per wire; run the tool loop: intercept the model's context tool calls, execute them locally, and continue the upstream turn, so the client never sees calls to tools it did not register; strip echoed tags from prose only (streaming-safe; arguments untouched); in proxy mode, carry the summary as a stable re-voiced user message so strict backends keep a stable prefix.
- Two compression modes, one code path. In proxy mode, the proxy injects tools and nudges. In plugin mode, the host agent owns the tools, and the proxy suppresses its own injection. Reason through both modes for every change.
- Prompt-cache stability: deterministic bytes after arrival; fold-anchor reconciliation; explicit Anthropic cache_control breakpoints; prompt_cache_key probing for origins that reject it; optional idle cache keepalive; a per-round cache ledger and billing (USD per model, with a compression payback view); a warning when the upstream cache collapses.
- Session identity: use the client's session id verbatim, preferring native stable ids; route anonymous traffic to anon-* sessions through prefix affinity (simhash chain, first-writer provenance); fork personas or subagents only on an evidence permitlist; message identity precedence: host msgid > order > content hash, with no fuzzy matching; when identity desyncs, fall back to the full legacy path for the turn and re-stamp truth headers.
- Fast paths (optional optimizations, each verified-or-fallback): an incremental plugin-turn lane (diff/ack/resync over host msgids); a watermark lane (reuse previous canonical cores and parse only the tail, with a breaker after 5 misses); server-side snapshot render of the prefix from stored rows. Any doubt means the whole turn takes the legacy path. Private headers (x-context-*) are stripped before upstream.
- Storage: one SQLite file (WAL, single batched writer) with tables sessions, conversations, messages, content, blocks, refs, dead_refs, checkpoints, retrieval_entries, message_media, session_ext, kv_store, statements; a stable absolute seq per row; additive migrations only, with a versioned schema; signed checkpoint frames plus per-row checksums; a background integrity check; classification of corruption errors; optional at-rest AES-256-GCM and zstd; an EPERM alert layer; opt-in session, dump, and storage GC; a driver ladder (builtin, then host, then a pinned prebuilt).
- Failure handling: preflight hold grace and dead-end cooldown; minimal SSE error plus finish on failed streams; degenerate (empty or truncated) turn detection with a continuation retry; an egress 429 governor (local hold, backoff, terminal 424); an upstream failure taxonomy and alerts; a runaway-stream terminator; learn-on-failure role compatibility rewrites; an event-loop watchdog; degrade, never guess.
- Security: admin routes under /__context/* accept loopback and trusted origins only; mask credentials in logs; body dumps are opt-in and carry a PLAINTEXT warning header; the CA for cert-MITM is generated lazily, with explicit trust discovery; re-sign signed gateways (e.g., HMAC APIG) after a body rewrite only where a re-signer exists, and otherwise refuse; per-lane credential overrides; stored originals are treated as untrusted content.
- Web panel: a server-rendered view over storage (it never owns data): session browser with a tier tree, logs, config editor with a parse guard, updates, notices (builtin + remote feed + local, fail-open), diagnostics blob, and an MD/SVG session report; i18n support; the panel never lies (a session with zero blocks exports nothing as "original").
- Update and install: check the registry every few minutes; update by tarball extraction with NO lifecycle scripts; the install source determines one writer per copy (a copy installed through a host channel is never written in place); advisories need a human to act, with no auto-rollback; opt-in self-restart; staggered rollout cohorts. Make telemetry and remote feeds opt-in or clearly disclosed.

## 8. Clients (group by integration style; preserve differences)
Verify each integration against the client's current version before claiming support.
- cert-MITM launcher (proxy plus a trusted local CA): pi, Codex, Claude Code, omp, opencode, Qoder, Trae, jcode, Kimi Code, Qwen Code, MiniMax Code, aider, Copilot CLI, Kiro, Amp, Crush, Zed.
- Base-URL rewrite to /context/<url>: hermes-agent, deepseek-harness, CodeBuddy, Gemini CLI (GOOGLE_GEMINI_BASE_URL), iFlow (IFLOW_BASE_URL), Antigravity (CLOUD_CODE_URL); Goose uses a base-URL redirect.
- In-process engine, no proxy: pi and opencode inline modes.
- Native plugins and MCP: Codex plugin: an MCP server named "context" with the four tools. Without a running proxy it reports "proxy unreachable." Claude Code plugin/MCP: a SubagentStart lane-token hook. opencode V1/V2 hooks with a /context command; pi/omp extensions with a subagent-delegation surface; deepseek-harness shim plus compaction gate; Kimi/ZCode managed TOML/JSON config edits that are idempotent and reversible; hermes plugin.
- An MCP or tool surface alone is NOT enough. Model traffic must actually pass through the engine for folding to take effect. Native compaction in the host should be disabled or gated so the two compressors don't fight.

## 9. Acceptance tests (deterministic, hermetic, mock upstreams)
1. Refs: deterministic assignment, never reused after fold, death, or restart. Sparse or unknown refs give a clean error.
2. context_compress -> context_restore(full) reproduces the original messages byte-for-byte. The default restore goes up exactly one tier.
3. After folding a range that contains the first user message, the wire holds the summary AND that message verbatim.
4. Tool pairs stay intact, and protected tools, latest-protected tools, and paths are never folded. A range that is entirely protected fails with a clear error.
5. Any range that recommend advertises is accepted by apply (shared projection).
6. Parser: fences, trailing commas, single quotes, stringified args, and truncated arrays salvage only the complete entries.
7. Schemas: no top-level combinators. A Gemini-safe variant exists. Every wire shape advertises the same tool set.
8. Nudge: no repeat without growth, baseline reset after compress, first-sight bypass, the T2/T3 mass triggers, and the estimate-hold backstop stops after 2 rounds.
9. Prompt surface: outputs with no overrides match golden fixtures byte-for-byte, and overriding a load-bearing rule without acknowledgeRisk throws.
10. Wire codecs: lossless round trip for all four wires, including unknown parts and mid-history system messages. Signed reasoning and tool args are unchanged.
11. Cache stability: across N turns with no new folds, the resent prefix bytes are identical. A content-cached retrieval placeholder stays byte-stable when the original is resent raw.
12. context_search finds terms that exist only in folded originals and returns the owning blockId.
13. Persistence: kill and restart, then status, search, and restore still work. Migrations are additive.
14. Tool loop: the client never receives context tool calls. The stream ends correctly on upstream errors.
15. Security: admin rejects non-loopback origins, and logs and dumps contain no keys.
16. Text-trigger mode: markers are executed and hidden from user-visible output.
17. Both modes (proxy and plugin) pass the same suite.
Report the measured token and cache numbers as observations, never as guarantees.

## 10. Verification requirements (do not invent)
- A unified snapshot-table storage model and declarative prompt-set packages are design directions, not requirements. Treat them as optional.
- A MySQL backend is optional and is for testing only. SQLite is the production store.
- External summary needs its own review of the config schema and secret storage before it ships.
- Exact parity with any existing tool is not claimed. Verify the behavior of the request pipeline, launcher, plugin, and storage layers against a running system and your own tests.
Deliver: a plan, the implementation, tests, an install guide, and a limitations section. If any requirement is infeasible in your environment, implement the closest honest subset and say so.
```

Command: `/context-layer-plan`. Agent: `context-layer-planner`.
