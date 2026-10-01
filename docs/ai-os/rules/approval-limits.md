# Approval limits

Defaults are deliberately strict. Lines marked **OWNER MUST SET** have no safe default — agents must stop and ask rather than assume.

| Limit | Value |
|---|---|
| Spend an agent may commit without approval | **EUR 0** |
| Ad budget change that may be *proposed* in one step | up to **20 %** of the campaign's daily budget (bigger needs a written reason) |
| Ad **stop-loss** (a PAUSE IT verdict needs spend with no real lead beyond this) | **OWNER MUST SET** (suggest: 3x target cost per lead) |
| Target cost per real lead | **OWNER MUST SET** |
| Touches per lead before a forced close-the-loop | **5** over **14 days** |
| Prospect batch size per run | **25** |
| Cash buffer that triggers a cash-flow alert | **OWNER MUST SET** (suggest: 1 month of fixed costs) |
| Invoice age for first reminder draft | **30 days** past due |
| Invoice age that escalates to the owner (no stronger draft) | **60 days** past due |
| Quiet hours for any outbound message | **OWNER MUST SET** (local time of the recipient) |
| Approval expiry | an approval covers the exact text shown; any edit voids it; it expires after **24 h** |

## Approval record

Approvals are recorded only by you, in a terminal: `python3 scripts/os_approvals.py approve <item-id>` (it shows you the card and makes you retype the id). The line carries the sha256 of the exact card text, a timestamp and a hash-chain link, so an edited card voids the approval, a 24-hour-old approval expires, and an altered ledger fails `verify`. Senders must call `python3 scripts/os_approvals.py check <item-id>` and proceed only on exit 0. An agent that acts without it is a gate bypass — the integrity report flags it CRITICAL.
