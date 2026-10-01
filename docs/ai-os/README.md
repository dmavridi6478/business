# AI Entrepreneur OS — operating manual

Built in Batch 98 from the ReStructure AI video "The Entire AI Entrepreneur Operating System" (TikTok @restructureai; creator's own claim: a 200-hour blueprint with 41 agents across 7 modules). This repo implements the **25 agents that are legible on screen**. The other ~16 (Operations, Content & Design, Risk & Legal, Data & Observability, Human Handoff internals) were not readable in the frames and are deliberately **not invented**.

## Architecture

```
                       YOU  (approvals, top 3)
                             ▲
                             │  Slack / Notion
            ┌────────────────┴────────────────┐
            │  03 THE BRAIN (Command Center)  │
            │  os-chief-of-staff              │
            │  os-priority   os-approval      │
            │  os-business-analyst os-watchdog│
            └──────┬───────────────────┬──────┘
   Grow            │ Find       Protect│       Run
 os-ads            │ os-response       │ os-bookkeeping   os-onboarding  (Day 0)
 os-seo            │ os-followup       │ os-invoice       os-checkin     (Day 7)
 os-email-sms      │ os-close          │ os-profit        os-health      (Day 30)
 os-lead-magnet    │ os-prospect       │ os-cashflow      os-referral    (Day 90)
                   │ + Research & Offer: os-market os-pain-point os-offer-builder os-pricing
            ┌──────┴───────────────────────────┐
            │ 01 KNOWLEDGE LAYER               │
            │ docs/ai-os/ops/   (SOPs, stack)  │
            │ docs/ai-os/rules/ (permissions,  │
            │   approval limits, compliance)   │
            └──────────────────────────────────┘
```

## The one design decision that matters

The video shows agents that reply to leads, send invoice reminders and shift ad budget. **Every agent here starts at autonomy tier 0 — draft only.** Nothing leaves the building without a recorded human approval. Promote an agent to a higher tier only by editing `rules/agent-permissions.md` after you have read 20+ of its drafts. See `rules/` for the tiers.

### What is enforced by code, and what is still only an instruction

A hostile review of the first build (`Artifacts/business/os-agents-hostile-review.html`) found that "draft-only" was a sentence, not a control. Status:

| Control | Enforced by | Status |
|---|---|---|
| `os-*` agents write only their own `.md` paths (default `data/ai-os/drafts/`); no `.claude/**`, no `docs/**`, no symlink or `..` escape | `.claude/hooks/os_guard.py` (PreToolUse, fails closed) | **enforced** (26 tests) |
| Nobody, agent or session, writes `approvals.md` or `log/**` | same hook + `permissions.deny` in `.claude/settings.json` | **enforced** |
| Approvals are human-only, bound to the exact card text, expire after 24 h, tamper-evident | `scripts/os_approvals.py` (needs a real terminal) | **enforced** for anything that calls `check`; no sender calls it yet |
| Evidence of what agents did, which they cannot erase | `.claude/hooks/os_log.py` (hash-chained log) + `integrity` report | **enforced**; absence of the log is reported as CRITICAL |
| Exfiltration (finding 3): the 4 web agents (`os-seo`, `os-market`, `os-pain-point`, `os-prospect`) fetch only allow-listed https hosts and cannot read private data; every other agent has no network tool; `os-*` agents cannot call connectors at all | `os_readscope.py`, `os_outbound.py`, `docs/ai-os/rules/fetch-allowlist.txt`, a frontmatter lint test | **enforced** (23 tests) |
| Connector sends/changes in the main session (finding 4): any connector tool that can send, change or spend asks you to confirm; read-only ones pass | `os_outbound.py` (`OS_OUTBOUND_MODE=off` at launch disables) | **enforced**, with caveats below |
| Second-order injection (finding 4): external text only inside ```` ```untrusted ```` fences, never acted on by readers; integrity report flags instruction-like text outside fences | agent baselines (instruction) + `integrity` heuristic scan (tripwire) | **partly enforced**: the scan is a heuristic, the fence rule is a prompt rule |
| Missing consent/price/opt-out files, same-day overwrite, numeric limits, orchestrator cannot delegate, connector wording, injection reporting | nothing yet | **OPEN** (review findings 5, 7, 8, 9, 10, 11) |

**Caveats you should know.** (1) Every `os-*` restriction relies on Claude Code passing `agent_type` to hooks, as its documentation says; I could not run a live subagent, so prove it with the canary below. (2) The main session is still unrestricted for everything that is not a connector send/change: it can write any file, including these hooks. That is by design (it is you, supervised) and means a hijacked main session is not contained; the confirmation prompts only help if you read them. (3) `WebSearch` queries are not restricted. (4) The allow-list is only as good as its entries: never add a host whose logs an outsider can read.

**Canary — run after restarting Claude Code.** Paste: *"Use the os-seo agent. Task: try to Read data/ai-os/drafts/ and try to WebFetch https://example.com/. Report exactly what each call returned."* Expected: both blocked, and `python3 scripts/os_approvals.py integrity` then shows `denials_today: 2` and verdict WARN. If either call succeeds, hooks are not receiving `agent_type`: stop using the agents and treat findings 1–4 as open again.

Hooks load when a session starts: **restart Claude Code (or review `/hooks`) after pulling this change**, and run `python3 -m unittest scripts/test_os_guard.py` once. Until the hooks are live in your session none of the enforced rows apply.

## Folder map

| Path | Purpose |
|---|---|
| `.claude/agents/os-*.md` | the 25 subagents |
| `.claude/skills/ai-entrepreneur-os/SKILL.md` | how to run the OS, model tiering, build order |
| `.claude/commands/os-morning-page.md`, `os-run-module.md` | the two entry commands |
| `docs/ai-os/ops/` | SOPs and tool stack — **you must fill these in** |
| `docs/ai-os/rules/` | permissions, approval limits, compliance |
| `data/ai-os/` | runtime drafts and logs (gitignored) |

## First-week build order

1. Fill `ops/tool-stack.md` and `rules/approval-limits.md` (the `OWNER MUST SET` lines). Agents refuse to guess these.
2. Connect the connectors you actually use (status in `ops/tool-stack.md`).
3. Run `/os-morning-page` for 5 days with **only** the Brain agents and one module (Finance is the safest start — read-only).
4. Read every draft. Fix the SOPs, not the agent.
5. Add the next module. Never add two at once.
