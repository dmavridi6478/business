# Batch 98 — Action Plan (iCloud Photos ×36 + "The 8 Ps of Sales" ×5)

Inputs: 36 TikTok/Instagram card screenshots (Sep 2026) and 5 infographics/screenshots. Sources: @the.wealth.lab, @earchoe, @githubnow, @theromanknox, @your.aimentor, @unifybrowse-style "save for later" tool cards, SalesDaily.co, Kinetyca (Matteo Fois), Beloved Brands, smarterwithai.news.

Confidence tags: **[Certain]** verified by me in this session · **[Likely]** strong inference · **[Guessing]** filled gap.

## 1. What was created and installed in this repo

| Type | Name | Source | Invoke |
|---|---|---|---|
| Skill + command | `eight-ps-of-sales` | SalesDaily 8 Ps infographic | `/8ps-audit` |
| Skill + command | `ai-gtm-maturity-levels` | Kinetyca "5 Levels of AI in GTM" | `/gtm-ai-level` |
| Skill + command | `brand-positioning-zones` | Beloved Brands Venn | `/positioning-zones` |
| Skill + command | `prompting-frameworks-8` | smarterwithai.news (TRACE, TAG, RTF, CLEAR, PACT, STAR, RISE, RASCEF) | `/prompt-frame` |
| Skill + command | `linkedin-prospecting-8-systems` | "LinkedIn Prospecting Guide to Claude" (cover + TOC only) | `/linkedin-systems` |
| Skill + command | `competitor-price-watchlist` | @earchoe 9-slide playbook | `/price-watchlist` |
| Command | `workflow-to-agent` | @the.wealth.lab steps 4–6 | `/workflow-to-agent` |
| Reference | `build-ai-agent-10-minutes/references/wealth-lab-6-step.md` | @the.wealth.lab 6-step carousel | (loaded by the skill) |
| Templates | see section 5 | design cards | `Artifacts/templates/` |
| Themes | see section 5 | design cards | `Artifacts/` |

## 2. "21 things to install in Claude" (@your.aimentor) — status

**[Certain]** The graphic's headline says 21, but it shows 18 items (6 plugins, 6 skills, 6 MCP), while its counters say "8 installed / 8 active / 8 connected". Star counts on the card are unverified.

| Item | Kind | Status here | How to install / connect |
|---|---|---|---|
| gstack | plugin/skill | Already installed (`.claude/skills/gstack`) | — |
| superpowers | plugin | Marketplace exists (verified) — not enabled; `claude-code-superpowers` command already present | `/plugin marketplace add obra/superpowers-marketplace` then `/plugin install superpowers@superpowers-marketplace` |
| codex-plugin-cc | plugin | Repo verified (`openai/codex-plugin-cc`); needs an OpenAI/Codex login, so not enabled | `/plugin marketplace add openai/codex-plugin-cc` |
| financial-services | plugin | Repo verified (`anthropics/financial-services`), not enabled | `/plugin marketplace add anthropics/financial-services` |
| claude-for-legal | plugin | Already referenced as installed suite; marketplace `anthropics/claude-for-legal` verified | `/plugin marketplace add anthropics/claude-for-legal` |
| marketingskills | plugin | Vendored in full (Corey Haines pack) | — |
| frontend-design, skill-creator, mcp-builder, hyperframes, claude-seo | skills | Already installed | — |
| find-skills | skill | **Not installed** — my attempt to vendor it was blocked by the permission classifier | `npx skills add vercel-labs/skills --skill find-skills` (MIT; `skills/find-skills/SKILL.md` verified fetchable) |
| Slack, Notion, Zapier, Higgsfield | MCP | Connected in this account [Certain] | — |
| Granola | MCP | Found in the registry, **not connected** — needs your OAuth in claude.ai | claude.ai → Settings → Connectors → Granola |
| Kondo (LinkedIn DM triage) | MCP | **Not in the connector registry** [Certain]; Taplio MCP LinkedIn is the nearest registered alternative and needs reconnect | Ask Kondo for an MCP endpoint; otherwise use Taplio |

Blocked actions (left for you): I tried to (a) add the four marketplaces above to `.claude/settings.json` `extraKnownMarketplaces` and (b) append four repos to `setup-repos.sh`. The permission classifier denied both (self-modification of agent config; untrusted code integration into a script that clones and runs code). Run the `/plugin marketplace add …` lines yourself if you want them.

## 3. GitHub repos (verified with `git ls-remote`, 2026-09-30) [Certain]

| Repo | What | Note |
|---|---|---|
| `ahujasid/blender-mcp` | MCP server: control Blender scenes from Claude (Python exec, objects, materials) | The card calls it `mcp-for-blender`; that name resolves to the same commit. Card says +3,209 stars this month (unverified). Clone: `git clone https://github.com/ahujasid/blender-mcp` |
| `PrismML-Eng/Bonsai-demo` | Bonsai 2 27B ternary-quantized reasoning model demo, 5.9 GB, vision, tool calling, `./setup.sh` | Card claims "98.2% FP16 parity", "262K context" — vendor claims, unverified |
| `oblien/openship` | Self-hosted CI/CD deploy platform (desktop/web/CLI) | Already in `docs/icloud-photos-action-plan.md` |
| `public-apis/public-apis` | Curated free-API list (APILayer card: 60K+ stars) | Skill `public-apis` already installed |
| Hackathon Projects / Hackathon Tools ("12.5k stars") | Curated hackathon lists | **[Guessing]** owner unknown; the mock GitHub UI on the card looks AI-generated (stars 12.5k header vs 3.5K+ stats). Not cloned. |
| Avani Codes ("610+ projects, 10 categories") | Curated OSS list | The card itself says "Stars Repo Not Found". Not cloned. |

## 4. Tools named (already covered)

AnswerThePublic, Exploding Topics, SERPtag, hunter.io — covered by `/seo-tools-hidden`, `entrepreneur-tool-directory`. **[Likely]** no new skill needed. The Wealth Lab "Digital Store" and follow-us cards are promotional; nothing to install.

## 5. Design content implemented

| File | Style source | Format |
|---|---|---|
| `Artifacts/templates/social-card-editorial-playbook.html` | @earchoe — beige paper, serif headings, mono body, red accent, dark code block | 1080×1920 slides |
| `Artifacts/templates/social-card-github-daily-briefing.html` | @githubnow — near-black navy, green accent, repo card | 1080×1920 |
| `Artifacts/templates/social-card-repo-showcase-warm.html` | @theromanknox — white pattern, brown→orange gradient headings, orange chips | 1080×1350 |
| `Artifacts/templates/infographic-framework-kit.html` | SalesDaily / Kinetyca / Beloved Brands — radial 8-step, 5-level pyramid, 3-circle Venn | 1080×1350 blocks |
| `Artifacts/theme-editorial-paper-red.html` | @earchoe | tokens + components |
| `Artifacts/theme-github-night-green.html` | @githubnow | tokens + components |

## 6. Prompts

All prompts from the photos, in plain text, are in `docs/batch-98-prompts.md`.

## 7. Not actioned

- "Claude Fable 5.1 / 3.7 Sonnet" screenshots inside cards show model names as decoration; nothing to act on.
- The LinkedIn guide's 80 skills are gated behind a "comment SYSTEMS" DM; only the structure was reproducible.
