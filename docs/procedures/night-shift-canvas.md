# Procedure: The Night Shift Canvas

## When this applies

Before building or scheduling any autonomous/unattended Claude workflow —
a recurring brief, a scheduled digest, a Routine/cron job, or any
"gather → triage → prepare → deliver" background task. Run this procedure
once per workflow, before the first scheduled run, not after. Backs the
`night-shift-workflow` skill.

## Steps

1. **Output — define what must be ready.** State the exact deliverable in
   concrete terms (e.g. "a Morning Decision Brief answering: what changed
   overnight, what requires attention, what is blocked, which decisions are
   due today, what can safely wait"). A vague objective ("keep me updated")
   cannot be automated reliably — a precise deliverable gives every scheduled
   run the same clear target. Define this first; every other step follows
   from it.

2. **Trigger — decide when it should begin.** Pick the actual mechanism:
   a fixed recurring schedule (a Routine via `create_trigger` or
   `CronCreate`), a self-paced dynamic loop (`ScheduleWakeup`), or a
   one-shot future reminder (`send_later`). State the cadence and timezone
   explicitly — don't leave "runs sometime in the morning" undefined.

3. **Sources — identify where current information actually lives.** List
   each source by name (mail, calendar, a doc store, a project board, web
   research) and confirm it's actually connected and authorized — check
   `ListConnectors` or the equivalent, don't assume. Claude cannot monitor
   what it cannot access; an unconnected source silently produces an
   incomplete brief instead of an error unless this is checked up front.

4. **Rules — write down what deserves attention.** Define explicit
   classification criteria for at least four buckets: Escalate (deadline
   today, financial impact, customer risk, executive decision, blocked
   critical work), Review (material change, emerging risk, conflicting
   information), Include (useful context, no action needed), Ignore
   (duplicates, routine notifications, low-value noise). Vague rules
   ("use judgment") produce noisy output — write specific criteria, then
   refine them against what the first few real runs actually surface.

5. **Actions — decide what Claude may prepare or perform on its own.**
   State explicitly what's in scope for unattended execution: retrieving
   authorized information, comparing against a prior run, classifying
   urgency, drafting the brief, preparing (not sending/executing)
   recommended actions.

6. **Approval — decide where a human must intervene.** State explicitly
   what always requires human sign-off before Claude acts: sending
   sensitive communications, committing money, changing critical records,
   approving consequential decisions, or acting when the evidence gathered
   is incomplete or conflicting. This list is the boundary that keeps the
   workflow inspectable rather than open-ended.

7. **Run the system readiness check before scheduling.** Confirm, out
   loud to the user or in the workflow's own documentation: is the output
   clearly defined? Is the timing appropriate? Are sources connected and
   authorized? Are attention rules documented? Are permitted actions
   clear? Is human approval clearly defined? If any answer is no, the
   workflow is not ready to run unattended — resolve that gap before the
   first scheduled run, not after a bad one.

8. **Revisit when the workflow's job changes.** A canvas answered
   correctly at setup can go stale — a new source gets added, a rule stops
   matching what actually shows up, or the workflow's output starts being
   used for something higher-stakes than originally scoped. Re-run this
   procedure's relevant steps rather than patching the workflow ad hoc.
