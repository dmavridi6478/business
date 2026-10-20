# 13 Claude Skills That Save You Hours Every Week

Source: GenAI Works infographic, "verified September 2026." One file each,
zero re-prompting — install once, Claude fires them on its own without
being asked.

Two of the 13 below (`/frontend-design`, `/doc-coauthoring`) and the "install
first" `/skill-creator` are already installed in this repo's `.claude/skills/`.
The rest are genuinely new — either install the ones you want the same way
this repo's other vendored skills were added (clone the source repo, copy its
`SKILL.md` into `.claude/skills/<name>/`), or ask Claude to build an
equivalent from the one-line description below via `/skill-creator`.

---

## Install first

| Skill | What it does |
|---|---|
| **Find skills** — `npx skills find` | The most-installed skill on skills.sh, by Vercel Labs. Ask "is there a skill for X" and it finds and installs the match. This repo's own `capability-scout` agent and `audit-my-workflow-for-skills` command cover the same job locally, without the npx dependency. |
| **Skill creator** — `/skill-creator` | Anthropic's builder. Turns the standards your team repeats in every prompt into one file Claude follows, then tests it. Already present as `anthropic-skills:skill-creator`. |

## The 13

| # | Skill | Slash | What it does | Example prompt |
|---|---|---|---|---|
| 01 | Grill me | `/grill-me` | Interviews you until every branch of the plan is resolved. Nothing gets built on a vague brief. | "Grill me on this before we touch anything." |
| 02 | Brainstorming | `/brainstorming` | Fires the moment you start building. Asks what you actually want, then shows the design in chunks you can sign off. | "Let's build a client onboarding tracker." |
| 03 | Writing plans | `/writing-plans` | Turns the approved design into 2-5 minute tasks with exact files and verification steps. | "Write the implementation plan for this design." |
| 04 | Doc co-authoring | `/doc-coauthoring` | Co-writes specs and decision docs in three stages, then tests the doc on a fresh Claude with zero context. **Already installed** as `doc-coauthoring`. | "Help me write the decision doc for the pricing change." |
| 05 | Systematic debugging | `/systematic-debugging` | Four-phase root-cause loop: reproduce, hypothesise, gather evidence, fix. No random-code changes. | "Checkout fails one time in ten. Debug it properly." |
| 06 | Research | `/research` | Investigates a question against primary sources and saves a cited Markdown file, running in the background. This repo's `agentic-researcher` agent and `research-and-self-factcheck`/`verified-research` commands already cover this. | "Research how competitors price annual plans, with sources." |
| 07 | Discernment nudge | `/discernment-nudge` | After any answer you might act on, adds 2-3 questions that make you check the facts, the logic, and what it assumed. | "Should we move the launch to Q1?" |
| 08 | Document skills | `/docx` `/pptx` `/xlsx` `/pdf` | The exact skills behind Claude's file creation — Word with tracked changes, real decks, live formulas, PDF forms. **Already installed** as `docx`/`pptx`/`xlsx`/`pdf`. | "Turn these notes into a 10-slide deck." |
| 09 | Frontend design | `/frontend-design` | Distinctive, production-grade UI instead of the default AI look. **Already installed** as `frontend-design`. | "Design the landing page. No template look." |
| 10 | Test-driven development | `/test-driven-development` | Failing test first, minimal code second, then refactor and commit. Deletes code written before tests. | "Add the export feature. TDD." |
| 11 | Humanizer | `/humanizer` | Strips the AI tells — not-X-but-Y contrasts, forced triads, dashes everywhere, inflated claims. Keeps what it says. **Already installed** as `humanizer`. | "Humanize this draft." |
| 12 | Handoff | `/handoff` | Compacts the whole chat into a handoff document so the next session, or another agent, continues without re-explaining. This repo has a generic `/handoff` command already — check it covers the same ground before adding a second one. | "Write the handoff, I'm out of context." |
| 13 | Teach | `/teach` | Teaches a skill over multiple sessions, using your folder as a classroom that remembers where you stopped. Overlaps this repo's `learn-topic`/`teachback`/`micro-curriculum` commands — compare before installing as a separate skill. | "Teach me SQL joins. Session one." |

## What's actually new to install

Not already present in this repo: `grill-me`, `brainstorming`,
`writing-plans`, `systematic-debugging`, `discernment-nudge`,
`test-driven-development`. Ask `/skill-creator` to build any of these from
its one-line description above, or search `npx skills find <name>` on your
own machine (not inside this sandboxed environment) if you want the exact
upstream version.
