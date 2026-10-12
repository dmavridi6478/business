---
name: operational-excellence-5-stages
description: The @succeed_at_work "5 Stages of Operational Excellence" build-in-order model - 1 Standardise, 2 Measure, 3 Improve, 4 Automate, 5 Innovate - each with what to do, how to achieve it, and a "ready to move on when" test, plus how it differs from the Partaker 5-layer ring in operational-excellence-layers. Use when diagnosing which stage a process or team is at, deciding whether to automate yet, or building an operations roadmap in order.
---

# 5 stages of operational excellence (build in order)

Rule: get the foundations right before you scale; skip them and you usually scale the problem.

| Stage | Goal | What to do -> how to achieve it | Ready to move on when |
|---|---|---|---|
| 1 Standardise | make good work repeatable | define roles and ownership -> job descriptions + RACI; agree the core process -> process map / SOP; simple checklists -> checklist template; document the best known way -> work instructions / playbook; reduce unnecessary variation -> templates + standards | the result does not depend on who does the work |
| 2 Measure | make performance visible | define useful measures -> KPIs / scorecard; set a baseline -> baseline report; track time, quality, cost, outcomes -> dashboard; make bottlenecks visible -> process view; review exceptions, not just averages -> exception report | you can see where performance is breaking down |
| 3 Improve | fix the process before adding technology | remove unnecessary steps -> process simplification; reduce handoffs and delays -> swimlane map; fix recurring root causes -> root cause analysis (5 whys); test small changes quickly -> pilot / experiment; make successful changes the standard -> updated SOP | better performance comes from the process, not heroic effort |
| 4 Automate | remove repeatable effort; technology should remove effort, not hide a broken process | target repetitive work -> workflow / RPA; connect systems and data -> system integration; remove manual re-entry -> auto-populate / single source; automate routine decisions -> business rules / decision tree; keep people for judgement and exceptions -> exception handling / approval | automation removes work without creating new work elsewhere |
| 5 Innovate | challenge how the work is done at all; do not just optimise the current model | challenge old assumptions -> question legacy rules / redesign workshops; involve customers and frontline -> feedback loops / co-design; test different approaches -> experiments, pilots, prototypes; run small pilots -> trial safely, learn quickly; scale what proves valuable -> roadmap, rollout plan, benefits case | you have found a better way, not the same work done better |

## How this differs from `operational-excellence-layers`
That skill (Eric Partaker's rings) orders the layers Standardisation, **Automation**, Measurement, Continuous Improvement, Innovation. This one puts **Measure before Improve before Automate**. They disagree on when to automate. My view: automate after you can measure and after the process is fixed, because automating first locks in waste; Partaker's order is defensible for small teams where standard work is trivially scriptable. Pick one and say which.

## Use
1. Score each stage 0-2 (absent, partial, in place) from evidence, not opinion.
2. The lowest stage below your current ambition is the binding constraint; work on it before any later stage.
3. For each stage write the artefact (RACI, SOP, scorecard, baseline, swimlane map, workflow spec, pilot plan) and name an owner.
Command: `/opex-stage`. Design template: `opex-stage-brush-card`. Related: `operational-excellence-layers`, `google-cloud-waf-operational-excellence`, `automation-audit-ops`.
