# GitHub Trending — Agent & Research Skill Repos (Sept 2026)

Source: @githubnow (TikTok), "Daily Briefing · Open Source · 23 September
2026 — Your agents just leveled up." Three repos gaining stars fast on the
day of the post; all three confirmed live via `git ls-remote`.

| Repo | Stars (source day) | What it does |
|---|---|---|
| [`K-Dense-AI/scientific-agent-skills`](https://github.com/K-Dense-AI/scientific-agent-skills) | +7,370 that week | Turns any AI agent into an AI scientist: 166 validated skills plus 100+ scientific databases for genomics, drug discovery, molecular dynamics, microbiome analysis, and more. Follows the open Agent Skills standard — compatible with Claude, Cursor, Codex. Flow: research task → skill lookup → query/execute → scientific result. |
| [`freestylefly/awesome-gpt-image-2`](https://github.com/freestylefly/awesome-gpt-image-2) | +19,065 that month | Prompt-as-code library: 530+ image-generation examples, 20+ production-ready industrial prompt templates, and a web gallery to browse/filter/compare/copy exact prompts with their generation records. Reusable across DALL-E, Midjourney, and GPT Image. |
| [`HKUDS/CLI-Anything`](https://github.com/HKUDS/CLI-Anything) | +41 that day | Agent-native CLI generator: makes any existing software agent-ready by generating CLIs that AI agents control via JSON-structured commands. Handles UI parsing, CLI generation, and validation automatically. Ships a CLI Hub registry (`pip install` community CLIs), 2,461 tests, 18+ supported apps (CAD, design, productivity, multimedia). |

Note: `K-Dense-AI` also publishes `science-superpowers` (a Superpowers-style
methodology skill for computational science, 339★) — a different repo from
`scientific-agent-skills` above, surfaced during verification but not part
of this source carousel.

## Clone

```bash
mkdir -p ~/repos/github-trending-sep2026 && cd ~/repos/github-trending-sep2026
git clone --depth=1 https://github.com/K-Dense-AI/scientific-agent-skills
git clone --depth=1 https://github.com/freestylefly/awesome-gpt-image-2
git clone --depth=1 https://github.com/HKUDS/CLI-Anything
```

`scientific-agent-skills` is the most directly installable one for this
repo — it follows the same Agent Skills format already used in
`.claude/skills/`. If this business does any scientific/technical research
work, copy the relevant skill subfolders in rather than the whole 166-skill
pack.
