---
name: token-saver-repos-top5
description: The @awayfromlovable "Top 5 Claude Code repos that cut the tokens it burns" - pxpipe (context as images), Caveman (terse answers), Context Mode (raw tool output kept in a sandbox), RTK (shrinks terminal output) and CodeBurn (shows where tokens go) - with the slide star counts and claimed savings, the install commands as shown, a security and accuracy note for each, and a measure-first protocol before adopting any of them. Use when someone wants to reduce Claude Code token or usage-limit burn, or asks whether one of these tools is safe or worth it.
---

# Token-saver repos (top 5)

All numbers are the slides' own and unverified here. Nothing below was installed in the cloud session.

| # | Tool | Slide claim | Install as shown | What to check first |
|---|---|---|---|---|
| 1 | **pxpipe** (7,505 stars) | sends context to Claude as images: ~48k chars (~25k tokens as text) becomes ~2.7k as one image; recent messages stay text | `npx pxpipe-proxy` then `ANTHROPIC_BASE_URL=http://127.0.0.1:47821 claude` | It is a local proxy between Claude Code and the API: it sees every prompt, file and credential. Image-encoded context may lose exact strings (paths, numbers, code). Read the source, pin a version, run on a throwaway repo |
| 2 | **Caveman** (110,982 stars) | "why does my component re-render?" 63 tokens vs 20, same fix (`useMemo`); `/ultracave` 14 | `/plugin marketplace add JuliusBrussee/caveman` then `/plugin install caveman@caveman` | Affects output tokens only. Skill `caveman` already exists here. Do not use it for text you will send to people |
| 3 | **Context Mode** (26,560 stars) | 315 KB of tool output becomes 5.4 KB; raw data stays in a sandbox; a stats command shows savings | `/plugin marketplace add mksglu/context-mode` then `/plugin install context-mode@context-mode` | A hook that rewrites tool results: confirm it never hides an error line you needed. Third-party marketplace, so read before adding |
| 4 | **RTK** (82,937 stars) | `git status` becomes `rtk git status`, up to 90% less output | `brew install rtk` then `rtk init -g` | Bash output only, not Read or Grep; "90% of terminal output, not 90% off your bill" (slide fine print) |
| 5 | **CodeBurn** (11,379 stars) | `codeburn optimize` finds a file re-read every turn, an unused MCP server, a CLAUDE.md riding along each time | `npx codeburn` (no account) | Reads session files on your machine: check what it uploads (should be nothing) |

## Order of operations (my recommendation)
1. **Measure before compressing.** Run CodeBurn (or `/context` and `/usage` in Claude Code) first. Most waste is structural: an oversized CLAUDE.md, MCP servers you never call, whole-file re-reads.
2. Cheap fixes with no new software: trim CLAUDE.md, disable unused MCP servers, `/clear` between tasks, use subagents for noisy searches, shorter outputs by instruction.
3. Then at most one compressor on a throwaway repo, and compare on a task where you already know the right answer.
4. Prefer tools that do not sit in the network path (RTK, Caveman, CodeBurn) over proxies (pxpipe).

## Claim check protocol
For any tool: what does it change in my prompts or tool results; what does it send to third parties; can compression drop a needed detail; does it break prompt caching; one test on a known-answer session; verdict adopt, trial or skip. Command: `/token-saver-check`.

## Caveats
Star counts are the slide's; 110k stars for Caveman is unusually high, so verify the repo owner before installing. Related: `caveman`, `token-budget-advisor`, `claude-token-rules-22`, `claude-code-tooling`.
