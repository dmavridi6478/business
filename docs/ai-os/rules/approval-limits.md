# Approval limits

**The numbers live in `limits.json` (same folder), not here.** They used to be a table that an LLM was asked to respect; they are now enforced in code by `scripts/os_gate.py`. A limit set to `null` means OWNER MUST SET: every action that needs it is **BLOCKED** until you set it. Run `python3 scripts/os_gate.py limits` to see what is set.

| Limit (key in limits.json) | Default | Enforced by the gate | What it does |
|---|---|---|---|
| `approval_expiry_hours` | 24 | yes (`os_approvals.py`, `os_gate.py`) | an approval older than this is expired |
| `max_spend_per_approval_eur` | **null** | yes | no spend or extra daily ad spend above this per approval; null blocks all spend |
| `max_budget_step_pct` | 20 | yes | an ad budget change larger than this percent is blocked; split it |
| `max_touches_per_window` / `touch_window_days` | 5 / 14 | yes | touches (messages) to one lead in the window; counted from the gate ledger |
| `prospect_batch_size` | 25 | yes | prospects per batch |
| `invoice_first_reminder_days` / `invoice_escalate_days` | 30 / 60 | yes | no reminder before the first, none at or after the second (owner call only) |
| `quiet_hours_local` | **null** | yes | recipient-local window with no messages, e.g. `{"start":"21:00","end":"08:00"}`; null blocks every message |
| `ad_stop_loss_eur`, `target_cost_per_lead_eur`, `cash_buffer_eur` | null | **no - advisory** | feed `os-ads`, `os-business-analyst`, `os-cashflow`; no action gate can enforce a judgement threshold |

There is **no unapproved path**: every action the gate checks must first be an approved card. "Spend without approval" is therefore always EUR 0 and is not a setting.

## How an action is checked

1. `os-approval` writes a card with one machine-readable ```` ```action ```` JSON block (type and numbers).
2. You approve it in a terminal: `python3 scripts/os_approvals.py approve <id>`. The screen shows the **machine-read action** and a gate preview, so you approve the numbers the gate will check, not just the prose. The approval is a hash of the exact card text: an edit voids it.
3. A sender runs `python3 scripts/os_gate.py commit <id>` and proceeds only on exit 0. The gate re-checks approval and expiry, that the approval was not already used (single use), the consent/opt-out registry, quiet hours in the recipient's timezone, the touch cap, and the numeric limits for that action type. It then records the use in `data/ai-os/gate-ledger.jsonl` (hash-chained, script-only).
4. `os-approval` is **not** the authority: it prepares cards. Whether an action is within limits is decided by code and, finally, by you.

**Limit of this design:** nothing in this repo sends anything yet. The gate protects whatever calls it; connector sends in the main session are still protected only by the confirmation prompt (`os_outbound.py`). When you adopt a sender, make it call `commit` first.

## Approval record

See `agent-permissions.md`. The ledger is `data/ai-os/approvals.md`; only `os_approvals.py` in a real terminal writes it.
