---
name: agent-repos-licence-ledger
description: Ownership, licence and overlap ledger for the "7 GitHub repos that could save you months building AI agents" carousel (@aiclawbots) - Browser Use, Agent Memory, Scientific Agent Skills, Diagram Design, Cybersecurity Skills, Awesome Harness Engineering, OpenViking - mapped to the seven building blocks (browser control, memory, research skills, diagrams, security, orchestration, context) with the licence read from each repo and the warnings the carousel omits. Use before adopting any of these into an agent stack, or when asked which block covers what.
---

# Seven agent building blocks: ownership and licences

Source: a seven-slide carousel plus a cover and a "Comment HERMES" slide offering a free Hermes setup guide. The carousel names no owners and gives no licences. This repository already covers the repos in `agent-github-repos-4` and `agent-memory-repos`; this ledger adds what those do not say. Checked 28 October 2026 (repo exists via `git ls-remote`; licence read from the repo's file).

| # | Block (carousel) | Repo | Licence (read) | Already covered in | Warning |
|---|---|---|---|---|---|
| 1 | Browser control ("Browser Use") | `browser-use/browser-use` | MIT | `agent-github-repos-4` | See `browser-use-to-stagehand` before starting a new build |
| 2 | Memory ("Agent Memory") | `rohitg00/agentmemory` | Apache-2.0 | `agent-memory-repos` row 7 | Name match only; the card shows no owner |
| 3 | Research skills (160+) ("Scientific Agent Skills") | `K-Dense-AI/scientific-agent-skills` | MIT | `github-trending-agent-repos-sep2026` | "160+" is the card's count, not checked |
| 4 | Diagrams ("Diagram Design") | `cathrynlavery/diagram-design` | MIT | `agent-github-repos-4` | Name match only |
| 5 | Security ("Anthropic Cybersecurity Skills") | `mukul975/Anthropic-Cybersecurity-Skills` | Apache-2.0 | `agent-github-repos-4` | **Not made by Anthropic.** The owner is an individual account; the name invites that assumption |
| 6 | Orchestration ("Awesome Harness Engineering") | `yenanjing/awesome-harness-engineering` (as resolved earlier) | No licence file found at LICENSE or LICENSE.md | `agent-github-repos-4` | At least three repos share this name (`ai-boost/`, `walkinglabs/`, `yenanjing/`); the card shows no owner, so the match is not certain |
| 7 | Context ("OpenViking") | `volcengine/OpenViking` | **AGPL-3.0** | `agent-memory-repos` row 2 | AGPL: if you run a modified copy as a network service you must offer its source. The carousel and the earlier rows do not mention this |

## The Hermes pitch
The "HERMES" slide says browser control, memory, research skills, diagrams, security, orchestration and context management all have open-source projects to build around, and offers a free setup guide to commenters. That guide is a lead magnet and was not in the archive; nothing here claims to reproduce it. Related installed skills: `hermes-nousresearch`, `hermes-agent-self-evolution`, `hermes-imports`, `oh-my-hermes`.

## Use
- `/agent-stack-plan [agent goal]` chooses which blocks a given agent needs and which licence limits apply.
- `/repo-vet owner/repo` repeats the existence, owner and licence check on any repo.
