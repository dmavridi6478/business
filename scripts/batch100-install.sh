#!/usr/bin/env bash
# Batch 100 - optional installs for the scanner tools. RUN ON YOUR OWN MACHINE from the repo root. Every step asks first.
# gitleaks and osv-scanner were already installed and run in the cloud session (see .claude/skills/agent-output-scanners).
# Nothing below was run by Claude except those two.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }

echo "== 1. gitleaks (MIT) - secrets in code and history =="
echo "   NOTE: the github.com/gitleaks/... module path fails; the module still declares zricethezav."
ask "go install github.com/zricethezav/gitleaks/v8@latest?" && go install github.com/zricethezav/gitleaks/v8@latest
echo "   Pre-commit hook:  gitleaks protect --staged --redact   (wire into .git/hooks/pre-commit yourself after reading it)"

echo "== 2. osv-scanner (Apache-2.0) - vulnerable dependencies =="
ask "go install github.com/google/osv-scanner/v2/cmd/osv-scanner@latest?" && go install github.com/google/osv-scanner/v2/cmd/osv-scanner@latest

echo "== 3. semgrep (LGPL-2.1) - static analysis =="
ask "python3 -m pip install semgrep?" && python3 -m pip install -U semgrep
echo "   Run with --metrics=off if you do not want telemetry."

echo "== 4. garak (Apache-2.0) - LLM vulnerability probes =="
ask "python3 -m pip install -U garak?" && python3 -m pip install -U garak
echo "   Probes cost API tokens against the model you point it at."

echo "== 5. trufflehog (AGPL-3.0) - NOT automated =="
echo "   brew install trufflehog  or the Docker image. It VERIFIES found credentials by logging in with them: use it only on repos you own."

echo "== 6. snyk agent-scan (Apache-2.0) - NOT automated =="
echo "   Needs a Snyk account: export SNYK_TOKEN=...  then  uvx snyk-agent-scan@<version> ~/.claude/skills"
echo "   It asks before contacting each MCP server it finds; say no to any you do not recognise."

echo "== 7. sops (MPL-2.0) - encrypted secrets in git - NOT automated =="
echo "   Download a release binary from https://github.com/getsops/sops/releases and choose a key backend (age is the simplest)."
echo "Done."
