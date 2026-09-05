# MCP Integration Scoping

SOP for scoping and pitching an MCP-consolidation project — internally or
for a client — instead of presenting "fewer wires" as a pitch on its own.
Backs the `mcp-integration-business-case` skill and the
`mcp-business-case-analyst` agent.

## When this applies

Before proposing (or accepting a request to build) an MCP integration
project: consolidating several point-to-point AI-tool integrations onto
MCP servers, standing up a new MCP server for a tool that doesn't have
one, or advising a client on whether MCP is worth adopting at all.

## Steps

1. **Inventory the real stack.** List every AI client (`N`) and every
   tool/data source (`M`) actually in play or realistically planned within
   the next 2 quarters. Don't inventory tools nobody is using — the case
   only holds for tools genuinely needed by more than one client.
2. **Run the N×M vs N+M math.** Use `mcp-integration-business-case` to
   compute current-state integration count and the MCP-consolidated
   count. If the reduction is small (client only has 1 AI tool, or only
   1-2 tools total), say so — don't force the pitch onto a stack too
   small to benefit.
3. **Price the current state.** For each existing point-to-point
   integration, get a real build cost and an ongoing maintenance cost
   (even a rough monthly-hours estimate). Sum across all `N×M` pairings.
   This is the number the MCP case has to beat — don't skip it and jump
   straight to the "after" pitch.
4. **Run build-vs-buy per tool.** For each tool in the inventory, check
   whether an official or credible community MCP server already exists
   (`mcp-integration-scout`, or direct research). Buy (adopt) where one
   exists and checks out; flag build where none does, and scope that
   build separately — it is real, additional cost, not included in the
   "fewer wires" number.
5. **Sequence the migration by maintenance-cost reduction, not ease.**
   Cut over the pairing duplicated across the most clients first — that's
   where the compounding savings are largest. An easy-but-low-impact
   pairing first just delays the payoff.
6. **State the caveats before anyone signs anything.** Existing
   integrations don't migrate themselves (cutover cost); MCP server
   quality varies between official and community builds; a client on a
   single AI tool won't see much benefit. Put these in the proposal, not
   just in this repo's internal notes.
7. **Re-run at each stack change.** A business case built for 3 clients ×
   5 tools goes stale once a 4th client or 3 more tools show up — the
   reduction gets *more* favorable as the stack grows, so re-running the
   math after growth is worth doing, not just before the initial pitch.

## Red flags to stop and reconsider

- The inventory has fewer than 2 AI clients or fewer than 3 tools — the
  N×M vs N+M gap is too small to justify a consolidation project on its
  own; a targeted single integration may be the better call.
- More than half the tools in the inventory need a **build**, not a
  **buy** — the project is really "build several MCP servers," and should
  be scoped and priced as that, not marketed as adopting an existing
  standard.
- The client can't produce real integration cost/maintenance numbers for
  step 3 — without them, the business case is a shape, not a number; say
  so rather than presenting illustrative figures as if they were real.

## Related

- `mcp-integration-business-case` (skill) — the formulas and structure.
- `mcp-business-case-analyst` (agent) — runs this SOP end to end on a
  specific client's inventory.
- `mcp-integration-scout` (agent) — the build-vs-buy check in step 4.
- `Artifacts/business/mcp-integration-business-case.html` — the
  calculator/diagram template for presenting the output of this SOP.
