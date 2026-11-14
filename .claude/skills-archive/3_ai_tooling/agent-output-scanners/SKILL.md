---
name: agent-output-scanners
description: Seven free scanners that check what an AI agent shipped - gitleaks and trufflehog (leaked keys), osv-scanner (vulnerable dependencies), semgrep (code patterns), snyk agent-scan (agents, MCP servers and skills), garak (LLM vulnerabilities) and sops (keep secrets encrypted in git) - with install commands, the order to run them, licence cautions and this repo's reviewed baseline. Use after an agent writes code or installs dependencies, before pushing or deploying, when auditing the skills and MCP servers installed on a machine, or when setting up pre-commit secret checks. Source @joshualevi.ai "7 repos that check what your agent shipped last night" (Batch 100).
---

# Agent output scanners

An agent gets three things wrong fastest: it leaks keys, pulls in unpatched dependencies and writes code nobody read. Run these before you push. Command: `/scan-agent-work`.

| # | Tool | Checks | Licence | Install |
|---|---|---|---|---|
| 1 | `gitleaks/gitleaks` | keys and tokens in files and git history; works as a pre-commit hook | MIT | `go install github.com/zricethezav/gitleaks/v8@latest` (see gotcha) |
| 2 | `trufflesecurity/trufflehog` | leaked credentials, then **logs in with them** to see if they are live | AGPL-3.0 | `brew install trufflehog` or the Docker image |
| 3 | `snyk/agent-scan` | agents, MCP servers and skills on your machine for prompt injection and vulnerabilities | Apache-2.0 | `uvx snyk-agent-scan@<version>`; needs a Snyk account and `SNYK_TOKEN` |
| 4 | `semgrep/semgrep` | static analysis across ~30 languages; your own rules | LGPL-2.1 (rule sets have their own terms) | `python3 -m pip install semgrep` |
| 5 | `google/osv-scanner` | dependencies against the OSV database; guided remediation | Apache-2.0 | `go install github.com/google/osv-scanner/v2/cmd/osv-scanner@latest` |
| 6 | `NVIDIA/garak` | probes the model behind a feature with jailbreaks and prompt injection | Apache-2.0 | `python -m pip install -U garak` |
| 7 | `getsops/sops` | prevention: encrypted YAML/JSON/ENV/INI in git (KMS, age, PGP) | MPL-2.0 | release binary or package manager |

Licences were read from each repo's LICENSE file on 2026-10-02. Stars on the card are a screenshot.

## Order of use

1. **gitleaks** first: cheapest, and a leaked key is the worst outcome. Install it as a pre-commit hook so a leak never reaches a commit.
2. **osv-scanner** on every lockfile the agent touched.
3. **semgrep** with a rule for any pattern an agent repeated.
4. **trufflehog** only on repos you own and only if you accept active verification: it sends the found credential to the provider's API.
5. **agent-scan** when you add skills or MCP servers from outside; the README says it asks before contacting each discovered MCP server in an interactive run.
6. **garak** when you ship a feature on top of a model.
7. **sops** to stop the next leak: commit ciphertext, not plaintext.

## Gotchas

- `go install github.com/gitleaks/gitleaks/v8@latest` **fails**: the module still declares `github.com/zricethezav/gitleaks/v8`. Use that path. (Tested 2026-10-02: v8.30.1.)
- `gitleaks version` prints "version is set by build process" when built with `go install`; that is normal.
- Always pass `--redact` so reports never print the secret. Do not paste a raw report into a chat.
- A finding is not a leak until you look at it with the value masked. Record reviewed false positives in `.gitleaksignore` (fingerprints) with a comment saying who checked and when.
- AGPL tools (trufflehog) have obligations if you modify and offer them as a network service. Running them on your own repos is fine.

## This repo's baseline (2026-10-02)

- **gitleaks, full history (258 commits):** 11 findings, all reviewed with values masked: placeholders in vendored skills and the README, plus upstream Sylius test fixtures that exist only in old history. Recorded in `.gitleaksignore`; a rescan reports no leaks. [Likely]: two `curl -u` lines were judged placeholders from context, not traced upstream.
- **osv-scanner, whole tree:** 191 unique advisories in 11 manifests, all inside vendored skill folders (largest: `cookie-sync` 81, `agent-platform-tuning` 80, `safe-browser` template 45, `webmcp-gen` 33, `mcp-builder` 27). They matter only if someone installs those dependencies. Do not run `npm install` or `pip install -r` in those folders without reviewing and upgrading first. Not fixed here: the files are upstream copies.
- Not run here: trufflehog, semgrep, garak, sops (not installed) and agent-scan (needs your Snyk token).
