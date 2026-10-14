---
name: agent-repos-took-off-sep-2026
description: Five GitHub repos from the @buildwithneej "5 that took off this week" carousel (hypit video-cloning workflow, Alibaba open-code-review, colibri 744B model on a laptop, tinycast Mac launcher, Cloudflare security-audit-skill) with real licences, install lines checked against each README, the slide errors found (a misspelled Homebrew tap owner, an outdated colibri release, hypit's modified licence), costs and risks, and which to try. Use when the user asks about any of these repos, wants the install commands, or wants a code-review, security-audit or local-model tool for coding agents.
---

# 5 repos that took off (week of 18 September 2026) - checked

Source: @buildwithneej carousel, 13 slides. READMEs and licences were read on 13 October 2026. Star counts on the slides (9,848 / 36,335 / 36,047 / 6,379 / 12,482) were **not** re-checked: a third-party tracker I searched reported a different tinycast total than the slide.

| # | Repo | Licence (from the repo) | What it does | Install line on the slide | Check |
|---|---|---|---|---|---|
| 1 | `hypit-ai/hypit` | **Modified Apache-2.0** with extra conditions | A coding agent takes a reference video and rebuilds it as an editable, re-runnable workflow | `npx skills add hypit-ai/hypit -g` and `npm install --global @hypit/hypit` | The first line matches the README; Node 22.15+ per its badge. Model calls cost money: the README's own three examples cost $1.07 to $1.15 each |
| 2 | `alibaba/open-code-review` | Apache-2.0 | Code-review CLI: matches review rules to changed files, comments line by line | `npm install -g @alibaba-group/open-code-review`, then `ocr delegate preview` | Matches the README. The README says the rule step is engineering logic, not a model. Its claims of higher precision, about 1/9 of the tokens and **lower recall** are the vendor's, not measured here |
| 3 | `JustVugg/colibri` | Apache-2.0 | Streams a mixture-of-experts model's rarely used parts from disk so a huge model runs on a small machine | `tar xzf colibri-v1.11.0-macos-arm64.tar.gz` then `COLI_MODEL=/path/to/model ./coli chat` | **Outdated**: the README header shows v2.0.0. Speed claim holds: 0.05 to 0.1 tokens/s cold on a 25 GB laptop is one token per 10 to 20 seconds; the 744B reference model is 429 GB on disk |
| 4 | `abue-ammar/tinycast` | AGPL-3.0 | Native macOS launcher, clipboard history, snippets; README says it runs Raycast extensions | Slide: `brew tap abu-ammar/tinycast` | **The slide's spelling is wrong.** The repo and tap owner is `abue-ammar` (with an "e"). README: `brew trust --tap abue-ammar/tinycast`, `brew tap abue-ammar/tinycast`, `brew install --cask tinycast`. Needs macOS 26 or newer |
| 5 | `cloudflare/security-audit-skill` | MIT | A six-phase security audit for a coding agent: recon, hunting, validation, machine-checked findings, report | `npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit` | Matches the README. A full run uses a lot of tokens (the author's own note). "Installs into 75 agents" was not checked |

## What the slides get wrong or leave out

1. **Typo-squatting risk (tinycast).** `abu-ammar` is not the project's owner. A Homebrew tap under a near-identical name could be a different, possibly hostile, project. Use the README's spelling and nothing from the slide.
2. **Hypit is not plain Apache.** Its licence forbids running it as a multi-tenant service, selling or redistributing it for gain, and removing its name, logo or copyright from the CLI and reports. Using it for your own organisation's work, including commercial work, is allowed, and the output belongs to you. "Free tool, paid renders" is accurate.
3. **Colibri's version is stale** and the "eight crafted-file bugs patched in v1.3.0" line was not found in the README; treat it as unverified. The safety point stands: load model files only from sources you trust.
4. **The "Which ones I would use" slide is the author's opinion** (installing open-code-review this week; security audit despite the token cost; hypit as a free tool with paid renders; tinycast free Raycast alternative, switching; colibri needs real hardware).

## What I would do

- **Try first:** `open-code-review` on a small repo (needs a model endpoint and key you configure) and `security-audit-skill` on a throwaway project. Scan both with `skillspector-preinstall-scan` before installing.
- **Only if relevant:** tinycast if you use a Mac on macOS 26+ and Raycast; hypit if you make short-form video and accept the render costs and licence limits.
- **Skip for now:** colibri unless you have the disk and patience: 429 GB and seconds per token is a demonstration, not a workflow.

## Command

`/repo-week-pick <what you need>` returns the one repo that fits, its licence consequence, the README-correct install line, and the first test to run.
