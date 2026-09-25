---
description: Run one of the 50 named Claude marketing jobs (strategy, ICP, offers, content, search, social, email, paid, analytics, agencies) against the context files
argument-hint: [job name] [inputs] — or a function name to list its 5 jobs, or blank for the menu
---

Use the `claude-marketing-jobs` skill. Request: "$ARGUMENTS"

1. If blank, show the 11-chapter table and ask which job. If a function name (e.g. "email"), list its 5 jobs with the deliverable each produces and ask which.
2. Read `docs/marketing-context/` (voice, proof, pillars, banned, last-quarter). If a file the job needs is empty or older than 90 days, stop and name it.
3. If the job needs data (CRM export, transcripts, ad data, URLs), ask for it. Never estimate or invent the data.
4. Run the job's prompt. Produce exactly the one deliverable named in bold. Nothing else.
5. Send the output to the `brand-reviewer` agent. Show me the output with the verdict and any claims flagged.
6. End with the next job that logically follows (one line).
