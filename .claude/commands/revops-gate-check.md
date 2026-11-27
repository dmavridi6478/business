---
description: Run the four-gate RevOps pipeline check (lead matched, rep routed, stage checked, forecast rolled up) on a CRM export
argument-hint: <CRM export path or pasted rows>
---

Use the `gtm-team-roles-revops-boundary` skill. Input: "$ARGUMENTS"

Run Workflow A (RevOps gated pipeline) on the supplied export. Report per gate: pass count, fail count, failing records; the four scorecard numbers where data allows; the three oldest stuck deals. Mark any metric the data cannot support as 'not measured'. Read-only: change nothing in the CRM.
