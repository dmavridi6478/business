---
name: github-briefing-oct13-three
description: The @githubnow daily briefing of 13 October 2026 (alibaba/open-code-review, xtool-org/xtool, vercel-labs/skills) with verified licences, install lines taken from each README, what the open-code-review benchmark table actually shows, the SkillSpector result on two of the repos and why it needs reading, and cautions for npx-based skill installs. Use when the user asks about any of these three repos or wants to install agent skills from a git source.
---

# Three repos from the 13 October 2026 briefing

Source: @githubnow, 5 images (cover, three repo slides, closing slide). Read 13 October 2026. The "+264 / +936 / +125 stars today" pills were not re-checked.

| Repo | What it is | Licence (read from the repo) | Install line from its README |
|---|---|---|---|
| `alibaba/open-code-review` | CLI that reads Git diffs, sends changed files to an OpenAI- or Anthropic-compatible model through a tool-using agent, and posts line-level comments | Apache-2.0 | `npm install -g @alibaba-group/open-code-review`, then `ocr delegate preview` (verified in Batch 108) |
| `xtool-org/xtool` | Builds a SwiftPM package into an iOS app, signs it, installs it on a device, from Linux, WSL or macOS; the XKit library exposes the same operations to your Swift code | MIT (LICENSE.md, Kabir Oberai) | Follow its installation pages (Linux/Windows or macOS), then `xtool setup`, `xtool new`, `xtool dev`. Not a one-line install |
| `vercel-labs/skills` | Installs agent skills from a GitHub shorthand, URL, GitLab, Azure Repos, any git remote or a local path, into the folders of 79 agents | MIT (Vercel, Inc., 2026) | `npx skills add <source>`; list first with `--list`; generate a one-skill prompt without installing with `npx skills use <source> --skill <name>` |

## What the open-code-review table shows

The slide shows the repo's own benchmark (small print, read approximately). The best row is a Claude Opus model run through Open Code Review at about 25% F1, about 34% precision and about 20% recall, in about 1 minute 23 seconds using about 385K tokens. The same table lists Claude Code configurations lower, at about 12% to 14% F1 with several times the tokens (about 2,062K for the best of them).

Read that plainly: even the best configuration finds about one in five of the benchmark's seeded issues, and about two in three of its comments are not matches. It is a second pair of eyes, not a gate. The comparison is the vendor's own; it was not reproduced here.

## vercel-labs/skills: what to know

- "79 agent targets" matches the README: four named agents plus "75 more".
- Private repos reuse your existing Git credentials; `GITHUB_TOKEN` or `GH_TOKEN` is optional (README).
- Symlink is the default (one copy, every agent sees updates); `--copy` makes independent copies.
- `npx` downloads and runs the latest published package each time. Pin a version once you rely on it.
- `--all` installs every skill to every agent without prompts. Do not use it on a source you have not read.
- A skill is instructions an agent will follow. Every source you add is code review work: apply `skillspector-preinstall-scan` first. The `use` command writes to a temporary folder and prints a prompt, which still feeds untrusted text to your agent.
- Already listed in `claude-code-tooling` and `docs/batch-98-action-plan.md`; not new, only re-verified.

## xtool: what to know

- Needs an Apple Developer Services login (`xtool auth`). That puts Apple credentials into a third-party tool: use an account you can afford to rotate, and read the project's auth documentation first.
- The repo's own Dockerfile, Makefile and build scripts exist for building the tool itself; they are not part of what you run to use it.

## SkillSpector result (static, `--no-llm`, whole repo, 13 October 2026)

| Repo | Score | Findings | Coverage |
|---|---|---|---|
| `vercel-labs/skills` | 100/100, CRITICAL, "DO NOT INSTALL" | 326 (8 high privilege-escalation, 5 high prompt-injection, 4 high rogue-agent, 1 high tool-misuse, the rest medium or low) | 66% of components fully inspected |
| `xtool-org/xtool` | 100/100, CRITICAL, "DO NOT INSTALL" | 163 (high findings mostly tool-misuse in Makefile, Dockerfile and generated Swift) | 98% |

**How to read this.** The scanner is built for skills, not for whole software repositories, and its score saturates on volume. I opened nine locations (six in `skills`, three in `xtool`; eight of them rated high): each was ordinary text or build code, such as a review rubric that tells reviewers to reject fixes that weaken security boundaries, CLI help lines that contain the word "update", a comment about not deleting a user's source folder, subprocess calls in build code, and a credentials file name listed among files to ignore. I did not read the other 480 findings, and I did not open the test files, Makefiles or generated Swift the scanner also flagged. So: the tool's verdict is not supported by what I sampled, and I have not cleared the code either. Treat both as unaudited software. Scan the individual skill folders you actually install, not the CLI repo.

## Rules

- Nothing from these repos was installed on any machine in this session.
- The cover's "Start with open-code-review, the README gets you running in ten minutes" is the author's claim. Try it on a small repository with a model key you control.

Command: `/briefing-oct13-pick <what you need>`.
