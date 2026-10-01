# data/ai-os — runtime folder for the AI Entrepreneur OS

Agents write here. **Everything except this file is gitignored** because it will contain lead, client and financial data.

| Path | Written by | Contents |
|---|---|---|
| `drafts/` | every `os-*` agent | one markdown draft per task, named `YYYY-MM-DD-<agent>.md`; **create-only** (a hook refuses overwrite/edit; collisions get `-2`, `-3`) |
| `morning/` | `os-chief-of-staff` | the one-page Morning Page |
| `approval-queue/` | `os-approval` | one new dated file per run holding approval cards (each with an ```` ```action ```` block); never overwritten |
| `gate-ledger.jsonl` | **`scripts/os_gate.py` only** | hash-chained record of every committed action (single-use approvals, touch counters) |
| `approvals.md` | **`scripts/os_approvals.py` only** (human, real terminal) | hash-chained approval ledger; no agent or session can write it (hook + deny rule) |
| `watchdog/` | `os-watchdog` | nightly audit of logs and gate bypasses |
| `log/` | **the hooks only** | hash-chained activity log (who, which tool, which target; never contents) |

Create the sub-folders on first use (`mkdir -p data/ai-os/{drafts,morning,watchdog,log}`).
