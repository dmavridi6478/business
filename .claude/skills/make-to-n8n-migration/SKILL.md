---
name: make-to-n8n-migration
description: Migrate a Make (Integromat) scenario to an importable n8n workflow with Claude in four steps (export blueprint, give it to Claude, get the module-to-node mapping first, import, reconnect credentials, test). Use when asked to move, convert or rebuild Make scenarios in n8n.
---

# Make to n8n migration (4 steps)

Source: a four-card carousel by Automated Digital (Batch 117): "Stop rebuilding Make scenarios by hand in n8n. Let Claude do the migration." The method is the card's; the cautions below are added here.

## The four steps

| Step | Do | Detail from the card |
|---|---|---|
| 1. Export the blueprint from Make | Open the scenario, click the three-dot menu, choose **Export blueprint** | You get a `.json` file |
| 2. Give the file to Claude | Attach the `.json` to a Claude chat | Say the target is n8n and that every Make module should become a native n8n node where one exists |
| 3. Ask for the mapping first | Have Claude list each Make module next to its n8n node and flag anything with no match | Check this table before Claude writes any JSON |
| 4. Import, reconnect, test | In n8n: Workflow menu, **Import from File**; re-add credentials; run a test | The prompt below |

## Exact prompt (from the card)

```
Convert this Make blueprint to n8n. First map each module to an n8n node and flag gaps. Then output importable workflow JSON.
```

## Rules added here

1. **Mapping first, JSON second.** Do not accept workflow JSON until the mapping table is approved. A wrong mapping is cheap to fix in a table and expensive to find inside 400 lines of JSON.
2. **Gaps are the real work.** Modules with no native n8n node (custom apps, some aggregators and routers, Make-specific functions) need an HTTP Request node, a Code node or a redesign. List them with a proposed replacement and an effort guess.
3. **Credentials do not travel.** Make blueprints and n8n exports carry no secrets. Re-create every credential in n8n; never paste keys into the chat.
4. **Webhook URLs change.** Every webhook trigger gets a new n8n URL; update the senders before cutover.
5. **Expression syntax differs.** Make mappings such as `{{1.field}}` become n8n expressions (`{{ $json.field }}`); check data types, dates and array handling after import.
6. **Test with pinned sample data, then run in parallel.** Keep the Make scenario active (or in a test mode) while the n8n version runs on sample inputs; compare outputs; only then disable Make.
7. **Operations and cost.** Count Make operations per month before and compare with the n8n hosting or execution plan; the card says nothing on cost, so do not claim savings without that comparison.

## Output format when invoked

1. Mapping table: Make module | n8n node | match quality (exact, close, none) | notes.
2. Gap list with proposed workaround per gap.
3. Credential checklist (service, n8n credential type, scope needed).
4. Test plan (sample payload, expected output, pass criterion).
5. Only after approval: the workflow JSON, with a reminder to import, reconnect, test.

## Related

`n8n-claude-workflow` command, `n8n-workflow-patterns`, `n8n-validation-expert`, `n8n-mcp-tools-expert`, `using-n8n-mcp-skills`. The n8n connector must be authorised by the user in claude.ai before Claude can create workflows directly; otherwise use file import as above.
