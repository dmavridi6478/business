#!/usr/bin/env bash
# Batch 111 - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: 20 skills, 24 commands, 10 agents, 8 design templates and 5 themes were added to the repo; nothing was installed.
# Repo slugs, stars and licences were read from each repo's GitHub page on 19 October 2026 (see .claude/skills/oss-swap-part-18/SKILL.md).
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Low-ops candidates (a CLI, a library or a static site; no new server to run) =="
for r in google/osv-scanner projectdiscovery/nuclei better-auth/better-auth withastro/starlight; do
  ask "git clone $r into ~/src (read-only look)?" && clone "$r"
done

echo "== 2. Read first, not recommended for a solo business: you would run and patch a server =="
for r in prometheus/prometheus concourse/concourse backstage/backstage pinpoint-apm/pinpoint logto-io/logto; do
  ask "git clone $r into ~/src (read-only look)?" && clone "$r"
done

echo "== 3. Licence check needed before any use (GitHub reports 'Other') =="
for r in keephq/keep BerriAI/litellm; do
  ask "git clone $r into ~/src, then read its LICENSE file?" && clone "$r"
done

echo "== 4. Coding agent CLI =="
echo "   openai/codex is Apache-2.0 and its README has the install steps. Model usage is billed by the provider."
ask "git clone openai/codex into ~/src (read-only look)?" && clone "openai/codex"

echo "== 5. Not automated =="
echo "   Nuclei: scan only systems you own or are authorised to test."
echo "   OSV-Scanner: run it on a project folder you own; it reports known vulnerabilities only."
echo "   Connectors cannot be installed from a script. Authorise Apollo.io, n8n, Intercom, Profound, Similarweb and Otter.ai yourself"
echo "   in claude.ai connector settings if you want them (see the Batch 111 intake report)."
echo "Done. Restart Claude Code so the new commands and agents appear."
