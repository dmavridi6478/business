# Batch 110 — iCloud Photos (25 images, no video) plus two infographics attached in chat (14 October 2026)

File names on disk use the physical numbers 113 and 114 (`scripts/batch113-install.sh`, `Artifacts/business/batch-114-intake-report.html`); the README sequence calls this Batch 110. It follows Batch 109 on the same branch and pull request.

## 1. What was in the batch

| Source | Images | Subject | Result |
|---|---|---|---|
| @modelsignal | 14 | "Save $6,846/year, use these free tools instead" (Part 9): cover, 12 swap slides, summary | Skill `oss-swap-savings-table-12-part9`; `/swap-savings` now covers Part 2 and Part 9; template `compare-paid-free-card-red` already existed (Batch 108) |
| @replace.so | 6 | "6 GitHub repos so good they shouldn't be free": cover and five repos (Convex, LimeSurvey, Prismical, Coder, Harper) | Skill `replace-so-six-repos-oct-2026`, template `repo-pick-card-pixel-grid-dark` |
| @githubnow | 5 | Second briefing of 13 October 2026: morluto/rea, tashfeenahmed/freellmapi, agent-substrate/substrate | Skill `github-briefing-oct13-rea-freellmapi-substrate`; `/briefing-oct13-pick` now covers both briefings |
| Chat image 1 | 1 | "Machine Learning Algorithms" cheatsheet, 16 rows | Skill `ml-algorithms-cheatsheet-16`, command `/ml-algo-pick`, template `cheatsheet-table-navy-matrix` |
| Chat image 2 | 1 | Prosp "Claude Skills for B2B Sales", 50 skills in 7 folders | Skill `claude-skills-b2b-sales-50-map`, command `/b2b-sales-skill`, agent `b2b-sales-stage-router`, template `skill-folder-explorer-dark`, theme `theme-claude-orange-night` |

14 + 6 + 5 = 25 archive images, all read, plus the two chat images.

## 2. What was created

| Kind | Items |
|---|---|
| Skills (5) | `oss-swap-savings-table-12-part9`, `replace-so-six-repos-oct-2026`, `github-briefing-oct13-rea-freellmapi-substrate`, `ml-algorithms-cheatsheet-16`, `claude-skills-b2b-sales-50-map` |
| Commands (2 new, 2 updated) | New: `/ml-algo-pick`, `/b2b-sales-skill`. Updated: `/swap-savings`, `/briefing-oct13-pick` |
| Agent (1) | `b2b-sales-stage-router` (read-only; routes a deal to a stage and names an installed skill; drafts only) |
| Design (3 templates + 1 theme) | `cheatsheet-table-navy-matrix`, `skill-folder-explorer-dark`, `repo-pick-card-pixel-grid-dark`, `theme-claude-orange-night` (Aptos first, light and dark, rendered to check) |
| User-run script | `scripts/batch113-install.sh` (asks before every step, scan helper, no piped installs, registers nothing) |

## 3. What was verified, and what was not

- Read from the repos on 14 October 2026 (README and LICENSE): rea, freellmapi, substrate, convex-backend, LimeSurvey, coder, harper, meltano, dittofeed, fider, cvat, freescout, rabbitmq-server, OpenSign, Zettlr, miniflux, bagisto, AdGuard Home (WordPress: licence file only). Prismical's repo was found afterwards (`amicalhq/prismical`, MIT).
- Not obtained: stars, "pushed N days ago" and developer counts on the slides (the GitHub API is out of reach in this session); all paid prices; the contents behind "Comment FREE" and "Comment SALES".
- SkillSpector, static, standing step applied:
  - REA's agent skill folder: 40, MEDIUM, 12 findings (five real: the unpinned package run; the rest documentation text).
  - REA whole repo and its installer scripts: no result, both scans timed out. FreeLLMAPI scripts, Dockerfile and compose file: 100, CRITICAL, 23 findings, mostly environment-file handling plus one real design fact (automatic updates). Agent Substrate scripts: nothing to scan, so not a clean result.
  - New skills: `oss-swap-savings-table-12-part9` 0, `replace-so-six-repos-oct-2026` 0, `ml-algorithms-cheatsheet-16` 0, `claude-skills-b2b-sales-50-map` 0, `github-briefing-oct13-rea-freellmapi-substrate` 89 on first run (it quoted the risky commands it warns about), reworded and rescanned to 7 with one remaining finding (the setup command, which the skill tells you to run only on your own machine). Agent `b2b-sales-stage-router`: 8, one finding: it lists skills, by design. Nothing suppressed.

## 4. Source problems

- **Arithmetic (again):** all 12 swaps add to $6,846; the eight listed on the summary slide add to $6,600. The $246 difference is Ecwid, Ulysses, Inoreader and Control D.
- **"Open source" claim:** Convex is under the Functional Source License 1.1 (Apache 2.0 after a delay), not an open-source licence, although the slide and README call it open source. Self-hosted builds contain a beacon.
- **Prismical (resolved later):** the slide shows no URL. A directory listing gave `amicalhq/prismical`; its LICENSE is MIT. The 104-star figure matches the directory, which labels it "last 30 days".
- **Cover count:** @replace.so says six repos; five are in the archive.
- **Stale maintenance:** OpenSign is marked "pushed 52 days ago" while the slide still says "Switch this one".
- **Small swaps cost more than they save:** five of the 12 are $24 to $120 a year.
- **REA:** its README example prompt asks the agent to understand an app and build a similar feature; its own disclaimer rules out copying protected code and bypassing licence checks. It ships a piped installer and its skill runs an unpinned package.
- **FreeLLMAPI:** routes prompts to up to 34 third parties; single-user by its own compose file; optional automatic image updates; Premium catalog is $19 a year.
- **ML cheatsheet:** mostly sound; loose or wrong entries are listed in the skill (Random Forest "tree independence", KNN "few-shot", Transformer "fast", RNN "stock prediction").
- **B2B sales graphic:** titles only; the skill files are behind "Comment SALES" and were not obtained, so the skills in this repo are mapped to installed ones and a method of my own.

## 5. Connectors and installs

REA is an MCP server and a connector installation. It was not installed: it edits agent configuration, needs your own Hopper, Ghidra or IDA for native work, and is dual-use. The script prints the safer route (pinned, after reviewing the proposed diff) and registers nothing. No other connector is referenced.

## 6. Not done

Nothing was installed on any machine. Agent Archive was dropped at your request after its sign-up endpoint failed.
