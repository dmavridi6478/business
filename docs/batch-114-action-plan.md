# Batch 110 (files numbered 114) - action plan

Input: `81b48838-iCloud_Photos.zip` with 11 JPEGs and one MP4. Ten images are the @your.aimentor carousel "5 GitHub repos everyone starred this week" (cover, five repo cards, five detail slides). One image is a different layout of the same series. The video is @cyberwithjohann "5 GitHub Repositories to Find Security Problems in Code" (Gitleaks, TruffleHog, Trivy, Semgrep, Prowler).

## 1. Created (committed)
| Source | Skill | Command / agent |
|---|---|---|
| 5 repo carousel | five-repos-agent-tools-nov2026 | /repo-vet (existing) |
| Claude Code Game Studios (card 01) | game-studio-chain-of-command | /studio-plan, agent `game-studio-planner` |
| 5 scanner video | security-scanners-five | /scanner-pick |
Design: `repo-get-it-cream`, `scan-result-terminal-card`, `theme-scan-night-ember`. User-run `scripts/batch114-install.sh` (syntax checked, not run).

## 2. Executed
- Confirmed with `git ls-remote` that all 10 repos exist and read each default branch.
- Read the licence file of all 10 from `raw.githubusercontent.com`: MIT (Gitleaks, Game Studios), Apache-2.0 (Trivy, Prowler, agent-desktop), BSD-3-Clause (Scrapling), MIT OR Apache-2.0 (Craft Anything, per its README), GPL-3.0-or-later with Apache components (Zed), LGPL-2.1 (Semgrep), AGPL-3.0 (TruffleHog).
- Read the README install lines, the MCP instructions (Scrapling and agent-desktop) and the claims on the cards. Read Zed's own Linux docs and pricing page.
- Looked up the March 2026 Trivy supply-chain compromise in public reports (Aqua, Snyk, Wiz) and wrote the caution into the skill.
- Rendered both templates at 1280 (light, dark) and 390 px: no overflow; one real bug (an invalid multi-layer background) was found by looking at the render and fixed.

## 3. Workflows
None created: nothing in the files describes a workflow to build. (The n8n connector also needs a new sign-in in this session.)

## 4. Connectors
- Registry search for Scrapling, Semgrep, Prowler, Trivy, Gitleaks, desktop automation and game development: no matching connector. TinyFish (hosted browser and scraping) is already connected and covers part of what Scrapling does.
- Scrapling and agent-desktop each ship a local MCP server. Neither is installed in the cloud container and each grants real capability, so `.mcp.json` is unchanged. To add them on your own machine, after installing the tool:
```json
{ "mcpServers": {
  "agent-desktop": { "command": "agent-desktop", "args": ["mcp"] },
  "scrapling": { "command": "scrapling-mcp" }
} }
```
  `agent-desktop mcp` is from its README; `scrapling-mcp` needs `pip install "scrapling[ai]"` and `scrapling install` and exists from Scrapling v0.4.13. Semgrep also documents `semgrep mcp`.

## 5. Not done - needs you
| Item | Why | Step |
|---|---|---|
| Clone, install or run any of the ten | The cloud session cannot touch your machine | `scripts/batch114-install.sh`, answer per step |
| Run any scanner | Scan only what you own; two need credentials | `/scanner-pick`, then run the commands yourself |
| Add the two MCP servers | Desktop control and bot-bypass scraping are your call | Snippet above |
| Install Zed | The Linux installer pipes a script into a shell | Use zed.dev/download or a package manager |

## 6. Claims to treat as unverified
- All star, fork and issue counts on the cards (36,085; 17,808; 98,794; 93,535; 18,039): the GitHub API was blocked from the cloud container.
- Game Studios' "ranked last" test and Scrapling's 1.1-second run are the authors' own results; not reproduced. The Game Studios README says four games were built but its table shows two.
- The card's line that Claude Agent and Codex run inside Zed was not checked on Zed's docs.
- The video's scan screens are illustrative output; the command `prowler a...` is cut off, and `prowler aws` is my reading.
- Trivy: reports disagree on tag counts; I did not check the current state of its releases.
