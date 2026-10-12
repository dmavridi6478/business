---
name: skillspector-preinstall-scan
description: Scan any agent skill, plugin, MCP server or repo with NVIDIA SkillSpector BEFORE installing it, then read the report instead of trusting the score. Covers install (uv, never a piped script), the static-only run, the optional LLM pass and what it sends out, how to read the 0-100 risk score, a baseline file for accepted findings, and a gate you can apply to every future install. Use when the user is about to install a skill, plugin, marketplace entry or MCP server from a repo, zip or URL, asks "is this skill safe", or says "scan before install".
---

# Pre-install scan with SkillSpector

Source: a @joshualevi.ai carousel ("Nobody checked the skills you installed in Claude Code"), checked on 12 October 2026 against the repo README and LICENSE of `NVIDIA/SkillSpector` (Apache-2.0).

## What the carousel says, and what I could confirm

| Carousel claim | Finding |
|---|---|
| NVIDIA analysed 31,132 skills; 26.1% vulnerable, 5.2% likely malicious | **Not verifiable from the repo README.** Treat as the author's quote of an NVIDIA study until you read the study. Directionally consistent with the repo's stated purpose |
| 71 patterns across 17 categories, taint tracking, YARA | Plausible; the README describes static rules plus an optional LLM pass. The exact counts were not recounted |
| Live CVE data from OSV.dev, 0 to 100 score | **Matches** the README (SC4 queries OSV.dev, offline fallback; 0 to 100 risk score) |
| One command on a repo, zip, URL or folder | **Matches**: `skillspector scan <path | SKILL.md | URL | .zip>` |
| Part of NVIDIA's Verified Skills pipeline | **Matches** the README |
| "A clean scan is not a guarantee" | True. A scanner finds known patterns. It does not prove safety |

## Install (do this once)

Use a virtual environment or `uv tool`. Do not run any `curl | sh` line from a README without reading it first.

```bash
uv tool install git+https://github.com/NVIDIA/skillspector.git
# optional MCP server mode:
uv tool install 'skillspector[mcp] @ git+https://github.com/NVIDIA/skillspector.git'
```

The README warns that the install pulls third-party open-source packages: review their licences. A Docker route also exists (build from the repo's Dockerfile, then `docker run --rm -v "$PWD:/scan" skillspector scan ./my-skill/ --no-llm`).

## The gate

1. **Fetch, do not install.** Download the skill to its own empty folder. Never open it from a folder that contains your own scripts.
2. **Static pass first**: `skillspector scan ./the-skill/ --no-llm`
3. **Read the findings**, not just the number. Look for: instructions that tell the agent to ignore rules, send files or env vars out, run shell commands, fetch and execute remote code, or edit its own memory or hooks.
4. **Optional LLM pass** (`skillspector scan ./the-skill/` with credentials in a local `.env`). The default backend is DeepSeek per the README, so the skill's text goes to that provider. Do not do this for private or client material without a decision.
5. **Decide**: install only if there are no unexplained high findings. Record the decision (date, version or commit, score) in the repo's install log.
6. **Re-scan on update.** A skill that was clean at v1 can change at v2.
7. **Suppress knowingly.** Accepted findings go in a baseline file (`--baseline .skillspector-baseline.yaml`) with a reason; `--show-suppressed` lists them.

Output formats: `--format json|markdown|sarif --output report.<ext>`.

## What a scan does not cover

- Runtime behaviour after install (network calls built at run time, packages fetched later).
- A malicious but well-worded instruction the model reads as harmless.
- Your own judgement about whether the author is who they say they are.

## Rules for this repo

- Skills in this repo that were written here (original content) are scanned with `--no-llm` before a pull request is opened.
- Vendored third-party skills are scanned and the score is recorded in their entry.
- No result of this scan is ever described as "safe", only as "no findings at this version".
