#!/usr/bin/env python3
"""Mechanical validator for an os-chief-of-staff ROUTING PLAN (hostile-review finding 5).

  python3 scripts/os_plan_check.py data/ai-os/drafts/<date>-routing-plan.md
exit 0 = valid, 1 = invalid (reasons printed), 3 = the chief of staff REJECTED the task (reason printed).

The plan is attacker-influenceable (the chief read the task text), so nothing is trusted: agent names must be real,
paths must stay inside data/ai-os/ or docs/, the step count is capped, and instruction-like text in `do=` fails the plan.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), ".claude", "hooks"))
import os_common as C  # noqa: E402

MODULES = ("Marketing", "Sales", "Finance", "Research and Offer", "Customer Success")
MAX_STEPS = 6
NEVER_PLAN = ("os-chief-of-staff", "os-approval")
SCREENING = ("none", "email", "sms", "phone")
ALLOWED_ROOTS = ("data/ai-os/", "docs/")


def check_plan(root, text):
    """Return (code, [messages]). code 0 valid, 1 invalid, 3 rejected."""
    errs = []
    lines = [l.rstrip() for l in text.splitlines() if l.strip()]
    if not lines or lines[0].strip() != "ROUTING PLAN":
        return 1, ["first line must be exactly 'ROUTING PLAN'"]
    mod = next((l for l in lines if l.startswith("module:")), None)
    if mod is None:
        return 1, ["missing 'module:' line"]
    module = mod[len("module:"):].strip()
    if module.startswith("REJECT"):
        return 3, ["task rejected by os-chief-of-staff: " + module]
    if module not in MODULES:
        errs.append("module %r is not one of %s" % (module, ", ".join(MODULES)))
    steps = [l for l in lines if re.match(r"^step \d+:", l)]
    if not steps:
        errs.append("no steps")
    if len(steps) > MAX_STEPS:
        errs.append("%d steps; at most %d allowed" % (len(steps), MAX_STEPS))
    extra = [l for l in lines[1:] if not l.startswith("module:") and not re.match(r"^step \d+:", l)]
    if extra:
        errs.append("unexpected line(s) in plan: %r" % extra[0][:80])
    for i, line in enumerate(steps, 1):
        m = re.match(r"^step (\d+): (.*)$", line)
        if int(m.group(1)) != i:
            errs.append("step numbering must be 1,2,3...; found step %s at position %d" % (m.group(1), i))
        fields = {}
        for part in m.group(2).split(" | "):
            if "=" not in part:
                errs.append("step %d: field without '=': %r" % (i, part[:40])); continue
            k, v = part.split("=", 1)
            fields[k.strip()] = v.strip()
        unknown = set(fields) - {"agent", "inputs", "screening", "do"}
        if unknown:
            errs.append("step %d: unknown field(s) %s" % (i, ", ".join(sorted(unknown))))
        agent = fields.get("agent", "")
        if not re.fullmatch(r"os-[a-z-]+", agent):
            errs.append("step %d: agent %r is not an os-* name" % (i, agent)); continue
        if agent in NEVER_PLAN:
            errs.append("step %d: %s must never be planned (the command runs it)" % (i, agent))
        if not os.path.exists(os.path.join(root, ".claude", "agents", agent + ".md")):
            errs.append("step %d: no such agent file .claude/agents/%s.md" % (i, agent))
        if fields.get("screening", "") not in SCREENING:
            errs.append("step %d: screening must be one of %s" % (i, "|".join(SCREENING)))
        for path in [p.strip() for p in fields.get("inputs", "").split(",") if p.strip()]:
            if os.path.isabs(path) or ".." in path.replace("\\", "/").split("/"):
                errs.append("step %d: input %r must be repo-relative without '..'" % (i, path)); continue
            if not any(path.replace("\\", "/").startswith(r) for r in ALLOWED_ROOTS):
                errs.append("step %d: input %r is outside %s" % (i, path, " or ".join(ALLOWED_ROOTS)))
            elif path.startswith("docs/") and "*" not in path and not os.path.exists(os.path.join(root, path)):
                errs.append("step %d: input %s does not exist" % (i, path))
        do = fields.get("do", "")
        if not do or len(do) > 200:
            errs.append("step %d: 'do' must be 1-200 characters" % i)
        if re.search(r"https?://|```", do):
            errs.append("step %d: 'do' may not contain URLs or code fences" % i)
        hits = C.untrusted_scan(do)
        if hits:
            errs.append("step %d: 'do' contains instruction-like text (%s)" % (i, "; ".join(hits[:2])))
    return (1, errs) if errs else (0, ["plan valid: module=%s, %d step(s)" % (module, len(steps))])


def main(argv):
    if len(argv) != 2:
        print(__doc__); return 2
    root = C.project_root()
    path = argv[1]
    if not os.path.exists(path):
        print("plan file not found: %s" % path); return 1
    with open(path, encoding="utf-8") as fh:
        code, msgs = check_plan(root, fh.read())
    print("\n".join(msgs))
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv))
