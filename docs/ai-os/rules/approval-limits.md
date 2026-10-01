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

Approvals are recorded by a human in `data/ai-os/approvals.md`: date, item id, "approved / rejected", initials. An agent that acts without a matching line is a gate bypass — `os-watchdog` reports it as CRITICAL.
