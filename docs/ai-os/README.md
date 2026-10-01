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
