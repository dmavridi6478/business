---
name: ai-governance-layers
description: Audit or build an enterprise AI governance program across 6 layers — Inventory, Responsible Deployment, Security & Access, Testing & Monitoring, Human Oversight, and Compliance & Audit. Use when the user asks to set up AI governance, audit their AI program, create AI policy, or assess readiness for enterprise AI at scale. Three postures: ADOPT (build responsibly), DEFEND (test and protect), GOVERN (authorize and oversee).
---

# 6 Layers for Enterprise AI Governance

A structured framework for governing AI systems in organizations — from first deployment through enterprise scale. Three postures, six layers, thirty components.

---

## The Three Postures

| Posture | Layers | Mandate |
|---|---|---|
| **ADOPT** | 1–2 | Build responsibly — know what you have and deploy it right |
| **DEFEND** | 3–4 | Test and protect — secure and monitor what you've built |
| **GOVERN** | 5–6 | Authorize and oversee — maintain human control and compliance |

---

## Layer 1: AI Inventory (ADOPT)

*Know what AI you have before you govern it.*

| Component | What to establish |
|---|---|
| AI System Inventory | Register every AI system, tool, and model in use across the org |
| Risk Classification | Rate each system: low/medium/high risk by impact + autonomy |
| Ownership & Roles | Assign a named owner and stakeholder for every AI system |
| Model & Tool Registry | Track model versions, providers, update cadence, deprecation dates |
| Usage Visibility | Monitor who is using what AI, how often, and for what purpose |

**Audit prompt:**
```
Audit our AI inventory. List every AI system, model, and tool currently in use across our organization.
For each: name, owner, use case, risk classification (Low/Medium/High), vendor, and last reviewed date.
Flag any AI systems with: no named owner, no documented risk classification, or unknown data handling.
Output as a registry table I can use as the foundation for our AI governance program.
```

---

## Layer 2: Responsible Deployment (ADOPT)

*Build with governance baked in, not bolted on.*

| Component | What to establish |
|---|---|
| Use Case Selection | Criteria for deciding which problems AI should and should not solve |
| Architecture & Model Choice | Decision framework: build vs. buy, model selection criteria, provider evaluation |
| Deployment Practices | Rollout process, staging environments, approval gates |
| Change Control | How changes to AI systems are reviewed, approved, and rolled back |
| DevSecOps Integration | Security and compliance checks embedded in the deployment pipeline |

**Policy prompt:**
```
Create a Responsible AI Deployment policy for [organization].
Include: criteria for approving new AI use cases, required architecture review steps, staging/testing requirements before production, change control process for AI updates, and rollback procedures.
Format as a policy document with sections, approval authorities, and a deployment checklist.
```

---

## Layer 3: AI Security & Access (DEFEND)

*Protect the systems and the data they touch.*

| Component | What to establish |
|---|---|
| Identity & Access | Who can access AI systems, with what permissions, under what conditions |
| Context & Data Protection | Data classification, input/output filtering, PII handling |
| Tool & MCP Controls | Which tools and integrations AI agents can invoke, with what limits |
| Access Controls | Role-based access, least-privilege enforcement, audit logging |
| Data Integrity | Preventing prompt injection, data poisoning, unauthorized data exfiltration |

**Security review prompt:**
```
Conduct an AI security review for [system/deployment].
Assess: identity and access controls, data classification and protection, tool invocation limits, access logging, and data integrity risks.
Flag: any system running with overly broad permissions, any AI that can access sensitive data without logging, any tool integration without rate limits or scope controls.
Output: security findings table (Critical/High/Medium/Low) + remediation actions.
```

---

## Layer 4: Testing & Monitoring (DEFEND)

*Know what your AI is doing in production.*

| Component | What to establish |
|---|---|
| Pre-Production Evaluation | Red teaming, bias testing, accuracy benchmarking before launch |
| Red Teaming & Threats | Adversarial testing: prompt injection, jailbreaks, edge cases, failure modes |
| Runtime Monitoring | Real-time visibility into what AI systems are doing, not just whether they're running |
| Drift Detection | Alerting when model behavior, output quality, or input distribution shifts |
| Incident Response | Playbook for AI-specific incidents: what triggers escalation, who responds, how fast |

**Monitoring prompt:**
```
Design a testing and monitoring program for [AI system].
Include: pre-launch evaluation criteria, red team test cases, runtime monitoring metrics and thresholds, drift detection triggers, and incident response playbook.
Define: what "normal" looks like, what anomaly thresholds trigger alerts, who gets alerted, and what the first response action is.
Output as a monitoring spec I can hand to our engineering team.
```

---

## Layer 5: Human Oversight (GOVERN)

*Maintain human authority over consequential AI decisions.*

| Component | What to establish |
|---|---|
| Decision Review | Which AI decisions require human review before action, and which don't |
| Escalation Paths | Clear routing when AI encounters ambiguity, high-stakes decisions, or edge cases |
| Override Authority | Who can override AI decisions, under what conditions, with what documentation |
| Output Validation | Spot-checking and quality-assurance processes for AI-generated outputs |
| Accountability Mapping | Tracing which human is accountable for each category of AI action |

**Oversight design prompt:**
```
Design a human oversight framework for [AI system/use case].
Define: which decisions AI can make autonomously, which require human review, and which must be made by a human with AI only providing information.
Specify: escalation triggers, override authority by role, output validation sampling rate, and accountability mapping.
Output as a decision authority matrix + escalation flowchart.
```

---

## Layer 6: Compliance & Audit (GOVERN)

*Be ready to prove you governed well.*

| Component | What to establish |
|---|---|
| Policy & Decision Rights | Who owns AI policy, who can approve exceptions, governance body structure |
| Regulatory Alignment | Mapping AI systems to applicable regulations (EU AI Act, GDPR, sector-specific) |
| Audit Evidence | What records you keep, for how long, in what format, retrievable how fast |
| Incident Reporting | External disclosure obligations, regulator notification timelines, breach response |
| Audit Trails & Logs | Immutable records of AI system actions sufficient to reconstruct any incident |

**Compliance prompt:**
```
Create an AI compliance and audit readiness plan for [organization] in [industry/jurisdiction].
Map our AI systems to applicable regulations: [EU AI Act / GDPR / HIPAA / SOC 2 / sector-specific].
For each regulation: what is required, what we currently have, what gap exists, and what action closes it.
Define our audit trail requirements: what events to log, retention period, and retrieval process.
Output as a compliance gap table + 90-day remediation roadmap.
```

---

## Full Governance Audit — All 6 Layers

```
Conduct a full AI governance audit for [organization].
Assess all 6 layers: AI Inventory, Responsible Deployment, Security & Access, Testing & Monitoring, Human Oversight, Compliance & Audit.
For each layer: current state (Green/Yellow/Red), specific gaps, risk of each gap, and recommended action.
Prioritize by: (1) regulatory risk, (2) operational risk, (3) reputational risk.
Output as a governance scorecard + prioritized action plan.
```
