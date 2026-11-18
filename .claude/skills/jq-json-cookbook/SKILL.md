---
name: jq-json-cookbook
description: Tested jq recipes for slicing, filtering, mapping, grouping, summing and exporting JSON on the command line (select, map, group_by, sort_by, unique, add, @csv, the // default operator, -e exit codes), each run against sample data with jq 1.7. Use when writing or debugging a jq filter, converting JSON to CSV, summarising an API response, or checking a JSON field in a script.
---

# jq cookbook (tested on jq 1.7)

jq is the command-line JSON processor from the `jqlang/jq` repository (MIT). Check `jq --version` first. Every recipe below was run on this sample file and gave the output shown.

Sample `orders.json`:
```json
{"orders":[{"id":1,"customer":"Ann","total":120.5,"status":"paid","tags":["b2b","eu"]},{"id":2,"customer":"Bo","total":40,"status":"refunded","tags":[]},{"id":3,"customer":"Ann","total":80,"status":"paid","tags":["b2b"]}]}
```

| Task | Command | Result |
|---|---|---|
| List a field | `jq '.orders[].customer' orders.json` | "Ann" "Bo" "Ann" |
| Count matches | `jq '[.orders[] \| select(.status=="paid")] \| length' orders.json` | 2 |
| Sum a field | `jq '[.orders[] \| select(.status=="paid") \| .total] \| add' orders.json` | 200.5 |
| Pick fields | `jq -c '.orders \| map({id, customer, total})' orders.json` | `[{"id":1,"customer":"Ann","total":120.5},...]` |
| Group and total | `jq -c '.orders \| group_by(.customer) \| map({customer: .[0].customer, total: (map(.total)\|add)})' orders.json` | `[{"customer":"Ann","total":200.5},{"customer":"Bo","total":40}]` |
| CSV rows | `jq -r '.orders[] \| [.id,.customer,.total] \| @csv' orders.json` | `1,"Ann",120.5` ... |
| Largest first | `jq '.orders \| sort_by(-.total) \| .[0].id' orders.json` | 1 |
| Distinct values | `jq -c '[.orders[].tags[]] \| unique' orders.json` | `["b2b","eu"]` |
| Array contains | `jq '.orders[] \| select(.tags \| index("eu")) \| .id' orders.json` | 1 |
| Default value | `jq '.orders[0].missing // "n/a"' orders.json` | "n/a" |
| Threshold ids | `jq -c '.orders \| map(select(.total > 50)) \| map(.id)' orders.json` | `[1,3]` |
| Check in a script | `jq -e '.orders \| length > 0' orders.json; echo $?` | true, exit 0 (exit 1 when false or null) |

## Rules that prevent most mistakes
- Quote the filter in single quotes so the shell does not touch `|`, `$` or `"`.
- `-r` removes quotes from strings; `-c` prints one line; `-e` sets the exit code from the last output.
- `.[]` iterates; wrap in `[ ... ]` when you need an array back.
- Use `//` to give a default for missing or null fields.
- Never paste untrusted JSON into a filter you build by string concatenation; pass values with `--arg name value` and use `$name`.
- Use `/jq-filter [what you want]` to have a filter written and tested on your sample.
