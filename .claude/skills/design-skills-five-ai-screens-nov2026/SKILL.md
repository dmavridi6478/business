---
name: design-skills-five-ai-screens-nov2026
description: Checked register of the five free design skills in the @jaytownley.design carousel "5 free skills to make AI-looking screens look designed" - unslop, Web Design Engineer (garden-skills), hue, Open Design Agent Kit, Color Expert - with licences and install lines read from each repo README, where the slide's install line differs from the README, what each skill is for, and the cautions the slides omit (CC BY attribution, a collection repo behind one name, a hosted variant that sends designs to a third-party server, vendored brand systems). Use when a Claude Code or Codex build looks generic and you want a skill to fix the look, or before installing any of the five.
---

# Five design skills for AI-built screens (carousel read 25 November 2026)

Source: 7 slides by @jaytownley.design ("For designers using AI", each marked "Checked 16 Nov 2026"). Repos, default branches, licence files and READMEs were read on 25 November 2026. Star counts on the slides (unslop 16.9k, garden-skills 15.2k whole repo, hue 910+, Open Design Agent Kit 1.1k, Color Expert 650+; "34k+ between them") were **not** verified: the GitHub API is blocked from the build environment. The slide arithmetic does add up (about 34.8k).

| # | Skill | Repo (branch) | Licence (read) | What it does (README) |
|---|---|---|---|---|
| 1 | unslop | `heydamir/unslop` (main) | CC BY 4.0 | Finds AI tells (purple gradients, glows, emoji labels, shouty copy, uneven spacing), sets a direction, then fixes the screen pass by pass. Claude Code, Codex, Google Antigravity |
| 2 | Web Design Engineer | `ConardLi/garden-skills` (main) | MIT | Declares a design system first, shows an early v0, builds, then verifies. One skill inside a collection |
| 3 | hue | `dominikmartn/hue` (main) | MIT | Learns a brand from a URL, name or screenshot and writes a design-system skill. Claude Code and Codex |
| 4 | Open Design Agent Kit | `feimacode/open-design-agent-kit` (main) | MIT | Brings Open Design's content (README: 181 skills, 114 design templates, 198 brand design systems, 193 remixable examples, 13 craft docs) into Claude Code, Codex, Copilot, Cursor via plugin, MCP or npx |
| 5 | Color Expert | `meodai/skill.color-expert` (main) | CC BY 4.0 for original files; third-party material keeps its own licence | Colour theory, spaces, contrast and accessibility, backed by about 185 reference files |

## Where the slide and the README disagree

| Skill | Slide line | README says | Consequence |
|---|---|---|---|
| unslop | `/plugin marketplace add heydamir/unslop` | That adds the marketplace only; then `claude plugin install unslop@heydamir`, then `/reload-plugins` or a new session | Running only the slide's line installs nothing |
| unslop | CC-BY-4.0, "Free" | Free to use and change, including commercially, if you credit Damir Sokolovsky and link the repo | Attribution is a condition, not a courtesy |
| Web Design Engineer | `npx skills add ConardLi/garden-skills` | The repo holds several skills (motion-showreel, web-video-presentation, web-design-engineer and others) | The slide's command installs the collection; the 15.2k stars belong to the whole repo |
| hue | "Get it hueapp.io" | Install is `git clone` of the repo into `~/.claude/skills/hue` (Codex path also given) | The website demos it; the install is a clone |
| Open Design Agent Kit | `npx @feimacode/open-design-agent-kit init` | Correct; the README also lists a Claude Code plugin route and a hosted variant (`open-design-hosted`) where designs live on the author's server | Choose local or hosted knowingly (see cautions) |
| Color Expert | CC-BY-4.0 | CC BY 4.0 covers README, SKILL.md and INDEX only; source-derived reference content keeps its original licence (THIRD_PARTY_NOTICES.md) | Do not redistribute the reference folder as if it were all CC BY |

## Which one for which job

| Job | Start with | Why |
|---|---|---|
| A finished screen looks "AI" | unslop | It audits first, then fixes in ordered passes |
| New page, want a design system declared before code | Web Design Engineer | Context, system, v0, build, verify |
| Make the build match a real brand (yours or a client's) | hue | Brand in, design-system skill out; use a brand you are allowed to imitate |
| Start from rendered examples, decks, dashboards | Open Design Agent Kit | Remix an example instead of a blank prompt |
| Palette, contrast or accessibility question | Color Expert | Reference-backed answers |

Existing repo skills that overlap: `claude-design-skills-top5` (Taste, Impeccable, UI UX Pro Max, frontend-design), `better-colors`, `design-dna`, `design-token-extractor`, `hallmark`, `taste`. Try those first; these five are additions, not replacements.

## Cautions the slides omit

1. **Skills can run code and commands.** unslop can drive Playwright and ffmpeg for live-site snapshots and story videos; the Open Design kit registers an MCP server through `npx`. Read the SKILL.md and the package before installing, and prefer project scope (`--scope local`) to global.
2. **Hosted variant sends your designs away.** `open-design-hosted` keeps designs on the author's server and returns links. Do not use it for client work under NDA.
3. **Brand design systems are other companies' looks.** Copying a real brand's visual identity for your own product risks trademark and passing-off problems. Check what the 198 systems are before shipping anything that resembles them.
4. **Attribution.** unslop and Color Expert (original files) are CC BY 4.0: keep the credit if you copy, change or share them.
5. **No results shown.** None of the slides shows before/after evidence or a measured outcome; run one skill on one screen and compare yourself.
6. **Do not stack all five at once.** Overlapping instructions fight each other; pick one process skill (unslop or Web Design Engineer) plus at most one reference skill (Color Expert).

## Not done

Nothing cloned, installed or run. Star counts, the README counts (181, 114, 198, 193, 185) beyond what the READMEs state, and any quality claim were not tested. Use `/design-skill-pick` to choose, `/repo-vet owner/repo` and `/repo-licence-check` before installing.
