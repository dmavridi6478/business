# Claude Code Token-Saving Skills

Source: @theromanknox (skool.com/knox)

5 skills to reduce token waste and keep Claude Code sessions efficient.

---

## SKILL 01 — /DOCTOR

Always run `/doctor` first.

It calculates your skill list's cost and highlights the biggest context drains before prompts start getting expensive.

**Use when:** Starting any session. Run before anything else.

---

## SKILL 02 — /PONYTAIL

Directs Claude to produce shorter code and explanations.

Reduces token usage by keeping answers concise.

> 87% fewer tokens (12,840 → 1,240)

**Use when:** You need a quick answer without full explanations or verbose code comments.

---

## SKILL 03 — /REWIND

Use `/rewind` to jump back before the error instead of wasting ten more messages fixing it.

**Use when:** Claude goes down the wrong path. Instead of correcting from the error forward, rewind to the last good state.

---

## SKILL 04 — /COMPACT

Use `/compact` in long sessions.

Creates a condensed checkpoint; can shrink active history by up to 85%.

**Use when:** A session has grown long and response quality is degrading. Compact before starting a new major task within the same session.

---

## SKILL 05 — /HANDOFF

Run `/handoff` first when starting a new session.

Carries forward:
- Goal & intent
- Key decisions
- Current state
- Next steps

Clean slate. Full context of what matters.

**Use when:** Ending one session and beginning the next. Ensures continuity without re-explaining the whole project.

---

## Quick Reference

| Skill | When to use |
|---|---|
| `/doctor` | Session start — audit context cost |
| `/ponytail` | Need short, concise answers |
| `/rewind` | Wrong direction — go back to last good state |
| `/compact` | Long session — compress history |
| `/handoff` | New session — carry forward what matters |
