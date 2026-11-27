---
name: github-trending-three-nov2
description: Three trending GitHub repositories from a @githubnow carousel (claude-seo, Claude-Code-Game-Studios, NSA Ghidra) with figures read from GitHub on 2 November 2026, how each differs from its card, what each can touch, and trial rules (reverse-engineering tool is dual-use; agent studio kits change settings and run many agents). Use before installing any of the three.
---

# Three repos from the @githubnow carousel (2 November 2026)

Source: a three-slide carousel (Batch 127). Card figures ("this month", "today") are snapshots; repo pages were read on 2 November 2026.

| # | Repo | Card says | Checked on GitHub | Care |
|---|---|---|---|---|
| 1 | `AgriciDaniel/claude-seo` | "+6,891 stars this month"; "Full SEO audit in 10 to 15 minutes"; up to 17 agents in parallel | 22,736 stars, 3,100 forks, MIT, created 7 Feb 2026. README now says 26 sub-skills and 19 sub-agents plus 9 optional extensions for live SEO data (agent readiness, llms.txt, WebMCP, backlinks, local, e-commerce, international, Google APIs, PDF and Excel reports). The homepage is the author's paid community | **Already vendored here** as `claude-seo` (top-level skill only, from an older commit). The vendored copy is behind (24 sub-skills then); the full plugin is not installed. Live-data extensions use paid APIs and need keys. A crawler running 17 agents at once hits a site hard: only audit sites you own or may test, and set a polite crawl rate. "10 to 15 minutes" is the author's figure. |
| 2 | `Donchitos/Claude-Code-Game-Studios` | "+970 stars today"; 49 agents; 74 workflow skills; hooks and rules; one session as a studio hierarchy | Description reads 49 agents and **72** workflow skills (card says 74). Release 1.2.0 on 19 Oct 2026; 43 commits. Stars, licence and contributors not read in the page text I got | A large kit: many agents, slash commands, commit and push gates and path rules. Hooks run on your machine and change how Claude Code behaves in that project. Try it in a throwaway folder, read `.claude/settings` and the hooks first, and check the licence file before reuse. The "you keep every final decision" claim is the card's; verify the gates actually block a commit |
| 3 | `NationalSecurityAgency/ghidra` | "+16,685 stars this month"; disassembler and decompiler in one tool; Windows, macOS, Linux; Java or Python extensions | 18,953 commits; recent commits on 30 Oct 2026. Stars not read in the page text; licence not read (I believe Apache-2.0, **[Likely]**, confirm in the LICENSE file) | **Dual-use.** Legitimate for malware analysis, vulnerability research, interoperability and education. Use it only on software you own or are authorised to analyse, and mind licence terms that forbid reverse engineering and any law on circumvention where you live. Run unknown binaries in an isolated virtual machine, never on your main machine. Built by a government agency; it is open source and widely audited, but read the release notes and verify downloads from the official releases page |

## What the carousel leaves out
- Star deltas are not endorsements: Ghidra gaining 16,685 stars in a month most likely reflects a news cycle, not a change in the tool.
- None of the three slides states a licence; check each LICENSE file.
- Claims of "49 agents" or "17 agents at once" describe configuration, not quality. Run one real task and read the output.

## Trial protocol (short)
Read LICENSE and install steps; list every command and hook; use a throwaway folder or virtual machine; back up first; know the rollback; do not paste secrets. For the full protocol see `trending-repos-week-oct23` and `/trial-repo`.

Related: `claude-seo`, `ai-search-visibility`, `seo-geo-tool-stack`, `binary-analysis-patterns`, `anti-reversing-techniques`, `protocol-reverse-engineering`, `memory-forensics`, `godot-gdscript-patterns`, `unity-ecs-patterns`, `github-briefing-oct4-three`.
