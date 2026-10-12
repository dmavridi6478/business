---
name: replace-so-oss-repos-10-oct
description: A second "10 GitHub repos so good they shouldn't be free" carousel from @replace.so (Oct 2026 edition; the first is replace-so-oss-repos-10) - Twenty (CRM), Llama.cpp, Jean, Rakazo, Windshift/Core (Jira replacement), Emdash, Hoppscotch, Firecamp, plus two repos not in the upload - with slide star counts, what each does, which are agent workspaces, and install-safety notes. Use when scouting open-source replacements for CRM, Jira, Postman-style API tools or local LLM running, or comparing agent-orchestration desktop apps (Emdash, Jean, Rakazo, Codync).
---

| Repo (slide) | What it is | Slide stars | Notes |
|---|---|---|---|
| Twenty (twentyhq/twenty) | open-source CRM for technical teams: customisable objects, views, workflows, agents; extend as code or self-host | 56,690 | already in README; alternative to HubSpot/Salesforce for dev teams |
| Llama.cpp (ggml-org/llama.cpp) | local or cloud LLM and vision inference in C/C++, quantization, CPU-GPU hybrid | 128,085 | skill `quantized-export`. The site shows a pipe-to-shell Windows installer (`irm ... \| iex`): do not run that; use Brew/Winget or build from source |
| Jean (coollabsio/jean) | desktop AI assistant for projects, Git worktrees, terminals, chat sessions across local coding-agent CLIs; open source; macOS tested, Windows/Linux need testers; v0.1.73 | 1,272 | young project |
| Rakazo | open-source platform for persistent AI teammates with memory, routines, voice, tools, isolated computers; Apache-2.0, self-hosted; "an open source Grok Bot alternative" | 2,369 | same genre as Codync (see `github-trending-oct8-repos`) |
| Windshift / "Core" | self-hosted work-management platform that replaces Jira; import a Jira project; AGPL v3; built in Switzerland, GDPR-ready | 163 | tiny; AGPL matters if you host for others |
| Emdash | desktop app that runs coding agents in parallel, each task in a Git worktree, review diffs, merge locally or remotely; built-in browser preview; YC-backed; any agent (Claude Code, Codex, Amp...); site says 1M+ downloads | 5,735 | pairs with `using-git-worktrees` |
| Hoppscotch (hoppscotch/hoppscotch) | open-source API client: requests, responses, tests, collections across devices | 80,300 | alternative to Postman; compare `bruno` in `own-your-apps-joshualevi-7` |
| Firecamp (firecamp-io/firecamp) | open-source API platform for REST, GraphQL, WebSocket, Socket.IO: design, test, document, collaborate | 2,610 | |
Two further icons on the cover are not identifiable from the upload; the CTA is "Comment REPOS and I'll send you this list" (lead magnet).
**Agent-workspace comparison:** Emdash, Jean, Rakazo and Codync all wrap coding agents in worktrees or persistent "teammates". All are young; pick one, read its permissions model, and run it on a throwaway repo first. Anything that gives an agent its own computer or your logged-in browser needs a sandbox.
Rule: read README and LICENSE, prefer official releases, never run a piped installer. Stars are the slides' own.
