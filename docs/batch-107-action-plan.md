# Batch 107 — iCloud Photos, two archives (49 images, 1 video) plus 3 images attached in chat (12 October 2026)

File names on disk use the physical number 110 (`scripts/batch110-install.sh`, `Artifacts/business/batch-111-intake-report.html`); the README sequence calls this Batch 107.

## 1. What was in the archives

| Creator | Images | Subject | Result |
|---|---|---|---|
| @aigenesis.official | 12 | "50 AI Automations Every Marketer Can Build This Weekend": cover, the stack, ten category slides | Skill `ai-automations-50-marketing`, command `/automation-pick`, template `automation-list-yellow-marker` |
| @githubnow | 10 | GitHub Trending, 12 October 2026: Open WebUI, BitNet, free-claude-code, AI Engineering from Scratch, WeKnora, diagram-design | Skill `oss-trending-picks-oct-2026`, command `/oss-pick-oct` |
| @awayfromlovable | 7 | Top 5 Claude Code add-ons by stars | Skill `claude-code-addons-top5`, command `/addon-pick` |
| @joshualevi.ai | 8 | "Nobody checked the skills you installed": NVIDIA SkillSpector in 7 numbered slides | Skill `skillspector-preinstall-scan`, command `/skill-scan` |
| @githubvault | 11 | 8 self-hostable tools plus a cover (Spotube, Spacedrive, MeTube, Stirling-PDF, Translumo, Glance, JumpServer, CryptPad, GeminiWatermarkTool, GitHub Store) | Same skill as @githubnow; template `social-card-vault-repo-mono`; theme `theme-github-vault-mono-starfield` |
| @boscokat | 1 | 5 Claude plugins for vibe coding | Skill `vibe-coding-plugin-layers-5` |
| @assmooorre.ai (video, 40 s) | 1 video | Laya (open source) vs Jev (closed API) decision model | Already covered by `laya-jev-ultrafast`, `jev-vs-llm`; nothing new |

Chat attachments: Prosp "100 Claude lead generation skills" folder graphic -> `lead-gen-skill-map-10x10`, `/lead-gen-map`; Thomas Pearce "Personal Brand Strategy" -> `personal-brand-strategy-map`, `/brand-map`, template `mind-map-tree-brand-blue`; "The Complete Claude SEO Team" -> `claude-seo-team-8-areas`, `/seo-team`, agent `seo-team-orchestrator`, template `hub-spoke-agent-team-radial`.

## 2. What was created

| Kind | Items |
|---|---|
| Skills (8) | `skillspector-preinstall-scan`, `claude-code-addons-top5`, `ai-automations-50-marketing`, `personal-brand-strategy-map`, `claude-seo-team-8-areas`, `lead-gen-skill-map-10x10`, `oss-trending-picks-oct-2026`, `vibe-coding-plugin-layers-5` |
| Commands (7) | `/skill-scan`, `/automation-pick`, `/brand-map`, `/seo-team`, `/addon-pick`, `/oss-pick-oct`, `/lead-gen-map` |
| Agents (2) | `seo-team-orchestrator`, `campaign-planner-multi-agent` (the "Multi-Agent Campaign Planner" from the Advanced AI Agents slide) |
| Design (4 templates + 1 theme) | `social-card-vault-repo-mono`, `automation-list-yellow-marker`, `mind-map-tree-brand-blue`, `hub-spoke-agent-team-radial`, theme `theme-github-vault-mono-starfield`. Font stack starts with Aptos |
| User-run script | `scripts/batch110-install.sh` (asks before every step; no piped installs) |

## 3. What was verified, and what was not

- READMEs and LICENSE files for 22 repos were fetched and read on 12 October 2026. Licences in the skills come from those files.
- SkillSpector (static, `--no-llm`) was installed in an isolated virtual environment and run on the 8 new skills. Five scored 0 to 7; three scored 29 to 30 ("CAUTION"); every flagged line was documentation that quotes an install command; no executable scripts. Findings were not suppressed.
- Star counts, "stars today" and the NVIDIA 31,132-skill figures were not re-checked.

## 4. Source problems

- The aigenesis list has 49 distinct items (one repeat), and three descriptions do not match their titles.
- The SEO graphic names eight areas, not twenty agents; the lead-gen graphic shows folder names only. Their contents are behind "comment" gates and were not obtained.
- The SkillUI slide has no repo path; the real repo is `amaancoderx/npxskillui`. CryptPad's real upstream is `xwiki-labs/cryptpad`.
- Open WebUI is not plain open source (branding clause above 50 users). free-claude-code installs by piped script and proxies every prompt. Spotube and MeTube touch YouTube terms. GeminiWatermarkTool removes only the visible mark.
- The karpathy-skills repo has no licence file at its root.

## 5. Not done

Nothing from the carousels was installed on any machine; no plugin was added; no connector was changed. Connectors the carousel stack names (Gmail, Drive, Sheets, Airtable, Slack, Notion, Calendar) are already connected in this workspace; WhatsApp and n8n are not. Meta Ads, Google Ads and Search Console are not connected and would need your authorisation. The Agent Archive account setup is waiting for your answer.
