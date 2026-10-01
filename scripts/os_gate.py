#!/usr/bin/env python3
"""Action gate for the AI Entrepreneur OS (hostile-review finding 9).  stdlib only.

Limits used to be a table an LLM was asked to respect. This script enforces them in code, at the point of action:

  python3 scripts/os_gate.py check  <ITEM-ID>    read-only verdict; exit 0 = ALLOW, 1 = BLOCK
  python3 scripts/os_gate.py commit <ITEM-ID>    check + record the use (single-use approval, touch counters); exit 0 = go
  python3 scripts/os_gate.py limits              show limits and which are unset (null)
  python3 scripts/os_gate.py status              recent commits

HOW IT BINDS: the action to check is read from the ```action JSON block INSIDE the approved card, so the numbers are
the ones the human approved (the approval is a hash of the exact card text, 24 h expiry, edit voids it). Nothing the
caller passes in can change what is checked. An approval can be committed ONCE.

FAIL CLOSED: a needed limit that is null ("OWNER MUST SET"), an unknown action type, a missing registry, an unknown
timezone, a missing action block - all BLOCK. A sender must proceed only on exit 0 of `commit`.
LIMIT OF THIS DESIGN: nothing in this repo sends anything yet; the gate protects whatever calls it. The connector
confirmation prompt (os_outbound.py) remains the backstop for everything that does not.
"""
import calendar
import json
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), ".claude", "hooks"))
import os_common as C  # noqa: E402
import os_approvals as A  # noqa: E402
import os_registry as R  # noqa: E402

ACTION_RE = re.compile(r"```action[ \t]*\n(.*?)\n```", re.S)
TYPES = ("outbound_touch", "invoice_reminder", "spend", "ad_budget_change", "prospect_batch")
TOUCH_TYPES = ("outbound_touch", "invoice_reminder")
GATED_LIMITS = ("max_spend_per_approval_eur", "approval_expiry_hours", "max_budget_step_pct", "max_touches_per_window",
                "touch_window_days", "prospect_batch_size", "invoice_first_reminder_days", "invoice_escalate_days", "quiet_hours_local")
ADVISORY_LIMITS = ("ad_stop_loss_eur", "target_cost_per_lead_eur", "cash_buffer_eur")


def ledger_path(root):
    return os.path.join(root, "data", "ai-os", "gate-ledger.jsonl")


def ledger(root):
    p = ledger_path(root)
    if not os.path.exists(p):
        return []
    with open(p, encoding="utf-8") as fh:
        return [json.loads(x) for x in fh.read().splitlines() if x.strip()]


def card_action(card):
    blocks = ACTION_RE.findall(card or "")
    if len(blocks) != 1:
        return None, "the card must contain exactly one ```action JSON block (found %d)" % len(blocks)
    try:
        a = json.loads(blocks[0])
    except ValueError as exc:
        return None, "the ```action block is not valid JSON (%s)" % exc
    if not isinstance(a, dict):
        return None, "the ```action block must be a JSON object"
    return a, None


def _num(a, key, errs, lo=0):
    v = a.get(key)
    if isinstance(v, bool) or not isinstance(v, (int, float)) or v != v or v < lo or v in (float("inf"),):
        errs.append("action field %r must be a number >= %s" % (key, lo))
        return None
    return float(v)


def _quiet(limits, tz, now, errs):
    q = limits.get("quiet_hours_local")
    if not isinstance(q, dict) or not re.fullmatch(r"\d{2}:\d{2}", str(q.get("start", ""))) or not re.fullmatch(r"\d{2}:\d{2}", str(q.get("end", ""))):
        errs.append("limit quiet_hours_local is not set (OWNER MUST SET, e.g. {\"start\":\"21:00\",\"end\":\"08:00\"})")
        return
    try:
        from zoneinfo import ZoneInfo
        from datetime import datetime
        local = datetime.fromtimestamp(now, ZoneInfo(tz))
    except Exception:
        errs.append("recipient timezone %r is unknown or time-zone data is unavailable" % (tz,))
        return
    cur = local.hour * 60 + local.minute
    s = int(q["start"][:2]) * 60 + int(q["start"][3:])
    e = int(q["end"][:2]) * 60 + int(q["end"][3:])
    inside = (s <= cur < e) if s <= e else (cur >= s or cur < e)
    if inside:
        errs.append("quiet hours: it is %s for the recipient (%s), quiet window %s-%s" % (local.strftime("%H:%M"), tz, q["start"], q["end"]))


def _need(limits, key, errs):
    v = limits.get(key)
    if v is None or isinstance(v, bool):
        errs.append("limit %s is not set (OWNER MUST SET in docs/ai-os/rules/limits.json)" % key)
        return None
    return v


def evaluate(root, item, now=None, assume_approved=False):
    """Return (allow, reasons, action). `assume_approved` is for the human's preview before approving."""
    now = now if now is not None else time.time()
    errs = []
    cards = A.read_cards(root)
    if item not in cards:
        return False, ["no card with id %r in the approval queue" % item], None
    if not assume_approved:
        st, det = A.status(root, item, now)
        if st != "approved":
            errs.append("approval is %s (%s); a human must approve this exact card" % (st, det))
        if any(e.get("event") == "commit" and e.get("item") == item for e in ledger(root)):
            errs.append("this approval was already used (single-use); a new approval is required")
    ok, why = C.verify_chain(ledger_path(root))
    if not ok:
        errs.append("gate ledger %s" % why)
    action, err = card_action(cards[item])
    if err:
        return False, errs + [err], None
    typ = action.get("type")
    if typ not in TYPES:
        return False, errs + ["unknown action type %r; allowed: %s" % (typ, ", ".join(TYPES))], action
    limits = C.load_limits(root)

    if typ in TOUCH_TYPES:
        channel, purpose = action.get("channel"), action.get("purpose", "marketing" if typ == "outbound_touch" else "service")
        to, text = action.get("to"), action.get("text")
        if channel not in R.CHANNELS or purpose not in R.PURPOSE_BASES or not isinstance(to, str) or not to.strip() or not isinstance(text, str) or not text.strip():
            errs.append("a message action needs channel (%s), purpose (%s), to and text" % ("|".join(R.CHANNELS), "|".join(R.PURPOSE_BASES)))
        else:
            good, reason = R.verdict(root, to, channel, purpose)
            if not good:
                errs.append("recipient not cleared: %s" % reason)
            _quiet(limits, action.get("tz", ""), now, errs)
            mx, win = _need(limits, "max_touches_per_window", errs), _need(limits, "touch_window_days", errs)
            if mx is not None and win is not None and R.health(root)[0]:
                lead = R.ident_hash(root, action.get("lead") or to)
                since = now - win * 86400
                n = sum(1 for e in ledger(root) if e.get("event") == "commit" and e.get("type") in TOUCH_TYPES and e.get("lead") == lead
                        and calendar.timegm(time.strptime(e["ts"], "%Y-%m-%dT%H:%M:%SZ")) >= since)
                if n >= mx:
                    errs.append("touch cap reached: %d touch(es) in the last %s days (limit %s)" % (n, win, mx))
        if typ == "invoice_reminder":
            days = _num(action, "days_late", errs)
            first, esc = _need(limits, "invoice_first_reminder_days", errs), _need(limits, "invoice_escalate_days", errs)
            if days is not None and first is not None and days < first:
                errs.append("invoice is %d days late; first reminder allowed at %s" % (days, first))
            if days is not None and esc is not None and days >= esc:
                errs.append("invoice is %d days late (>= %s): owner call only, no automated reminder" % (days, esc))
    elif typ == "spend":
        amt = _num(action, "amount_eur", errs)
        cap = _need(limits, "max_spend_per_approval_eur", errs)
        if action.get("currency", "EUR") != "EUR":
            errs.append("only EUR spend is supported")
        if amt is not None and cap is not None and amt > cap:
            errs.append("spend EUR %.2f exceeds the per-approval cap EUR %s" % (amt, cap))
    elif typ == "ad_budget_change":
        old, new = _num(action, "old_daily_eur", errs, 0.01), _num(action, "new_daily_eur", errs)
        step, cap = _need(limits, "max_budget_step_pct", errs), _need(limits, "max_spend_per_approval_eur", errs)
        if old and new is not None and step is not None:
            pct = abs(new - old) / old * 100.0
            if pct > step:
                errs.append("budget change of %.1f%% exceeds the %s%% step limit; split it into smaller steps" % (pct, step))
            if new > old and cap is not None and (new - old) > cap:
                errs.append("extra daily spend EUR %.2f exceeds the per-approval cap EUR %s" % (new - old, cap))
    elif typ == "prospect_batch":
        n, mx = _num(action, "count", errs, 1), _need(limits, "prospect_batch_size", errs)
        if n is not None and mx is not None and n > mx:
            errs.append("prospect batch of %d exceeds the limit %s" % (n, mx))
    return (not errs), errs, action


def commit(root, item, now=None):
    allow, reasons, action = evaluate(root, item, now)
    if not allow:
        return False, reasons, None
    lead = ""
    if action["type"] in TOUCH_TYPES and R.health(root)[0]:
        lead = R.ident_hash(root, action.get("lead") or action["to"])
    rec = C.append_chained(ledger_path(root), {"ts": C.utc_now_iso(now), "event": "commit", "item": item, "type": action["type"], "lead": lead})
    return True, ["recorded"], rec


def unset_limits(root):
    lim = C.load_limits(root)
    return ([k for k in GATED_LIMITS if lim.get(k) is None], [k for k in ADVISORY_LIMITS if lim.get(k) is None])


def main(argv):
    root = C.project_root()
    if len(argv) < 2:
        print(__doc__); return 2
    cmd = argv[1]
    if cmd in ("check", "commit") and len(argv) == 3:
        fn = evaluate if cmd == "check" else commit
        allow, reasons, _ = fn(root, argv[2])
        print(("ALLOW" if allow else "BLOCK") + (": " + "; ".join(reasons) if not allow or cmd == "commit" else ""))
        if not allow:
            for r in reasons:
                print("  - " + r)
        return 0 if allow else 1
    if cmd == "limits":
        lim = C.load_limits(root)
        for k in GATED_LIMITS + ADVISORY_LIMITS:
            print("%-30s %s%s" % (k, lim.get(k), "   <-- NOT SET" if lim.get(k) is None else ""))
        return 0
    if cmd == "status":
        for e in ledger(root)[-20:]:
            print(e["ts"], e["item"], e["type"])
        return 0
    print(__doc__); return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
