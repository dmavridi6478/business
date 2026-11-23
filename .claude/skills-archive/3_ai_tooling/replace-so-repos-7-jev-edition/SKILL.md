---
name: replace-so-repos-7-jev-edition
description: The "7 GitHub repos so good they shouldn't be free" carousel from @replace.so (Nhost, Foreman, Aria-Icons, Open-glean, Repolyze, Openjev; the seventh slide was not in the upload) with owners and licences from clones, the Jev link between Foreman and Openjev (a decision model that scores typed yes/no questions) and what to check before using each. Use when considering any of these repos, or when working with Jev-style typed decision servers and agent supervisors.
---

# 7 repos "so good they shouldn't be free" (6 seen)

Source: @replace.so carousel; slide stars shown (Foreman 505, Openjev 306, Open-glean 832) are unverified. Slides give no owners, so owners were found by web search and licences read from clones on 5 October 2026.

| Repo | Slide says | Owner found | Licence | Watch |
|---|---|---|---|---|
| Nhost | Open-source backend: PostgreSQL, GraphQL, auth, storage, serverless functions | nhost/nhost | MIT | Self-hosting the whole stack is real work; the hosted plan is the maintainers' business |
| Foreman | Supervises coding agents with Jev: progress, requirements, tests, verification, human escalation | thruwire/foreman | MIT | Pairs a coding worker (Codex or OpenCode) with an independent scorer; a Python policy turns scores into actions; has a demo mode that needs no key. Needs a Jev or Jev-compatible endpoint for real runs. Python 3.11+. (A different repo, `497974/foreman`, shares the name: not this one) |
| Aria-Icons | Searchable access to 380,000+ SVG icons, CLI and MCP | LeulAria/Aria-Icons | MIT for the tool | Its README says 340,000+ icons; the icons come from many collections with their own licences; its README offers a `curl ... \| bash` install: use `npx` or read the script instead |
| Open-glean | AI workspace for searching memories, files and connected apps with cited answers over Hydra DB | hydra-db/open-glean | Apache-2.0 | Needs a Hydra DB key (hosted) or your own Hydra DB; connectors read your Slack, Notion, GitHub and Gmail data |
| Repolyze | AI repo analysis: quality, security, architecture, dependencies, exportable reports | OssiumOfficial/Repolyze | MIT | Sends repository code to a model: not for private code without a data decision. Another project named `repolyze` exists |
| Openjev | Jev-compatible open decision server (typed yes/no, choice, score) with DiffusionGemma | razorback16/openjev | Apache-2.0 | Needs an NVIDIA GPU (vLLM) or Apple silicon (MLX); also serves other models (Laya, Verdict, CLM, JevK5); a free hosted API exists at its site with its own terms |

## How Foreman and Openjev connect

Jev (a typed decision model) answers narrow questions with a probability and confidence: "is this worker stuck?", "does this need independent verification?". Foreman is a supervisor loop that asks nine such questions about a coding agent and maps the scores to actions (continue, stop, verify, finish, escalate). Openjev is an open server that speaks the same API. Typed output does not mean correct output: measure on your own cases first (see `laya-jev-ultrafast` and `jev-vs-llm`).

Use `/jev-supervisor` to plan a supervised agent run and `/repo-licence-check` for licences.
