# business
Collect Claude material for buiness

## Skills

A starter bundle of business-oriented Claude skills lives in `.claude/skills/`:

- `sales-enablement` — pitch decks, one-pagers, objection handling, MEDDPICC/MEDDIC/BANT
- `business-decision-frameworks` — MoSCoW, RICE, OKRs, Kano, roadmap formats, Minto Pyramid
- `quarterly-okr-architect` — quarterly/annual goal architectures (4DX, MASTER, DUMB, backward planning)
- `business-intelligence-report` — reports for managers/CEO on results, trends, predictive analysis
- `ceo-reporting-skill` — growth/business reports for the CEO (Greek healthcare context)
- `product-marketing-context` — product/audience/positioning context doc used by other marketing skills
- `competitor-profiling` — structured competitor research and profiles
- `content-strategy` — content planning, topic clusters, editorial calendars
- `internal-comms` — company newsletters, FAQs, general internal communications
- `doc-coauthoring` — structured workflow for co-authoring docs, proposals, and specs
- `attachment-intake` — how to handle uploaded files (zips, photo batches, docs) that arrive with no or mismatched instructions, instead of guessing at intent
- `design-dev-resources` — curated directory of free design/frontend tool sites (unDraw, SVGL, Aceternity, Glassmorphism generator, JSON Crack) plus notable external AI tools (Genspark, Google Stitch, Google Flow, Gumloop, Figma Make) worth knowing about

A design/output bundle sits alongside it, for turning business content into actual visual deliverables:

- `frontend-design` — distinctive, production-grade web components/pages/artifacts
- `web-artifacts-builder` — complex multi-component HTML artifacts (React/Tailwind/shadcn)
- `canvas-design` — static poster/art pieces (.png/.pdf), ships with real fonts
- `theme-factory` — 10 preset visual themes (colors/fonts) applicable to any artifact
- `premium-html-presentation` — cinematic, dark-mode HTML slide decks
- `the-design-system-prompt` — an alternative cinematic-HTML-deck prompt (secondary to `premium-html-presentation`)
- `campaign-page-one-shot` — one-shot marketing landing pages
- `brand-guidelines` — **Anthropic's own** brand colors/fonts specifically, not a generic client-branding tool (see caveat in the skill itself)
- `pptx` / `docx` / `xlsx` / `pdf` — editable PowerPoint, Word, Excel, and PDF file creation/editing

A third bundle covers **setting up a new business** — validating an idea and turning someone's own expertise into a sellable product/service before (or instead of) building a team-scale product:

- `product-strategy-session` — full positioning → discovery → roadmap process for validated direction before committing to execution
- `saas-idea-validator` — critical, non-cheerleading stress-test of a new product/software/service idea (problem-solution fit, market, competition, moat, specific failure mode)
- `the-specific-knowledge-excavator` — reverse-engineers a person's unique intersection of expertise nobody else holds in the same combination
- `the-productize-yourself-blueprint` — converts that expertise into a scalable product/service format that sells without the founder's live presence
- `the-leverage-stack-auditor` — diagnoses whether a business idea is actually leveraged (media/code) or just relabeled labor
- `content-repurposing-service` — a concrete worked example: a productized weekly service that turns one client recording into a 7-asset content pack (carousel, video outlines, email, text posts) on a Mon–Fri cadence

A fourth pair covers **personal AI infrastructure** — setting up Claude Code itself as a tool, rather than producing business deliverables:

- `advisory-board` — set up a personal "council of experts" (named advisors + their real source material) that the `/ask-the-board` command draws on
- `ai-discoverable-site` — make a personal/company site readable by AI assistants (semantic HTML, meta descriptions, `llms.txt`, `robots.txt`, an "Ask AI about me" cross-provider block)
- `humanizer` — strips AI-writing tells (inflated symbolism, promotional language, em dash overuse, filler phrases, etc.) from drafted text; vendored for real from [blader/humanizer](https://github.com/blader/humanizer) (MIT)
- `claude-code-tooling` — curated directory of external Claude Code tools (a design-engine desktop app, a senior-engineer skill pack, multi-agent orchestration, a skills package manager, an agent context/memory database) that are standalone software, not skill files, so they're documented here rather than vendored in

Drop this repo into a Claude Code project (or point `.claude/skills` at it) to make these available.

## Commands

Slash commands live in `.claude/commands/` — unlike skills (which Claude loads
automatically when relevant), commands are invoked explicitly by name:

- `/ask-the-board [question]` — answers a question using the advisory board set up by the `advisory-board` skill; refuses to improvise generic advisor impressions if no board has been configured yet
- `/improve-system` — reviews the current session for one genuine, durable behavioral signal (not a transcript summary) and persists it to a `memory/` file, updating the memory index

**Skill vs. command, in this repo:** a skill is background knowledge/procedure
Claude reaches for when relevant ("how do I structure a quarterly OKR cascade");
a command is something the user explicitly invokes by typing `/name` ("run my
board" / "reflect on this session now"). `advisory-board` (skill) documents
*how to set up* the board; `/ask-the-board` (command) is *how you use it* once
set up.

### How the skills connect

Each `SKILL.md` has a "Related skills in this repo" (or annotated "Related
Skills") section pointing at the others that feed it or consume its output:

- `product-marketing-context` is the foundational doc: `sales-enablement`,
  `competitor-profiling`, `content-strategy`, and the design skills (for the
  user's *actual* brand, not `brand-guidelines`) all pull from it.
- `business-decision-frameworks` prioritizes initiatives/topics that feed
  `quarterly-okr-architect` (goal cascades) and `content-strategy` (editorial
  calendars).
- `quarterly-okr-architect` sets the targets that `business-intelligence-report`
  and `ceo-reporting-skill` report progress against.
- `business-intelligence-report` and `ceo-reporting-skill` are a pair —
  the former is the general BU-manager version, the latter is specialized for
  a Greek MedTech CEO audience.
- `content-strategy` decides what to write; `doc-coauthoring` (long-form) and
  `internal-comms` (short-form) draft it; `docx`/`pdf` produce the final file.
- `competitor-profiling` feeds both `sales-enablement` (battle cards) and
  `content-strategy` (competitive content gaps).
- Any of the reporting/planning skills can hand off to `pptx`, `premium-html-presentation`,
  or `xlsx` to become an actual deck or workbook, then `pdf` to export it.
- `design-dev-resources` supplies real icons/illustrations/logos to
  `frontend-design`, `web-artifacts-builder`, `canvas-design`, and
  `campaign-page-one-shot` instead of hand-drawn SVG.
- For a brand-new business: `the-specific-knowledge-excavator` finds the
  expertise → `the-productize-yourself-blueprint` turns it into a product/service
  format → `saas-idea-validator` / `product-strategy-session` stress-test it →
  `the-leverage-stack-auditor` checks it's actually leveraged →
  `product-marketing-context` captures the validated positioning → the rest of
  the business/design/output skills take over from there.
  `content-repurposing-service` is a ready-made example of running that whole
  chain and landing on a productized content service.

- For personal AI setup: `advisory-board` supplies advisors that
  `product-strategy-session`, `quarterly-okr-architect`, and the new-business
  cluster can sanity-check decisions against via `/ask-the-board`.
  `ai-discoverable-site` pulls its "who they are" content from
  `product-marketing-context` and hands implementation to `frontend-design`.

- `humanizer` is a general-purpose editing pass — run it on drafts from
  `sales-enablement`, `content-strategy`, `doc-coauthoring`, `internal-comms`,
  or `content-repurposing-service` before delivering them.

`attachment-intake` and `claude-code-tooling` are separate, meta-level skills
and aren't part of this content chain.

### ⚠️ `brand-guidelines` applies Anthropic's brand, not the user's

That skill is hardcoded to Anthropic's own colors (`#d97757` orange, etc.) and
fonts (Poppins/Lora) — it's for artifacts that should carry *Anthropic's*
look-and-feel specifically. For the user's own company or client branding, use
`product-marketing-context` to capture their real brand and apply it manually
in the design skills instead.

## Procedures

Standard operating procedures live in `docs/procedures/`:

- `attachment-intake.md` — inspect an unlabeled/ambiguous attachment before
  acting, ask a grounded clarifying question, and don't force-fit mismatched
  answers onto the file. Backs the `attachment-intake` skill above.
