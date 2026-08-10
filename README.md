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

Drop this repo into a Claude Code project (or point `.claude/skills` at it) to make these available.

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

`attachment-intake` is a separate, meta-level skill and isn't part of this
content chain.

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
