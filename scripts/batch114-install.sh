#!/usr/bin/env bash
# Batch 114 - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: 1 skill, 1 reference, 2 commands, merges into 6 existing skills, 2 design templates, 2 themes, a workflows page and a prompts file; nothing was installed.
# Repo slugs, stars and licences were read from GitHub pages on 22 October 2026 (see .claude/skills/oss-alternatives and self-hosted-docker-stack, "Batch 114").
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Read-only looks (permissive licences) =="
for r in luongnv89/claude-howto anthropics/skills actualbudget/actual; do
  ask "git clone $r into ~/src (read-only look)?" && clone "$r"
done

echo "== 2. Copyleft or unusual licence: read LICENSE before any use beyond personal =="
for r in karakeep-app/karakeep paperless-ngx/paperless-ngx immich-app/immich rustdesk/rustdesk; do
  ask "git clone $r into ~/src (GPL/AGPL; look only)?" && clone "$r"
done
ask "git clone n8n-io/n8n into ~/src (fair-code licence, not OSI open source)?" && clone "n8n-io/n8n"

echo "== 3. Claude Code plugins: commands only, not run =="
echo "   Inside Claude Code, review then run yourself:"
echo "   /plugin marketplace add anthropics/skills"
echo "   /plugin install example-skills@anthropic-agent-skills"
echo "   /plugin install document-skills@anthropic-agent-skills"
echo "   Document skills are source-available, not open source; all skills are demonstrations."

echo "== 4. Services (Docker): not started by this script =="
echo "   Start nothing before you have a backup and restore plan. Suggested first: paperless-ngx. Last: rustdesk and home-assistant (remote access and device control)."
echo "   Keep remote-control tools behind a VPN. Never expose a service to the internet without authentication."

echo "== 5. Not installable from a script =="
echo "   Connectors (Ahrefs, Semrush are connected; Sentry and Stripe need reconnecting) are authorised in claude.ai settings."
echo "   The 20 GTM vendors were not verified; no installs offered."
echo "Done. Restart Claude Code so the new commands appear."
