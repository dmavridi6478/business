# Batch 109 — iCloud Photos (14 images, no video) plus one infographic attached in chat (13 October 2026)

File names on disk use the physical numbers 112 and 113 (`scripts/batch112-install.sh`, `Artifacts/business/batch-113-intake-report.html`); the README sequence calls this Batch 109. It follows Batch 108 on the same branch and pull request.

## 1. What was in the archive

| Creator | Images | Subject | Result |
|---|---|---|---|
| @danielmofi1 | 9 | "7 best AI tools for coding": cover, seven tool slides (Cursor, Claude Code, GitHub Copilot, Windsurf, Replit Agent, Aider, Gemini Code Assist) and a "Comment CODING for setup guide" closing slide | Skill `ai-coding-tools-7-ranking-2026`, command `/coding-tool-pick`, template `ranked-tool-card-black-blue`, theme `theme-black-electric-blue` |
| @githubnow | 5 | Daily briefing of 13 October 2026: open-code-review, xtool, vercel-labs/skills, plus cover and closing slides | Skill `github-briefing-oct13-three`, command `/briefing-oct13-pick` |
| Chat image (Charlie Hills) | 1 | "How to Make LinkedIn a Landing Page" | Skill `linkedin-landing-page-checklist`, command `/linkedin-landing-page`, template `annotated-callout-map-navy` |

9 + 5 = 14 archive images, all read, plus the chat image.

## 2. What was created

| Kind | Items |
|---|---|
| Skills (3) | `ai-coding-tools-7-ranking-2026`, `github-briefing-oct13-three`, `linkedin-landing-page-checklist` |
| Commands (3) | `/coding-tool-pick`, `/briefing-oct13-pick`, `/linkedin-landing-page` |
| Design (2 templates + 1 theme) | `ranked-tool-card-black-blue`, `annotated-callout-map-navy`, `theme-black-electric-blue` (Aptos first, light and dark, rendered to check) |
| User-run script | `scripts/batch112-install.sh` (asks before every step, scans before installing, no piped installs) |

Not duplicated: the @githubnow look is already covered by `social-card-github-daily-briefing` and `theme-github-night-green`.

## 3. What was verified, and what was not

- Verified from the repos: Aider is Apache-2.0 and its README install is `python -m pip install aider-install` then `aider-install`; xtool is MIT; vercel-labs/skills is MIT and its "79 agent targets" equals the README's four named agents plus 75 more; `skills use` prints a prompt without installing; open-code-review is Apache-2.0 (read in Batch 108).
- SkillSpector, static mode, standing step applied:
  - `vercel-labs/skills` whole repo: 100/100 CRITICAL, 326 findings, 66% coverage. `xtool-org/xtool` whole repo: 100/100 CRITICAL, 163 findings, 98% coverage.
  - I opened nine locations (eight rated high); every one was ordinary text or build code. I did not read the other 480 findings, so neither repo is cleared. They are unaudited software; the scanner is built for skills, not whole repositories.
  - Own new skills: `ai-coding-tools-7-ranking-2026` 0, `linkedin-landing-page-checklist` 0, `github-briefing-oct13-three` 73 on the first run (it quoted trigger phrases from the repos), reworded and rescanned to 10 with one remaining finding: an unpinned `npx skills` reference, which the skill already tells you to pin. Findings were not suppressed.
- Not re-checked: all prices, star counts, benchmark figures, LinkedIn image sizes, the Premium status of the custom button, the Windsurf ownership note (from memory), the Copilot extensions model.

## 4. Source problems

- The coding-tool mock-ups look invented: a "Claude Code v1.2 research preview" terminal with typos, an Aider `--model a,b,c` line the README does not document, Kotlin code calling `applyTerraform()`, and unsourced figures ("+28%", "-$120/mo", "42 extensions").
- The Claude Code "fix" lets tokens through for 60 seconds after expiry. That is a policy choice presented as a bug fix.
- The open-code-review table (vendor benchmark) shows about 25% F1 at best: roughly one in five issues found.
- "Codeium team" for Windsurf is probably outdated.
- Comment-gated: "Comment CODING for setup guide" was not obtained and not invented.
- The LinkedIn slide's "use this prompt to template other creators' About sections" shows no prompt; the skill carries my own audit prompt, marked as mine.

## 5. Connectors

Copilot's slide mentions Jira and Sentry. Jira: the Atlassian connector is already available in this session. Sentry: not connected, and OAuth cannot be started from here, so you would need to authorise it. Nothing was changed.

## 6. Not done

Nothing was installed on any machine. Pending: the Agent Archive account question. Decided this session: the SkillSpector scan is a standing step (`CLAUDE.md`, commit `607ef82`).
