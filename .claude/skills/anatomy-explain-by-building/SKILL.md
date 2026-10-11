---
name: anatomy-explain-by-building
description: wheresryan22/anatomy - a Claude Code skill that explains an idea by building it as an interactive, many-part isometric object (SVG plus WebGL/3D) instead of text, with the install command, the example prompt and the claimed examples, from a short @GithubSignals video read from sampled frames only. Use when you want a visual, interactive explanation of a mechanism (rate limiter, cache, engine), or when evaluating the anatomy skill before installing it.
---

# anatomy (explain an idea by building it)

**Confidence: low.** Source is a short video read from frames (no audio). Verify the repo before installing.

- What it is, per the video: "A Claude Code skill that explains an idea by building it as a real, working object": interactive isometric figures made of many small, precise parts, rendered with SVG, WebGL and 3D.
- Repo: `wheresryan22/anatomy` (site shown: skills.wheresryan.sh/anatomy). MIT, Node >= 20.10, zero dependencies (as shown).
- Install (as shown, run on your own machine): `npx skills add wheresryan22/anatomy -g -a claude-code`
- Use: ask in Claude Code, for example `anatomy: explain how a token bucket rate limiter works`.
- Claimed examples: a raptor engine (SVG engine with WebGL plume); "cache key = skips work" as a pin-tumbler lock; "one GPU context, many canvases" as a gantry plotter.

## Before installing
`npx skills add -g` installs a skill globally into your agent: read its SKILL.md and scripts first (a skill is instructions your agent obeys). Not installed in the cloud session.

## Equivalent without installing
Prompt: "Explain [CONCEPT] as a single self-contained HTML page: an interactive diagram where each part is a labelled shape, hovering a part shows what it does, and a step button walks one request through the system. No external libraries beyond what is allowed; finish with a three-sentence summary." In this environment such pages are published as artifacts.
