Audit a described software stack for paid tools that have a viable free/open-source alternative from the `lean-software-stack` skill, and recommend whether to switch using the `free-vs-paid-tool-decision` procedure.

Given the stack described in "$ARGUMENTS" (a list of paid tools/subscriptions currently in use, or a description of the business's current tooling — ask the user for this if not provided):

1. For each paid tool mentioned, check whether it falls in a category `lean-software-stack` covers (workspace/docs, notes, password manager, live streaming/recording, video editing, team chat, PDF toolkit, file transfer). Note the matching free alternative if one exists; say plainly when no match exists rather than forcing a weak comparison.
2. For each match, run the `docs/procedures/free-vs-paid-tool-decision.md` steps against the user's actual situation: team size, sync/collaboration needs, support vs. portability trade-off, security/compliance sensitivity, and current business stage.
3. Output a short table: Current tool | Free alternative | Recommendation (switch / keep paid / needs more info) | Why.
4. Don't recommend switching tools that are working fine and aren't costing meaningful money relative to the business's stage — this is a cost-and-control check, not a mandate to self-host everything.
5. If the user's stack includes recurring costs flagged as a leverage leak (per `the-leverage-stack-auditor`), call that connection out explicitly.
