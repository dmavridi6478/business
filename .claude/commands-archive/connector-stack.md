---
description: Show which connectors from the life or content stack are connected in this session, the safe rollout order and the next one to connect
argument-hint: <life|content|vet <name>>
---

Use the `connector-starter-stacks` skill. Argument: "$ARGUMENTS"

1. `life` or `content`: print the stack table for it, then call ListConnectors and mark each connector connected / not installed / not connected / not in registry (SearchMcpRegistry for missing ones).
2. Recommend exactly ONE next connector to connect, with the first read-only test prompt to run.
3. `vet <name>`: run the plugin/connector vetting checklist for that name; check the registry or the marketplace file before claiming it exists.
4. Never connect anything or enable write actions; report what the user must do in claude.ai or with /plugin.
