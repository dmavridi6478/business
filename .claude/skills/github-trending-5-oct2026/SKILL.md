---
name: github-trending-5-oct2026
description: Five repos from the @buildwithkenny "Trending on GitHub this week" carousel (morluto/rea, cloudflare/security-audit-skill, stablyai/orca, Graphify-Labs/graphify, anomalyco/opencode) with the licence read from each repo's own file, what the card says it does, and the cautions the card leaves out. Use when evaluating one of these repos, comparing coding-agent runners, or deciding which are safe to clone and try.
---

# GitHub trending, five repos (@buildwithkenny, October 2026)

Cover claim: "+78.6K new stars for the No.1 in one week". Star totals and ages below are what the screenshots show, not checked. Existence and licences were checked on 28 October 2026 (repo exists via `git ls-remote`; licence read from the repo's file).

| # | Repo | Card says | Licence (read) | Caution |
|---|---|---|---|---|
| 01 | `morluto/rea` | Reverse engineer anything with agents, from app behaviour down to native binaries; 379k stars, 5,426 commits | MIT | Dual-use. Reverse engineering software you do not own or have rights to analyse can breach licence terms or law. Use only on your own software, open source, or with permission |
| 02 | `cloudflare/security-audit-skill` | Coding-agent skill for multi-phase security audits with independently verified, machine-readable findings; 44.9k stars, 14 commits | MIT (Cloudflare, Inc.) | 14 commits against 44.9k stars is an unusual ratio; read the code before trusting findings, and run audits only on code you may test |
| 03 | `stablyai/orca` | Place to work with a fleet of coding agents (Claude Code, Grok Bot and others) using your own subscriptions; desktop, mobile, remote; 105k stars | MIT (Lovecast Inc.) | Runs agents with your credentials and subscriptions; check permissions and spend limits first |
| 04 | `Graphify-Labs/graphify` | Turns a codebase, docs, SQL schemas, configs and PDFs into a queryable knowledge graph; a /graphify skill for Claude Code, Cursor, Codex and Gemini CLI; local AST parsing, no vector store; 135k stars | Apache-2.0 | Indexing PDFs and configs can pull secrets into the graph; exclude them. Also listed in `claude-code-tooling` |
| 05 | `anomalyco/opencode` | The open source coding agent in your terminal; 221k stars | MIT | Already referenced in `claude-code-tooling`; a terminal agent that edits files and runs commands, so use a clean git state |

## Reading it critically
- The star figures are very large (up to 379k) and were not checked; treat them as unverified until you open the repo yourself.
- Ranking is "stars gained in 7 days", which rewards novelty, not quality or safety.
- For orca and opencode, compare with `autonomous-agent-harness` and `agent-harness-construction` before adding another runner.
- Vet any of them with `/repo-vet owner/repo`.
