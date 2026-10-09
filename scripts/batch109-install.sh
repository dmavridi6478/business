#!/usr/bin/env bash
# Batch 109 - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: skills, commands and a design template were added to the repo; nothing was installed.
# Facts come from each repo's README and LICENSE, read on 5 October 2026.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Clone for reading (shallow; no install) =="
for r in thruwire/foreman razorback16/openjev hydra-db/open-glean OssiumOfficial/Repolyze nhost/nhost louislam/uptime-kuma paperless-ngx/paperless-ngx; do
  ask "git clone $r into ~/src?" && clone "$r"
done

echo "== 2. Foreman demo mode (MIT; Python 3.11+; no API key needed for the demo) =="
echo "   Its README installs with: python -m pip install foreman-core   (use a virtual environment)"
ask "create ~/foreman-venv and pip install foreman-core?" && { python3 -m venv "$HOME/foreman-venv" && "$HOME/foreman-venv/bin/pip" install foreman-core; echo "   Then follow the demo section of its README. Do not point it at real work until you have tested it."; }

echo "== 3. Read first, not automated =="
echo "   Openjev needs an NVIDIA GPU (vLLM, Docker) or Apple silicon (MLX). A free hosted API exists with its own terms."
echo "   Aria-Icons: its README also offers 'curl | bash'; use 'npx -y aria-icons@latest setup' only after reading it. Icon collections carry their own licences."
echo "   Open-glean needs a Hydra DB key and connects to Slack, Notion, GitHub and Gmail data; HydraDB itself is AGPL-3.0."
echo "   Repolyze sends repository code to a model: not for private code without a decision."
echo "   Linkwarden, Plausible and Vaultwarden are AGPL-3.0; Paperless-ngx is GPL-3.0; Uptime Kuma is MIT."
echo "   Vaultwarden is an unofficial Bitwarden-compatible server: you become responsible for securing and backing up your passwords."
echo "   Uptime Kuma (README): docker run -d --restart=always -p 3001:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:2"
echo "Done. Restart Claude Code so the new commands appear."
