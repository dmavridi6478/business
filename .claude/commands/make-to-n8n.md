---
description: Convert a Make blueprint (.json) to an n8n workflow, mapping modules to nodes first and flagging gaps before any JSON is written
argument-hint: [path to the exported Make blueprint .json, or paste its content]
---

Use the `make-to-n8n-migration` skill.

Input: $ARGUMENTS

1. Read the blueprint. List the trigger, every module in order, routers and filters, and every external service involved.
2. Produce the mapping table (Make module | n8n node | match: exact, close, none | notes). Flag each gap and propose a workaround (HTTP Request node, Code node, redesign).
3. List the credentials the n8n version needs, as a checklist. Do not ask for secrets.
4. Stop and ask me to approve the table. Do not write workflow JSON before I do.
5. After approval, output importable n8n workflow JSON, then the import and test steps: Workflow menu, Import from File, re-add credentials, run with sample data, compare with the Make output, only then switch off the Make scenario.
6. State what could not be verified without running it (expressions, pagination, error paths).
