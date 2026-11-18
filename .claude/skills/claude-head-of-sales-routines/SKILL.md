---
name: claude-head-of-sales-routines
description: The "Claude Head of Sales" poster (9 routines - 5 weekly, 4 monthly - for founders, sales leaders and small sales teams) turned into a working method - Monday pipeline review, Tuesday target accounts, Wednesday message review, Thursday deal clinic, Friday week in numbers, then monthly forecast, win/loss, territory and coaching - with the one-file sales context rule, a prompt skeleton and the data each routine needs, and the limits the poster leaves out (no prompts shown, a "comment HEADOFSALES" gate, no CRM access implied). Use when setting up a weekly and monthly sales operating rhythm with Claude, or before running any of the routines.
---

# The Claude Head of Sales - nine routines

Source: one poster, "The Claude Head of Sales" (for founders, sales leaders, small sales teams). The nine routine names, their one-line jobs and the rule "every routine reads one sales context file first" are the poster's. The prompt skeletons, data lists and cautions are my additions: the poster shows no prompts, ends with "Comment HEADOFSALES for free access", and states no results.

The seat at the top: "Head of Sales reads the pipeline, flags the risk, preps the week."

## The nine routines

| When | Routine | Poster's one-line job | Data you must supply |
|---|---|---|---|
| Mon | Pipeline review | What moved, what went quiet | Deal list with stage, amount, owner, last activity date, last stage change |
| Tue | Target accounts | Who to go after, and why now | Your ideal customer profile, a candidate account list, any real trigger events you have |
| Wed | Message review | Tighten it before it goes out | The draft message, the recipient's role, what you know about them |
| Thu | Deal clinic | The 3 deals most at risk | The deal list plus notes: buyer roles, next step, close date, blockers |
| Fri | Week in numbers | Five lines on what happened | Weekly counts: meetings, new pipeline, advanced, closed won, closed lost |
| Monthly | Forecast | Ranges, not guesses | History of closed deals, stage-by-stage conversion, current pipeline |
| Monthly | Win / loss | Why deals closed | Closed deals with the reasons recorded by the rep or buyer |
| Monthly | Territory | Where the effort goes | Accounts by segment or region, owner, activity and results |
| Monthly | Coaching | One thing per seller | Per-seller activity and outcome data plus call notes you are allowed to share |

## The one file: `sales-context.md` (the poster's rule)

Every routine begins by reading this file, so keep it short and current: who you sell to, what you sell and at what price, your stages and their exit criteria, ideal customer profile, top three competitors, the sales motion, targets, and rules (what the assistant must not do). Without it each run starts from nothing. Treat it as confidential company data.

## Prompt skeleton for any routine (my addition)

```
Read sales-context.md first. Task: [routine name].
Data I am pasting: [list].
Produce: [the poster's one-line job, in 5 bullets or fewer].
Rules: use only the data I pasted; if a field is missing, say so and ask; no invented numbers, no invented buyer facts; mark anything that is a judgement call.
End with: Not checked, and the one action I should take today.
```

## What the routines can and cannot do

- **Pipeline review (Mon).** Flag deals with no activity in N days (set N from your cycle length), stalled stages and slipped dates. It reads what you paste; it does not see your CRM.
- **Target accounts (Tue).** "Why now" must cite a real trigger you supply (funding, hiring, a leadership change, product news). Ask Claude to list assumptions; do not let it invent triggers.
- **Message review (Wed).** Tighten, never send. Check every claim about the prospect against a source.
- **Deal clinic (Thu).** Rank by risk using your criteria (no champion, no next step, slipped close date, single-threaded). The ranking is a prompt for your judgement, not a verdict.
- **Week in numbers (Fri).** Five lines of what the data says; recompute totals yourself.
- **Forecast (monthly).** "Ranges, not guesses": give the range from your stage conversion history. With fewer than a few dozen historical deals the range is wide; say so.
- **Win / loss.** Loss reasons recorded by sellers are often unreliable; if you can, ask buyers.
- **Territory.** Moves of accounts between sellers are a management decision; Claude only shows the evidence.
- **Coaching.** One thing per seller from data you may legally use; do not paste personal data or recordings you do not have consent to process, and follow your employment and privacy rules.

## Making it a rhythm

Run each routine as a saved prompt in a Claude Project holding `sales-context.md`, or schedule a reminder for yourself (Mon 08:30, Fri 16:00, first working day of the month). Automating it against a CRM would need an authorised connector or n8n workflow with read-only access; none is set up here, and nothing is sent, posted or changed by these routines.

## Poster problems

- Free access is gated behind a comment keyword; the actual prompts are not visible.
- No evidence of results, time saved or forecast accuracy.
- "Claude Head of Sales" is a label: it does not replace a head of sales who owns the team, the target and the relationships.

Related: `cowork-sales-prompts-10`, `claude-sales-by-role`, `sales-workflow-catalog`, `sales-methodologies-20`, `one-person-sales-system`, `revops`, `cmo-operating-cadence`. Use `/head-of-sales [routine]` to run one.
