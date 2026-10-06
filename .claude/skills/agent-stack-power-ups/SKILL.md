---
name: agent-stack-power-ups
description: 'Map of the "5 power-ups for AI agents" carousel - a DeepSeek harness (model, memory, tools, sandbox, orchestration), Orca (parallel agents), Herdr (fleet control), Claudex Loop (cross-model review), Looper (issues to PRs) - to the skills already in this repo, plus the agent-stack build order, the new OpenRig team-orchestration card and the Substrate sandbox runtime. Use when the user is assembling a coding-agent setup or asks which tool covers which job. No installs were run.'
---

# Agent stack power-ups

The carousel (@hash42labs) names five items with no URLs or commands. This skill maps them to what the repo already has and says what is still unknown.

| Power-up | Job | Local skill | Public repo found |
|---|---|---|---|
| DeepSeek harness | Build the agent stack: model + memory + tools + sandbox + orchestration | build order below | `deepseek-ai/deepseek-harness` ("dsh", MIT, developer preview) - a match on the name only; the carousel gives no URL, so confirm it is the one meant |
| Orca | Run agents in parallel in isolated worktrees | `orca-cli`, `orca-linear`, `orca-per-workspace-env`, `orca-emulator` | `stablyai/orca` (see `oss-repo-register-106`) |
| Herdr | Control the fleet of agents | `herdr` | `herdrdev/herdr` (Rust terminal multiplexer for coding agents, Apache-2.0) |
| Claudex Loop | Make two models review each other | `claudex-loop`, `claudex-route` | No repo of that name found; unverified |
| Looper | Turn issues into pull requests | `looper` | Ambiguous name; nearest search hit `quangdang46/looper_rust`, not fetched - unverified |

## Agent-stack build order (from the DeepSeek-harness slide, my wording)
1. **Model** - pick one; keep the choice swappable behind one interface.
2. **Memory** - what persists between runs (files first, a database only when needed).
3. **Tools** - the smallest set of actions the job needs; read-only first.
4. **Sandbox** - where code runs; no production credentials inside.
5. **Orchestration** - who hands work to whom; one human approval point before anything outward-facing.
Test each layer alone before adding the next.

## Related cards in this batch
- `mvschwarz/openrig` - YAML-defined agent teams across Claude Code, Codex and Pi with shared context (card: +114 stars that day). Candidate for a study clone only.
- `agent-substrate/substrate` - Kubernetes runtime that multiplexes stateful agents (claims: 10x density, sub-500 ms resume, gVisor/microVM isolation). Infrastructure for operators, not for this repo.
- Cost note: parallel fleets multiply token spend. Set a per-run cap before launching more than two.

## Rules for this repo
Agents here stay draft-only (`data/agent-drafts/`, tools Read/Grep/Glob/Write). Fleet tools that open PRs or push code are outside that rule; use them only in a separate sandbox repo with the owner's approval.

## Keywords
agent harness, parallel agents, worktrees, fleet, orchestration, DeepSeek, Orca, Herdr, OpenRig
