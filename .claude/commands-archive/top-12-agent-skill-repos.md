# Top 12 Agent Skills You Should Know

Source: ByteByteGo, "The most-starred skill repos on GitHub (August 2026)."

Every repo below was checked with a live GitHub search before being listed.
Six resolved to a confident owner/repo; six had no owner visible on screen
and share a name with dozens of similarly-named repos — those are flagged
**unverified** rather than guessed at, per this repo's standing rule of not
writing down a repo that wasn't actually confirmed to exist.

| # | Name | Stars (source) | What it does | Repo |
|---|---|---|---|---|
| 1 | Superpowers | ★266k | Makes your agent plan and test before it writes code | [`obra/superpowers`](https://github.com/obra/superpowers) — confirmed, 291k★ live |
| 2 | skills | ★201k | Makes your agent challenge its plan first | **Unverified** — no owner shown; too generic a name to resolve with confidence (closest real matches found were all under 20 stars) |
| 3 | andrej-karpathy-skills | ★199k | Karpathy's tips to avoid common AI coding mistakes | [`multica-ai/andrej-karpathy-skills`](https://github.com/multica-ai/andrej-karpathy-skills) — confirmed, 215k★ live |
| 4 | everything-claude-code | ★178k | Sets up your coding agent like rules and hooks | [`affaan-m/everything-claude-code`](https://github.com/affaan-m/everything-claude-code) — confirmed reachable; several forks/mirrors exist under other owners with far lower star counts, this is the original |
| 5 | skills (official) | ★163k | Anthropic's own skills to create Word, Excel, PDF, and more | [`anthropics/skills`](https://github.com/anthropics/skills) — **already documented** in this repo's `claude-code-tooling` skill as the upstream source of the installed `docx`/`pptx`/`xlsx`/`pdf` skills |
| 6 | ui-ux-pro-max-skill | ★113k | Helps your agent design pages that don't look like AI | [`nextlevelbuilder/ui-ux-pro-max-skill`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) — confirmed, 130k★ live |
| 7 | caveman | ★95k | Agent talks like a caveman — short words, way cheaper | **Already vendored** in this repo as the `caveman` skill (`JuliusBrussee/caveman`, per Batch 79) |
| 8 | ponytail | ★86k | Makes your agent write less and simpler code | **Unverified** — no owner shown; not found under a plausible name in a live search |
| 9 | agent-skills | ★79k | Your agent follows production-grade engineering habits | **Unverified** — no owner shown; too generic a name to resolve with confidence |
| 10 | graphify | ★75k | Maps your codebase so the agent can navigate it easier | **Unverified** — no owner shown; not found under a plausible name in a live search |
| 11 | Understand-Anything | ★69k | Turns confusing code into visual maps you can explore | **Unverified** — no owner shown; not found under a plausible name in a live search |
| 12 | impeccable | ★54k | Makes your UI design polished and consistent | **Already documented** in this repo's `claude-code-tooling` skill (`pbakaus/impeccable`, per Batch 79 — cloned and actually run against two of this repo's own artifacts) |

## Net new to this repo

Only **3 of the 12** aren't already covered or unverifiable:
`obra/superpowers`, `multica-ai/andrej-karpathy-skills`,
`affaan-m/everything-claude-code`, `nextlevelbuilder/ui-ux-pro-max-skill`
(4, correcting the count — the other 8 are either already vendored/
documented or unverified).

Clone the four confirmed new ones:

```bash
mkdir -p ~/repos/top-agent-skills && cd ~/repos/top-agent-skills
git clone --depth=1 https://github.com/obra/superpowers
git clone --depth=1 https://github.com/multica-ai/andrej-karpathy-skills
git clone --depth=1 https://github.com/affaan-m/everything-claude-code
git clone --depth=1 https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
```

`superpowers` and `everything-claude-code` are both full Claude Code
harness/methodology packages (agents, commands, skills, hooks) rather than a
single skill file — read their own README before copying anything into
`.claude/` wholesale, since both are opinionated about directory layout and
may collide with this repo's existing 194 skills / 350+ commands.
