# Batch 108 — iCloud Photos, one archive (35 images, no video) (13 October 2026)

File names on disk use the physical numbers 111 and 112 (`scripts/batch111-install.sh`, `Artifacts/business/batch-112-intake-report.html`); the README sequence calls this Batch 108. It follows Batch 107 on the same branch and pull request.

## 1. What was in the archive

| Creator | Images | Subject | Result |
|---|---|---|---|
| @modelsignal | 12 | "10 free GitHub repos replacing $100M+ software companies, Part 2": 10 paid-vs-free swaps, a price summary and a "Comment GIT" call to action | Skill `oss-swap-savings-table-10`, command `/swap-savings`, template `compare-paid-free-card-red` |
| @buildwithneej | 11 | "5 GitHub repos that took off this week": hypit, open-code-review, colibri, tinycast, security-audit-skill, plus intro, verdict table and a "Comment REPO" call to action | Skill `agent-repos-took-off-sep-2026`, command `/repo-week-pick` |
| @claude.with.christelle | 3 | "20 things to have Claude check before you launch your website" with a one-prompt audit | Skill `prelaunch-website-audit-20`, command `/prelaunch-audit`, script `scripts/prelaunch_check.py`, template `checklist-dark-copper-grid`, theme `theme-dark-copper-serif` |
| @entr3p2 | 6 | "Useful websites for your business": Calendly, SERPtag, Google Business Profile, Wave, Tally | Skill `free-business-websites-5`, command `/biz-sites-pick`, template `website-pick-card-clean` |

Images counted by creator group: 12 + 11 + 3 + 6 = 32. The other 3 of the 35 are cover and call-to-action slides that belong to the @modelsignal and @buildwithneej series and are folded into those two series. All 35 were read.

## 2. What was created

| Kind | Items |
|---|---|
| Skills (4) | `prelaunch-website-audit-20`, `oss-swap-savings-table-10`, `agent-repos-took-off-sep-2026`, `free-business-websites-5` |
| Commands (4) | `/prelaunch-audit`, `/swap-savings`, `/repo-week-pick`, `/biz-sites-pick` |
| Script (1) | `scripts/prelaunch_check.py`: stdlib checker for the items of the 20-point list that HTML can decide; tested on a deliberately bad page (12 FAILs) and on `Artifacts/index.html` |
| Design (3 templates + 1 theme) | `compare-paid-free-card-red`, `checklist-dark-copper-grid`, `website-pick-card-clean`, `theme-dark-copper-serif` (Aptos first in the font stack, light and dark; rendered to check) |
| User-run script | `scripts/batch111-install.sh` (asks before every step; no piped installs) |

## 3. What was verified, and what was not

- README and LICENSE files of 15 repos were fetched and read; the tinycast owner and licence and the Seafile licence were checked through search and the repo where possible.
- SkillSpector (static, `--no-llm`) on the 4 new skills and the checker script: three scored 0 with no listed issues (two of them still rated "CAUTION" by the tool, reason not shown), `agent-repos-took-off-sep-2026` scored 10 (two generic "MCP rug pull" medium flags with no snippet), `free-business-websites-5` and the script scored 0 "SAFE". Findings not suppressed.
- Not re-checked: all paid prices, star counts, "stars this week" figures, memory figures for tinycast, "installs into 75 agents".

## 4. Source problems

- **Arithmetic:** the @modelsignal closing slide says "8 of 10" and "Save $3,012 a year"; its 8 listed rows add to $2,856. $3,012 is the sum of all ten swaps. All prices are single-seat.
- **Typo-squatting risk:** the @buildwithneej tinycast slide spells the Homebrew tap `abu-ammar/tinycast`; the real owner is `abue-ammar`.
- **Outdated release:** colibri's slide shows v1.11.0; its README header shows v2.0.0.
- **Licences not stated on slides:** hypit uses a modified Apache-2.0 with extra conditions; AppFlowy and tinycast are AGPL-3.0; Activepieces is MIT except its `ee` folders; Odoo Community is LGPL-3.0 and Enterprise is proprietary.
- **Not obtained:** Qdrant's LICENSE file and Seafile's server repo could not be fetched; both are marked unconfirmed in the skill.
- **Comment-gated:** both repo series end in "comment a word and I will send the links"; the full breakdowns were not obtained and were not invented.
- **Tax rule:** Wave is not suitable by default for Greek e-invoicing; confirm with an accountant.

## 5. Not done

Nothing was installed on any machine and no connector was changed. Pending from before: the Agent Archive account question, and whether to make the SkillSpector pre-install scan a standing step.
