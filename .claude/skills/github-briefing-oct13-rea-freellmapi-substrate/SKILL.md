---
name: github-briefing-oct13-rea-freellmapi-substrate
description: The second @githubnow briefing of 13 October 2026 ("The free AI tools devs are quietly starring this week": morluto/rea reverse-engineering MCP, tashfeenahmed/freellmapi LLM routing gateway, agent-substrate/substrate agent sandbox runtime) with licences read from each repo, what each does to your data and agent configuration, the legal limits on reverse engineering, the free-tier terms risk of routing many providers, the scan results and their limits, and a clear install rule. Use when the user asks about any of these three repos or about an MCP server for binary analysis, a free-tier LLM proxy, or running agent sandboxes on Kubernetes.
---

# Three more repos from the 13 October 2026 briefings

Source: @githubnow, 5 images (cover, three repo slides numbered 1/3 to 3/3, and a closing slide). Read 14 October 2026. The star pills (+2,963 today, +8,012 this month, +498 today) were not re-checked: the GitHub API is out of reach in this session. The first briefing of the same day (open-code-review, xtool, vercel-labs/skills) is in `github-briefing-oct13-three`.

**Closing slide:** "Start with rea, the README gets you running in ten minutes" is the author's claim. Native analysis also needs a Hopper, Ghidra or IDA install, which the README says you provide.

| Repo | What it is | Licence (read from the repo) | Status and cost |
|---|---|---|---|
| `morluto/rea` | One MCP server and skill that lets an agent inspect native binaries, Electron and JavaScript apps, .NET assemblies and websites; native analysis uses your own Hopper, Ghidra or IDA | MIT (REA code); third-party material keeps its own licences; you must be licensed to use the commercial tools | npm package `rea-agents`; setup edits your agent's configuration |
| `tashfeenahmed/freellmapi` | OpenAI-compatible `/v1` gateway that routes across 34 free LLM providers and 635 free endpoints, with failover and encrypted key storage | MIT | Free tier gets the model catalog as a monthly snapshot; a Premium live catalog is $19/yr (README) |
| `agent-substrate/substrate` | Kubernetes runtime that maps many agent "actors" onto a pool of ready worker pods, with suspend and resume | Apache-2.0 | README says pre-1.0: no backward-compatibility guarantees |

## REA: what to know before you let it touch your agent

- **Setup changes your agent.** `npx rea-agents setup` adds REA's MCP server and workflow instructions to your agent's configuration, with backups, after you approve. It can optionally install Hopper. It is an MCP connector, so it is a connector installation: do it on your own machine, not in a cloud session.
- **The skill tells the agent to run an unpinned package.** Its instructions run the npm package through `npx` with no version pinned, five times (and with the newest-version tag for diagnostics), which downloads and executes whatever is current on npm. Pin a version after you have reviewed it.
- **A piped installer exists.** The repo ships `install.sh`, designed to be fetched and piped straight into a shell. Use the npm route, or download the script and read it first. I did not read the script in full and a grep did not show checksum verification.
- **The README example is a legal question.** Its sample prompt is: "Understand how search works in the Notes app, show me the evidence, and build a similar feature for my project." The project's own disclaimer says it is for lawful analysis of software you own or are authorized to examine, and says it will not help with copying proprietary software or reproducing its protected code, or with bypassing licence checks. Reverse engineering a competitor's product can breach its licence terms and, depending on jurisdiction, copyright or anti-circumvention law. Do not use it on someone else's product without legal advice.
- **Typosquat warning from the README:** get it only from `morluto/rea`, `rea.tools` or the `rea-agents` npm package.

## FreeLLMAPI: what it does to your data and your terms

- **Your prompts go to up to 34 third parties.** Each request is routed to whichever free provider has capacity. Do not send customer data, secrets or personal data through it.
- **The README says free tiers fall short:** no frontier models, variable latency, no SLA, and quality dips late in the day as daily caps are hit.
- **Terms of service.** The README links a provider-by-provider review (May 2026) of how each provider views a personal, single-user proxy. Read it. Its compose file binds the service to `127.0.0.1` and says it is single-user and must not be exposed to the internet. Offering it to a team or customers is a different use.
- **It can update itself.** The README says the router updates its model catalog from a signed feed, and the compose file wires an optional automatic-update path through a Watchtower container that tracks the image's newest tag. Anything that pulls the newest tag automatically can change under you. Leave auto-update off unless you accept that.
- **Cost:** free providers are rate-limited per key; the Premium catalog is $19 a year per the README.

## Agent Substrate: who it is for

- It is infrastructure for teams that already run Kubernetes and need many sandboxed agents. The slide's "resume in under 500 ms" and "500+ suspend/resume operations per second" come from the project's own description and were not measured here.
- Pre-1.0: expect API changes.
- Not a thing to install on a laptop to try an agent.

## SkillSpector (static, `--no-llm`, 14 October 2026)

| Target scanned | Score | What it means |
|---|---|---|
| REA's own agent skill (`reverse-engineer-anything`, 7 files) | 40/100, MEDIUM, "CAUTION"; 12 findings; 100% coverage | Five findings are the real unpinned-package references. The others are documentation text about analysing macOS application bundles and a read-only disk-image mount |
| REA whole repo (3,755 files) and its `install.sh` plus scripts | **No result: both scans timed out** | Unscanned. Treat as unaudited |
| FreeLLMAPI `scripts/`, `Dockerfile`, compose file | 100/100 CRITICAL, 23 findings | Mostly the bootstrap scripts reading and preserving the local environment file, plus the automatic-update setting above. The automatic-update setting is a real design fact; the `.env` handling is ordinary |
| Substrate `scripts/` | Nothing to scan (0 components) | Not a clean result. The runtime itself was not scanned |

Reading: no repo here was cleared. A scanner built for skills over-scores software repositories (see `github-briefing-oct13-three`). The REA skill's genuine issue is the unpinned package. The FreeLLMAPI issue is its automatic-update design.

## Install rule

Nothing from these repos was installed. If you install, do it on your own machine: scan first, pin versions, and for REA review the diff that `setup` proposes before approving it.

Command: `/briefing-oct13-pick <what you need to do>`.
