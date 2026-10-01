# data/ai-os — runtime folder for the AI Entrepreneur OS

Agents write here. **Everything except this file is gitignored** because it will contain lead, client and financial data.

| Path | Written by | Contents |
|---|---|---|
| `drafts/` | every `os-*` agent | one markdown draft per task, named `YYYY-MM-DD-<agent>.md` |
| `morning/` | `os-chief-of-staff` | the one-page Morning Page |
| `approval-queue.md` | `os-approval` | pending cards for the human |
| `approvals.md` | **the human only** | the record of what was approved, by whom, when |
| `watchdog/` | `os-watchdog` | nightly audit of logs and gate bypasses |
| `log/` | the human / hooks | append-only activity log the watchdog reads |

Create the sub-folders on first use (`mkdir -p data/ai-os/{drafts,morning,watchdog,log}`).
