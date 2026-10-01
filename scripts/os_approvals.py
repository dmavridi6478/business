#!/usr/bin/env python3
"""Human-only approval ledger and integrity report for the AI Entrepreneur OS
(hostile-review fixes 2 and 6).  stdlib only.

  python3 scripts/os_approvals.py list                 pending / approved / voided items
  python3 scripts/os_approvals.py approve <ITEM-ID>    record YOUR decision (needs a real terminal)
  python3 scripts/os_approvals.py reject  <ITEM-ID>
  python3 scripts/os_approvals.py check   <ITEM-ID>    exit 0 only if approved, card unchanged, < 24 h old
  python3 scripts/os_approvals.py verify               is the approvals chain intact?
  python3 scripts/os_approvals.py integrity            write data/ai-os/watchdog/integrity-<date>.json (exit 1 = CRITICAL)

Cards live in data/ai-os/approval-queue.md as '## ITEM <id> ...' blocks (written by os-approval).
An approval is bound to the sha256 of the exact card text: any edit voids it. Approvals expire after
EXPIRY_HOURS (docs/ai-os/rules/approval-limits.md). approvals.md is a hash chain; editing, deleting or
re-ordering a line breaks it. LIMIT: the chain detects tampering, it does not authenticate WHO wrote a line -
that guarantee comes from the guard hook plus the terminal requirement below.
"""
import calendar
import getpass
import json
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), ".claude", "hooks"))
import os_common as C  # noqa: E402

EXPIRY_HOURS = 24
CARD_RE = re.compile(r"^## ITEM (\S+)", re.M)


def paths(root):
    d = os.path.join(root, "data", "ai-os")
    return {"queue": os.path.join(d, "approval-queue.md"), "ledger": os.path.join(d, "approvals.md"),
            "watchdog": os.path.join(d, "watchdog")}


def read_cards(root):
    """{item_id: card_text} from the approval queue."""
    p = paths(root)["queue"]
    if not os.path.exists(p):
        return {}
    with open(p, encoding="utf-8") as fh:
        text = fh.read()
    marks = [(m.start(), m.group(1)) for m in CARD_RE.finditer(text)]
    cards = {}
    for i, (start, iid) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        cards[iid] = text[start:end].strip()
    return cards


def read_ledger(root):
    p = paths(root)["ledger"]
    if not os.path.exists(p):
        return []
    with open(p, encoding="utf-8") as fh:
        return [json.loads(x) for x in fh.read().splitlines() if x.strip()]


def status(root, item, now=None):
    """Return (state, detail). state in approved|rejected|pending|voided|expired|unknown-item."""
    now = now if now is not None else time.time()
    cards = read_cards(root)
    if item not in cards:
        return "unknown-item", "no card with that id in the queue"
    last = None
    for rec in read_ledger(root):
        if rec.get("item") == item:
            last = rec
    if last is None:
        return "pending", "no decision recorded"
    if last["decision"] == "reject":
        return "rejected", last["ts"]
    if last.get("card_sha256") != C.sha256_text(cards[item]):
        return "voided", "card text changed after approval"
    age_h = (now - calendar.timegm(time.strptime(last["ts"], "%Y-%m-%dT%H:%M:%SZ"))) / 3600.0
    if age_h > EXPIRY_HOURS:
        return "expired", "approved %.1f h ago (limit %d h)" % (age_h, EXPIRY_HOURS)
    return "approved", last["ts"]


def record_decision(root, item, decision, by, now=None):
    cards = read_cards(root)
    if item not in cards:
        raise KeyError("no card with id %r in the queue" % item)
    if decision not in ("approve", "reject"):
        raise ValueError("decision must be approve or reject")
    ok, why = C.verify_chain(paths(root)["ledger"])
    if not ok:
        raise RuntimeError("approvals chain is broken (%s); refusing to append" % why)
    return C.append_chained(paths(root)["ledger"], {"ts": C.utc_now_iso(now), "item": item, "decision": decision,
                                                    "card_sha256": C.sha256_text(cards[item]), "by": by})


def integrity(root, now=None):
    now = now if now is not None else time.time()
    day = time.strftime("%Y-%m-%d", time.gmtime(now))
    crit, warn = [], []
    ldir = C.log_dir(root)
    files = sorted(f for f in os.listdir(ldir) if f.endswith(".jsonl")) if os.path.isdir(ldir) else []
    today = os.path.join(ldir, day + ".jsonl")
    events_today = 0
    if not files:
        crit.append("NO EVIDENCE: data/ai-os/log/ is missing or empty. Either no agent ran, or the hooks are not "
                    "loaded - an empty log is NOT proof that nothing bad happened.")
    chain_ok = True
    denials, outside = 0, []
    for f in files:
        full = os.path.join(ldir, f)
        ok, why = C.verify_chain(full)
        if not ok:
            chain_ok = False
            crit.append("LOG TAMPERING: %s - %s" % (f, why))
        with open(full, encoding="utf-8") as fh:
            lines = fh.read().splitlines()
        for line in lines:
            try:
                ev = json.loads(line)
            except ValueError:
                continue
            if f == day + ".jsonl":
                events_today += 1
            if ev.get("event") == "deny":
                if ev.get("ts", "")[:10] == day:
                    denials += 1
            elif ev.get("event") == "tool" and ev.get("tool") in C.READ_TOOLS and \
                    (ev.get("agent_type") or "") in C.WEB_AGENTS:
                tgt = ev.get("target") or ""
                if tgt.startswith("(default") or not C.read_allowed(ev["agent_type"], tgt):
                    outside.append("%s %s READ %s" % (ev.get("ts"), ev["agent_type"], tgt))
            elif ev.get("event") == "tool" and ev.get("tool") == "WebFetch" and \
                    (ev.get("agent_type") or "").startswith(C.AGENT_PREFIX):
                why = C.fetch_verdict(ev.get("target") or "", C.load_allowlist(root))
                if why:
                    outside.append("%s %s FETCH %s (%s)" % (ev.get("ts"), ev["agent_type"], (ev.get("target") or "")[:80], why))
            elif ev.get("event") == "tool" and (ev.get("tool") or "").startswith("mcp__") and \
                    (ev.get("agent_type") or "").startswith(C.AGENT_PREFIX):
                outside.append("%s %s CONNECTOR %s" % (ev.get("ts"), ev["agent_type"], ev.get("tool")))
            elif ev.get("event") == "tool" and ev.get("tool") in C.WRITE_TOOLS and \
                    (ev.get("agent_type") or "").startswith(C.AGENT_PREFIX):
                if not C.allowed_for(ev["agent_type"], ev.get("target")):
                    outside.append("%s %s -> %s" % (ev.get("ts"), ev["agent_type"], ev.get("target")))
    if outside:
        crit.append("GATE BYPASS: %d os-* action(s) outside the policy got through (hooks not enforcing?): %s"
                    % (len(outside), "; ".join(outside[:5])))
    if denials:
        warn.append("%d write attempt(s) were blocked today - read data/ai-os/log/%s.jsonl, deny events" % (denials, day))
    suspicious = []
    ddir = os.path.join(root, "data", "ai-os", "drafts")
    if os.path.isdir(ddir):
        for fn in sorted(os.listdir(ddir)):
            fp = os.path.join(ddir, fn)
            if fn.endswith(".md") and now - os.path.getmtime(fp) < 48 * 3600:
                with open(fp, encoding="utf-8", errors="replace") as fh:
                    hits = C.untrusted_scan(fh.read())
                if hits:
                    suspicious.append("%s: %s" % (fn, "; ".join(hits[:3])))
    if suspicious:
        warn.append("instruction-like text OUTSIDE an ```untrusted fence in %d draft(s) (possible injection, heuristic): %s"
                    % (len(suspicious), " | ".join(suspicious[:5])))
    ok, why = C.verify_chain(paths(root)["ledger"])
    if not ok:
        crit.append("APPROVALS TAMPERING: %s" % why)
    voided = []
    for iid in read_cards(root):
        st, det = status(root, iid, now)
        if st in ("voided",):
            voided.append(iid)
    if voided:
        warn.append("approved cards edited after approval (approval void): %s" % ", ".join(voided))
    report = {"date": day, "log_files": len(files), "log_events_today": events_today, "log_chain_ok": chain_ok,
              "denials_today": denials, "approvals_chain_ok": ok, "voided_items": voided, "suspicious_drafts": suspicious,
              "CRITICAL": crit, "WARNINGS": warn, "verdict": "CRITICAL" if crit else ("WARN" if warn else "OK")}
    os.makedirs(paths(root)["watchdog"], exist_ok=True)
    with open(os.path.join(paths(root)["watchdog"], "integrity-%s.json" % day), "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=2)
    return report


def _need_terminal():
    if not (sys.stdin.isatty() and sys.stdout.isatty()):
        sys.exit("Refused: approving needs a real interactive terminal. A tool call from an agent or Claude's Bash "
                 "tool has none, which is the point. Run this yourself in a terminal.")


def main(argv):
    root = C.project_root()
    if len(argv) < 2:
        print(__doc__)
        return 2
    cmd = argv[1]
    if cmd == "list":
        for iid in read_cards(root):
            print("%-14s %s" % (iid, status(root, iid)[0]))
        return 0
    if cmd in ("approve", "reject"):
        _need_terminal()
        item = argv[2]
        cards = read_cards(root)
        if item not in cards:
            sys.exit("No card with id %r in data/ai-os/approval-queue.md" % item)
        print(cards[item])
        if input("\nType the item id (%s) to confirm you %s EXACTLY this text: " % (item, cmd)).strip() != item:
            sys.exit("Not confirmed. Nothing recorded.")
        rec = record_decision(root, item, cmd, getpass.getuser())
        print("Recorded %s for %s at %s (expires in %d h, void if the card is edited)." % (cmd, item, rec["ts"], EXPIRY_HOURS))
        return 0
    if cmd == "check":
        st, det = status(root, argv[2])
        print("%s: %s" % (st, det))
        return 0 if st == "approved" else 1
    if cmd == "verify":
        ok, why = C.verify_chain(paths(root)["ledger"])
        print("approvals chain: %s%s" % ("OK" if ok else "BROKEN", "" if why is None else " (%s)" % why))
        return 0 if ok else 1
    if cmd == "integrity":
        rep = integrity(root)
        print(json.dumps(rep, indent=2))
        return 1 if rep["CRITICAL"] else 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
