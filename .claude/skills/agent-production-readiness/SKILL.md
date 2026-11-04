---
name: agent-production-readiness
description: Go/no-go review for moving an AI agent from demo to production - the six failure causes, the seven parts of a production-ready agent (plan, access context, use tools, validate and guard, monitor and recover, human escalation, learn), the five-step failure-and-recovery loop, and six questions that must be answered before launch. Use when someone asks whether an agent is ready for production, why a proof of concept keeps failing in the real world, or how to design recovery, guardrails and escalation. Run via /agent-prod-check; the recovery loop runs via /agent-recovery. Source - "AI Agents Never Make It to Production" (Ismat Kamal).
---

# AI agents: demo to production

Source thesis: most agents fail **not because of the model but because of what surrounds it**. "Plan for failures. Design for recovery. Build for trust."

## Why agents fail (six causes)

1. Limited context - works on test data, fails on real data.
2. Tool and API reliability - APIs change, time out or return errors.
3. Security and permissions - data leakage, compliance risk.
4. Lack of guardrails - uncontrolled actions, unexpected behaviour.
5. No observability - cannot see what it is doing or why.
6. No human intervention - nowhere to escalate when things go wrong.

## What a production-ready agent needs (seven parts, in flow order)

| Part | Requirement | Evidence to ask for |
|---|---|---|
| Plan | Break the goal down and create a plan | A logged plan per run |
| Access context | Enterprise data with proper permissions | Scoped credentials; least privilege list |
| Use tools / APIs | Interact with systems and complete tasks | Tool list with timeouts and retry policy |
| Validate and guard | Check rules, policies and risk controls | Pre- and post-action checks; blocked-action log |
| Monitor and recover | Detect issues, retry, roll back or continue safely | Alerts; rollback path per write action |
| Human escalation | Hand over when needed | Named owner; escalation trigger conditions |
| Learn and improve | Capture feedback and get better over time | Incident-to-prompt/tool fix process |

## Failure and recovery loop (the five-step runbook)

1. **Detect failure** - identify errors, exceptions, unexpected results.
2. **Understand** - analyse logs, context, root cause.
3. **Recovery options** - retry the action; roll back changes; continue from a safe point; use an alternative tool; escalate to a human.
4. **Resume safely** - continue the task or hand over with full context.
5. **Learn** - capture the incident and improve prompts, tools and processes.

## Six questions before going to production

| Question | Pass condition |
|---|---|
| What can it access? (data, systems, tools) | Written list; each item justified |
| What decisions can it make? | Explicit allowed set; everything else needs approval |
| What happens when it fails? | A tested failure path exists |
| How does it recover? | Rollback or safe-resume demonstrated once |
| Who monitors it? | A named person and an alert channel |
| Can we measure its impact? | One baseline number and one target |

**Rule: if any question cannot be answered confidently, the agent is not ready.** Output the verdict as READY / READY WITH CONDITIONS / NOT READY, with the failing question first.

## Expected outcomes (the source's four)

Higher reliability (fewer failures, faster recovery); greater trust (safe, compliant, transparent); measurable value (business impact, not a demo); scalable adoption.

## Repo mapping

- Guardrail layers -> `ai-guardrails-5-layers`, `add-agent-guardrails`.
- Scanning outputs -> `agent-output-scanners`. Evaluation -> `agent-eval`, `build-eval-and-improve`.
- Approval and audit design -> the AI Entrepreneur OS gates (`docs/ai-os`), `signed-audit-trails-recipe`.
- Ops -> `enterprise-agent-ops`, `agent-architecture-audit`, `production-audit`.

## Keywords
agent production readiness, guardrails, observability, human escalation, failure recovery, go no-go
