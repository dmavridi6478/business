# Batch 108 (files numbered 112) - action plan

Input: `97c95fa1-iCloud_Photos.zip` with 5 JPEG repo cards from @sitetusk: FreeCAD/FreeCAD, ossu/computer-science, jqlang/jq, imthenachoman/How-To-Secure-A-Linux-Server, FreshRSS/FreshRSS. No prompts, workflows, agents or connectors are described in these images.

## 1. Created (committed)
| Source | Skill | Command |
|---|---|---|
| All five cards | sitetusk-free-tools-5 | /free-tool-pick |
| jq card | jq-json-cookbook (12 recipes, each run on jq 1.7) | /jq-filter |
| Linux guide card | linux-server-hardening-guide | /harden-server |
Design: template `repo-card-stone-teal` (rendered and checked). User-run `scripts/batch112-install.sh` (asks before each step; syntax checked, not run).

## 2. Executed
- Confirmed with `git ls-remote` that all five repositories exist.
- Read licences from each repo's own file: FreeCAD LGPL-2.1; OSSU MIT; jq MIT (COPYING); Linux guide CC BY-SA 4.0 (LICENSE.txt); FreshRSS AGPL-3.0 (LICENSE.txt).
- Ran every jq recipe against sample JSON with jq 1.7 and recorded the real output in the skill.
- Read from the OSSU README: about 2 years at roughly 20 hours a week. Read from the FreshRSS Docker README: it gives a docker run example and a Compose section.

## 3. Not done - needs you
| Item | Why | Step |
|---|---|---|
| Install FreeCAD, jq, FreshRSS on your machine | Cloud session cannot install on your computer | Run `scripts/batch112-install.sh` locally |
| Run FreshRSS | It is a server you must patch and back up; AGPL-3.0 | Follow the Docker README first |
| Harden any server | Advice only; no server access | Use `/harden-server` to plan, apply on a test machine first |

## 4. Prompts in plain text
The images contain no prompts. Prompts for the new commands:
- `/free-tool-pick I want to learn computer science without a degree`
- `/jq-filter total of paid orders per customer from orders.json`
- `/harden-server small Ubuntu 24.04 VPS running a web app, no test copy yet`

## 5. Claims to treat as unverified
- "release v1.1.4" on the FreeCAD card and "41.27 EUR/week" on the FreshRSS card are snapshots from one day.
- I did not read the Linux guide's chapters; the skill says so and gives only general safe practice.
- Maintenance status and security posture of the five projects were not assessed beyond existence and licence.
- The earlier batch 103 entry for FreshRSS ("not installed") is unchanged; nothing was installed in this batch.
