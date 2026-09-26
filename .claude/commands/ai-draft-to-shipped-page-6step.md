---
description: The 6-step loop (Reference → Shape → Build → Render → Critique → Repair) that turns a rough AI-coded page into a shipped one, with the 4 MCP/CLI tools each step uses
argument-hint: [step name, "audit" to run the loop on a page you already built, or a rough page idea to start step 1]
---

# Stop Shipping the First AI Draft

Source: @jimai005, "Stop Shipping the First AI Draft" (7-slide carousel). The core claim: pages get good because you repair them, not because the first draft was magic. Use the same 6-step loop on every page.

```
1 REFERENCE → 2 SHAPE → 3 BUILD → 4 RENDER → 5 CRITIQUE → 6 REPAIR
```

## Step 1 — Reference: show the agent what "good" means before it designs

Give it 3 references instead of a vague prompt — Layout (A), Type (B), Nav (C) — and ask it to combine layout-from-A + type-from-B + nav-from-C into the new page. Same ingredients, a better page. "Don't just say modern — be specific."

**Tool: Mobbin MCP** — lets your coding agent search real shipped product UI for references directly, instead of you screenshotting apps by hand.

- Official hosted server, nothing to clone/install/run locally: `https://api.mobbin.com/mcp` (Streamable HTTP transport, OAuth sign-in on first use). Docs: https://docs.mobbin.com/mcp
  ```json
  { "mcpServers": { "mobbin": { "url": "https://api.mobbin.com/mcp" } } }
  ```
- No Mobbin access? Pick 3 screenshots yourself — the split (layout/type/nav) still works without the tool.
- This repo already lists Mobbin the *website* as a manual inspiration resource in `design-dev-resources` and `designer-resource-directory` — this MCP server is the newer, agent-callable version of the same source, not a duplicate: it lets the agent pull references itself mid-build instead of you pasting screenshots in.

## Step 2 — Shape: make the design decisions before the code starts

A better prompt is not enough — you want a structured brief: Audience (who's this for?), Goal (what's the page for?), Hierarchy (what matters most?), Layout & Visual Tone, States & Edge Cases. Turn "build something amazing" into a 5-section brief before any code is written.

**Tool/command:** `/impeccable shape` — from `pbakaus/impeccable` (already documented in this repo's `claude-code-tooling` and `web-design-taste-workflow` skills as a general design-quality tool; this carousel is the first source in this repo naming its individual subcommands). This one turns a rough idea into the 5-section UI brief above.

## Step 3 — Build: from real components, not made-up ones

Start from an actual component library (buttons, cards, navbar, feature blocks, accordions, image/media) instead of the agent inventing markup from scratch — fewer weird decisions, faster, more consistent spacing.

**Tool: shadcn MCP** — lets the coding agent browse, search, and install real shadcn/ui components (works with Claude Code, Codex, and other agents). The repo behind it, `shadcn-ui/ui`, is already documented in this repo's `dev-repos-to-clone` skill (`npx shadcn@latest init` to pull components directly into your repo) — same project, this carousel just names the MCP-driven browse/search/install workflow specifically rather than the plain CLI init.

## Step 4 — Render: open the real page and look at the actual result

This is where you stop judging the prompt and start judging the page. Check: does it still look good on mobile, did spacing/images/type render correctly, are there console errors or broken states, capture a screenshot to review next. "If you never open the page, you're still guessing."

**Tool: Chrome DevTools MCP** — official browser tools that let the coding agent open pages, inspect them, resize them, and take screenshots.
```bash
claude mcp add chrome-devtools -- npx chrome-devtools-mcp@latest
```
Already partially documented in this repo's `explain-interface` skill (for reverse-engineering *someone else's* page); this carousel uses the identical tool for checking *your own agent's just-built* page instead — same install, different job. Alternative named in the source: Playwright MCP, for browser automation and page interaction.

## Step 5 — Critique: review it like a designer, not just a compiler

A page can work and still feel off — this step is where you catch that. Split the review in two: **Critique** (design quality — hierarchy, spacing, alignment, clarity) vs. **Audit** (technical quality — accessibility, responsive issues, performance basics, broken implementation details). "Works" is not the same thing as "it's good." Run both on the actual rendered page output, not just the prompt.

**Tools/commands:** `/impeccable critique` (design review) and `/impeccable audit` (technical review) — same `pbakaus/impeccable` repo as step 2.

## Step 6 — Repair: fix the failure you found, then render again

The loop most people skip. Fix one issue at a time, then re-render, re-critique, repeat until the meaningful problems are gone — you're not chasing perfection, you're removing obvious reasons the page feels unfinished.

**Tools/commands:** `/impeccable layout` (structure, spacing, composition), `/impeccable typeset` (text hierarchy and readability), `/impeccable polish` (finish, consistency, detail) — same `pbakaus/impeccable` repo. Run `render → critique → repair` as an inner loop until nothing meaningful is left to fix, then ship.

## Plain-text prompt to run the whole loop

```
I have a rough AI-drafted page: [PASTE URL OR DESCRIBE IT]. Run the 6-step
loop on it: (1) pull 3 real references for layout/type/nav via Mobbin MCP
if available, else use these screenshots [PASTE]; (2) write a 5-section UI
brief (audience, goal, hierarchy, layout & visual tone, states & edge
cases); (3) rebuild using real shadcn/ui components, not invented markup;
(4) open the actual rendered page (desktop + mobile) and list every console
error and broken state; (5) critique it as a designer (hierarchy, spacing,
alignment, clarity) and separately audit it as an engineer (accessibility,
responsive issues, performance, broken details); (6) fix one issue at a
time and re-render until nothing meaningful is left. Show me the brief
from step 2 and the final issue list from step 6 before you ship.
```

## Related

`dev-repos-to-clone` (shadcn-ui/ui), `explain-interface` (chrome-devtools-mcp, for reverse-engineering instead of self-review), `claude-code-tooling` and `web-design-taste-workflow` (pbakaus/impeccable, general documentation), `design-dev-resources` and `designer-resource-directory` (Mobbin the website, vs. Mobbin MCP here).
