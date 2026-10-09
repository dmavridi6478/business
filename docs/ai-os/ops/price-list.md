# Price list (the only source of prices for `os-close` and `os-pricing`)

`os-close` may quote **only** items in the table below, inside their validity dates. A price that is not here is
"NOT ON PRICE LIST - owner must price this". While the table has **no rows**, `os-close` refuses to draft a proposal
(`python3 scripts/os_registry.py prices check` exits 1). Agents cannot edit this file; you do.

| item | description | price_eur | unit | vat | valid_from | valid_to | approved_by | approved_on |
|---|---|---|---|---|---|---|---|---|

<!-- Example row (delete the comment markers to use; rows inside comments are ignored):
| ITEM-001 | Initial assessment, 2 h | 150.00 | per session | 24 % | 2026-10-01 | 2026-12-31 | owner | 2026-10-01 |
-->
