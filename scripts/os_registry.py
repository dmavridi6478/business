#!/usr/bin/env python3
"""Consent / opt-out registry, contact screening and price-list check for the AI Entrepreneur OS
(hostile-review finding 7).  stdlib only.

WHY A SCRIPT: the os-* agents have no shell, so they cannot look anyone up. Screening runs here, outside the model,
and agents only ever see the RESULT (data/ai-os/screened/*.md). If no screened file exists they must refuse.

  init                                         create the registry (salt + two ledgers); safe to re-run
  consent grant|withdraw --identifier X --channel email|sms|phone [--basis consent|contract|legitimate-interest-b2b]
                         --source "where the evidence lives"      grant needs a real terminal; withdraw does not
  optout add    --identifier X [--channel all|email|sms|phone]    works from anywhere (it only ever protects people)
  optout remove --identifier X [--channel ...]                    needs a real terminal
  check  --identifier X --channel C [--purpose marketing|service] exit 0 only if sendable
  screen --in FILE --channel C [--purpose P] [--name N]           extract emails/phones from FILE and write
                                                                   data/ai-os/screened/<date>-<name>.md
  prices check                                                    exit 1 if docs/ai-os/ops/price-list.md has no rows
  status                                                          counts and chain health

Identifiers are stored as HMAC-SHA256 under a random per-install salt (data/ai-os/.salt), so the ledgers contain no
raw email addresses or phone numbers. Phones must be written in international form (+30...). Ledgers are hash-chained.
DEFAULT RULE (not legal advice): marketing needs a recorded 'consent'; service messages accept 'consent' or 'contract'.
Opt-outs always win. Have an adviser confirm the rule for your jurisdiction before loosening it.
"""
import argparse
import hashlib
import hmac
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), ".claude", "hooks"))
import os_common as C  # noqa: E402

CHANNELS = ("email", "sms", "phone")
BASES = ("consent", "contract", "legitimate-interest-b2b")
PURPOSE_BASES = {"marketing": ("consent",), "service": ("consent", "contract")}
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(r"(?<![\w@])\+?\d[\d\s().\-]{7,}\d")
PRICE_LIST = os.path.join("docs", "ai-os", "ops", "price-list.md")


def P(root):
    d = os.path.join(root, "data", "ai-os")
    return {"dir": d, "salt": os.path.join(d, ".salt"), "consent": os.path.join(d, "consent-ledger.jsonl"),
            "optout": os.path.join(d, "opt-outs.jsonl"), "screened": os.path.join(d, "screened")}


def normalise(identifier):
    s = identifier.strip().lower()
    if "@" in s:
        return "email:" + s
    digits = re.sub(r"[^\d+]", "", s)
    if digits.startswith("00"):
        digits = "+" + digits[2:]
    return "tel:" + digits


def ident_hash(root, identifier):
    with open(P(root)["salt"], "rb") as fh:
        salt = fh.read().strip()
    return hmac.new(salt, normalise(identifier).encode(), hashlib.sha256).hexdigest()


def init(root):
    p = P(root)
    os.makedirs(p["dir"], exist_ok=True)
    os.makedirs(p["screened"], exist_ok=True)
    if not os.path.exists(p["salt"]):
        fd = os.open(p["salt"], os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, "wb") as fh:
            fh.write(os.urandom(32).hex().encode())
    for k in ("consent", "optout"):
        if not os.path.exists(p[k]):
            open(p[k], "a").close()


def initialised(root):
    p = P(root)
    return all(os.path.exists(p[k]) for k in ("salt", "consent", "optout"))


def health(root):
    """(ok, problem). Missing registry is a problem; a broken chain is a worse one."""
    if not initialised(root):
        return False, "registry not initialised (run: python3 scripts/os_registry.py init)"
    for k in ("consent", "optout"):
        ok, why = C.verify_chain(P(root)[k])
        if not ok:
            return False, "TAMPERING: %s ledger %s" % (k, why)
    return True, None


def _records(path):
    import json
    with open(path, encoding="utf-8") as fh:
        return [json.loads(x) for x in fh.read().splitlines() if x.strip()]


def _latest(records, key):
    state = {}
    for r in records:
        state[key(r)] = r
    return state


def record_consent(root, identifier, channel, event, basis=None, source="", by="owner", now=None):
    if channel not in CHANNELS:
        raise ValueError("channel must be one of %s" % (CHANNELS,))
    if event == "grant" and (basis not in BASES or not source.strip()):
        raise ValueError("a grant needs --basis (%s) and a non-empty --source" % "|".join(BASES))
    ok, why = health(root)
    if not ok:
        raise RuntimeError(why)
    return C.append_chained(P(root)["consent"], {"ts": C.utc_now_iso(now), "id": ident_hash(root, identifier), "channel": channel,
                                                 "event": event, "basis": basis or "", "source": source, "by": by})


def record_optout(root, identifier, channel, event, by="owner", now=None):
    if channel not in ("all",) + CHANNELS:
        raise ValueError("channel must be all or one of %s" % (CHANNELS,))
    ok, why = health(root)
    if not ok:
        raise RuntimeError(why)
    return C.append_chained(P(root)["optout"], {"ts": C.utc_now_iso(now), "id": ident_hash(root, identifier), "channel": channel,
                                                "event": event, "by": by})


def verdict(root, identifier, channel, purpose="marketing"):
    """Return (sendable, reason)."""
    ok, why = health(root)
    if not ok:
        return False, "REGISTRY UNAVAILABLE: " + why
    h = ident_hash(root, identifier)
    out = _latest([r for r in _records(P(root)["optout"]) if r["id"] == h], lambda r: r["channel"])
    for ch in ("all", channel):
        if ch in out and out[ch]["event"] == "optout":
            return False, "OPTED-OUT (%s)" % ch
    cons = _latest([r for r in _records(P(root)["consent"]) if r["id"] == h], lambda r: r["channel"])
    rec = cons.get(channel)
    if not rec or rec["event"] != "grant":
        return False, "NO RECORDED CONSENT for %s" % channel
    need = PURPOSE_BASES[purpose]
    if rec["basis"] not in need:
        return False, "basis '%s' is not enough for %s (needs %s)" % (rec["basis"], purpose, "/".join(need))
    return True, "basis=%s" % rec["basis"]


def extract_identifiers(text):
    found, seen = [], set()
    for m in EMAIL_RE.finditer(text):
        v = m.group(0)
        if normalise(v) not in seen:
            seen.add(normalise(v)); found.append(v)
    scrubbed = EMAIL_RE.sub(" ", text)
    for m in PHONE_RE.finditer(scrubbed):
        v = m.group(0).strip()
        if len(re.sub(r"\D", "", v)) >= 9 and normalise(v) not in seen:
            seen.add(normalise(v)); found.append(v)
    return found


def screen(root, text, channel, purpose="marketing", name="audience", now=None):
    ok, why = health(root)
    if not ok:
        raise RuntimeError(why)
    now = now if now is not None else time.time()
    ids = extract_identifiers(text)
    sendable, blocked = [], []
    for i in ids:
        good, reason = verdict(root, i, channel, purpose)
        (sendable if good else blocked).append((i, reason))
    day = time.strftime("%Y-%m-%d", time.gmtime(now))
    safe = re.sub(r"[^A-Za-z0-9_-]+", "-", name).strip("-") or "audience"
    path = os.path.join(P(root)["screened"], "%s-%s.md" % (day, safe))
    lines = ["# SCREENED AUDIENCE (generated by scripts/os_registry.py; agents cannot edit this file)",
             "CONSENT CHECK RUN %s | channel=%s | purpose=%s | rule: opt-outs win; marketing needs recorded consent" % (C.utc_now_iso(now), channel, purpose),
             "Draft ONLY for SENDABLE. Never address BLOCKED. An identifier that is in neither list was not in the input and is not cleared.",
             "", "## SENDABLE (%d)" % len(sendable)]
    lines += ["- %s  (%s)" % x for x in sendable] or ["- (none)"]
    lines += ["", "## BLOCKED (%d)" % len(blocked)]
    lines += ["- %s  - %s" % x for x in blocked] or ["- (none)"]
    os.makedirs(P(root)["screened"], exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    return path, len(sendable), len(blocked)


def price_rows(root):
    path = os.path.join(root, PRICE_LIST)
    if not os.path.exists(path):
        return 0
    with open(path, encoding="utf-8") as fh:
        text = re.sub(r"<!--.*?-->", "", fh.read(), flags=re.S)
    rows, seen_sep = 0, False
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
            seen_sep = True
            continue
        if seen_sep and any(cells):
            rows += 1
    return rows


def _terminal(action):
    if not (sys.stdin.isatty() and sys.stdout.isatty()):
        sys.exit("Refused: %s needs a real interactive terminal. Agents and Claude's Bash tool have none, which is the point." % action)


def main(argv):
    root = C.project_root()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("init"); sub.add_parser("status")
    c = sub.add_parser("consent"); c.add_argument("action", choices=["grant", "withdraw"])
    c.add_argument("--identifier", required=True); c.add_argument("--channel", required=True, choices=CHANNELS)
    c.add_argument("--basis", choices=BASES); c.add_argument("--source", default="")
    o = sub.add_parser("optout"); o.add_argument("action", choices=["add", "remove"])
    o.add_argument("--identifier", required=True); o.add_argument("--channel", default="all")
    k = sub.add_parser("check"); k.add_argument("--identifier", required=True); k.add_argument("--channel", required=True, choices=CHANNELS)
    k.add_argument("--purpose", default="marketing", choices=list(PURPOSE_BASES))
    s = sub.add_parser("screen"); s.add_argument("--in", dest="infile", required=True); s.add_argument("--channel", required=True, choices=CHANNELS)
    s.add_argument("--purpose", default="marketing", choices=list(PURPOSE_BASES)); s.add_argument("--name", default="audience")
    pr = sub.add_parser("prices"); pr.add_argument("action", choices=["check"])
    a = ap.parse_args(argv[1:])
    import getpass
    who = getpass.getuser()
    if a.cmd == "init":
        init(root); print("registry ready in data/ai-os/ (salt, consent-ledger.jsonl, opt-outs.jsonl, screened/)"); return 0
    if a.cmd == "status":
        ok, why = health(root)
        print("registry:", "OK" if ok else why)
        if ok:
            print("consent events: %d | opt-out events: %d" % (len(_records(P(root)["consent"])), len(_records(P(root)["optout"]))))
        print("price list rows: %d" % price_rows(root))
        return 0 if ok else 1
    if a.cmd == "consent":
        if a.action == "grant":
            _terminal("recording consent")
        record_consent(root, a.identifier, a.channel, a.action, a.basis, a.source, who)
        print("recorded %s for %s" % (a.action, a.channel)); return 0
    if a.cmd == "optout":
        if a.action == "remove":
            _terminal("removing an opt-out")
        record_optout(root, a.identifier, a.channel, "optout" if a.action == "add" else "remove", who)
        print("recorded opt-out %s (%s)" % (a.action, a.channel)); return 0
    if a.cmd == "check":
        good, reason = verdict(root, a.identifier, a.channel, a.purpose)
        print(("SENDABLE: " if good else "BLOCKED: ") + reason); return 0 if good else 1
    if a.cmd == "screen":
        with open(a.infile, encoding="utf-8", errors="replace") as fh:
            path, n_ok, n_bad = screen(root, fh.read(), a.channel, a.purpose, a.name)
        print("wrote %s | sendable=%d blocked=%d" % (os.path.relpath(path, root), n_ok, n_bad)); return 0
    if a.cmd == "prices":
        n = price_rows(root); print("price list rows: %d" % n)
        if n == 0:
            print("PRICE LIST EMPTY: fill docs/ai-os/ops/price-list.md before any proposal is drafted.")
        return 0 if n else 1
    return 2


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except (RuntimeError, ValueError, KeyError) as exc:
        sys.exit("Error: %s" % exc)
