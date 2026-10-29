---
name: pmp-formulas-cheat-sheet
description: The 12-section PMP formulas cheat sheet (earned value, schedule, cost and resource, quality, risk, procurement, stakeholder, communication, benefit, PERT and distributions, NPV) transcribed with variables, when to use each, and a worked example, plus the Excel workbook Artifacts/business/pmp-project-dashboard.xlsx that calculates them. Use when computing project health (CPI, SPI, EAC, TCPI), float, expected monetary value, PERT estimates, ROI or NPV, or when building a project-controls dashboard.
---

# PMP formulas cheat sheet

Source: a "PMP Formulas Cheat Sheet" image. Its own note: PMP does not require memorising formulas; use the right formula, understand the inputs and assumptions.

## 1. Earned value management
PV planned value; EV earned value; AC actual cost; BAC budget at completion.
CV = EV - AC. SV = EV - PV. CPI = EV / AC. SPI = EV / PV.
EAC: (a) BAC / CPI; (b) AC + (BAC - EV) / CPI. VAC = BAC - EAC.
ETC: (a) EAC - AC; (b) (BAC - EV) / CPI.
TCPI: (a) (BAC - EV) / (BAC - AC); (b) (BAC - EV) / ETC.

## 2. Schedule management
Forward pass: ES = max(EF of predecessors); EF = ES + duration.
Backward pass: LF = min(LS of successors); LS = LF - duration.
Total float = LS - ES = LF - EF. Free float = min(ES of successors) - EF. Independent float = max(0, min(ES of successors) - max(EF of predecessors) - duration).
Critical path: zero total float; project duration = max EF.

## 3. Cost and resource management
CV = EV - AC. CPI = EV / AC. BV = BAC - EV. EAC = AC + (BAC - EV)/CPI or BAC/CPI. ETC = EAC - AC. TCPI as above.
Resource utilization (%) = actual units / available units x 100.

## 4. Quality management
Defect density = defects / size. DPMO = defects / opportunities x 1,000,000. Yield (%) = (opportunities - defects) / opportunities x 100.
Cost of quality = prevention + appraisal + failure (internal + external).

## 5. Risk management
Risk exposure = probability x impact. EMV = sum(probability x impact). Decision tree EV = sum(probability of path x payoff). RPN = probability x impact x detectability. Monte Carlo: simulate distributions for mean, standard deviation and P(X <= x).

## 6. Procurement management
TCO = purchase price + operating + maintenance + disposal. Make or buy: net benefit = cost of purchase - cost to make; choose the option with the higher net benefit. Seller performance index = sum(weight x rating), weights sum to 1.0.

## 7. Stakeholder management
Influence and interest scored 0-5. Stakeholder impact index = (influence + interest) / 2. Engagement impact = SII x engagement level.

## 8. Communication management
Communication effectiveness (%) = messages received and understood / total messages sent x 100. Efficiency = useful communication / total communication. Information overload index = volume of information / capacity to absorb.

## 9. Benefit management
ROI (%) = net benefits / total investment x 100. BCR = total benefits / total costs. Payback (years) = initial investment / annual net benefits. NPV = sum over t of (benefits_t - costs_t) / (1 + r)^t.

## 10 to 12. Summary, distributions, NPV
Summary table: CPI cost performance; SPI schedule performance; EAC forecast at completion; TF = LS - ES schedule flexibility; RE = P x I risk size; EMV decision making; DPMO = D/Opp x 10^6 process quality; TCO = sum of costs; SII = (I + I)/2 stakeholder priority; ROI = B/I x 100.
PERT (beta): E = (O + 4M + P) / 6; variance = ((P - O) / 6)^2. Triangular: E = (O + M + P) / 3. Standard deviation = sqrt(sum((x - mean)^2) / (n - 1)).
NPV = sum from t=0 to n of cash flow_t / (1 + r)^t, cash flow_0 = - initial investment. NPV > 0 accept; = 0 break even; < 0 reject.

## Reading it critically
- The sheet's TCPI (b) "(BAC - EV) / ETC" is correct only when ETC is the revised estimate to complete (EAC - AC).
- DPMO as printed divides by opportunities; strictly it is defects divided by units times opportunities per unit.
- "Choose the option with the higher net benefit" in make-or-buy depends on the sign convention above; check it with real numbers.
- Use `/pmp-formula [question or numbers]` to pick the formula and compute with inputs shown.
