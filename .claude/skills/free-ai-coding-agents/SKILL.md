---
name: free-ai-coding-agents
description: Five free open-source coding agents (Cline, opencode, OpenHands, Aider, Continue) with licences, verified install commands and caveats, checked against cloned READMEs on 7 Oct 2026.
---

# Free AI coding agents (@will.ai.m "Cursor, Copilot and Devin for free")
Verified by shallow clone, 7 Oct 2026. Stars are the card's figures, not re-measured.

| Tool | Replaces | Licence | Install (from its README) | Caveat |
|---|---|---|---|---|
| cline/cline (67k) | Copilot | Apache-2.0 | `npm i -g cline` (CLI) or VS Code extension saoudrizwan.claude-dev | model API key is paid separately |
| anomalyco/opencode (203k) | Cursor | MIT | `npm i -g opencode-ai@latest` or `brew install anomalyco/tap/opencode` | same project as sst/opencode (identical HEAD commit) |
| OpenHands/OpenHands (86k) | Devin | MIT | `npm install -g @openhands/agent-canvas` then `agent-canvas` (Docker sandbox option exists) | no-sandbox mode gives the agent full filesystem access |
| Aider-AI/aider (49k) | pair programmer | Apache-2.0 | `python -m pip install aider-install` then `aider-install` | latest commit 22 May 2026 - slower cadence |
| continuedev/continue (36k) | Tabnine | Apache-2.0 | VS Code/OpenVSX extension or `@continuedev/cli` | README says "Final 2.0.0 Release": no further development |

"Free" means the software; model tokens still cost money unless you run a local model. Prefer a sandbox for any agent that executes commands. The card's DIY prompt ("check these repos are legit, then install them") is safe only after the checks above.
