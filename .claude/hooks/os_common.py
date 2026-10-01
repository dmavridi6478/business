"""Shared helpers for the AI Entrepreneur OS guard, logger and approval tooling.

Everything here is deliberately dependency-free (stdlib only) and fails closed where it matters.
"""
import hashlib
import json
import os
import time

try:
    import fcntl
except ImportError:  # Windows: no locking, still append-only
    fcntl = None

ZERO = "0" * 64
WRITE_TOOLS = ("Write", "Edit", "MultiEdit", "NotebookEdit")

# Paths no agent may ever write, and no Claude Write/Edit call from ANY session may touch.
# approvals.md is written only by scripts/os_approvals.py on a real terminal; log/ only by the hooks;
# the consent/opt-out registry and screened/ only by scripts/os_registry.py.
PROTECTED_EXACT = ("data/ai-os/approvals.md", "data/ai-os/consent-ledger.jsonl", "data/ai-os/opt-outs.jsonl",
                   "data/ai-os/.salt", "data/ai-os/gate-ledger.jsonl")
PROTECTED_PREFIX = ("data/ai-os/log/", "data/ai-os/screened/")

# Where each os-* agent may write (relative to the project root, lower-case). Anything else is denied.
DEFAULT_ALLOW = ("data/ai-os/drafts/",)
# Finding 11: every os-* agent may create injection reports here (create-only, capped), because agents cannot message
# each other or the watchdog. The watchdog and the integrity report read this folder.
FLAGS_DIR = "data/ai-os/flags/"
MAX_FLAGS = 200
ALLOW = {
    "os-chief-of-staff": ("data/ai-os/drafts/", "data/ai-os/morning/"),
    "os-approval": ("data/ai-os/drafts/", "data/ai-os/approval-queue/"),
    "os-watchdog": ("data/ai-os/drafts/", "data/ai-os/watchdog/"),
}
AGENT_PREFIX = "os-"
AGENT_FILE_SUFFIX = ".md"


def project_root(data=None):
    r = os.environ.get("CLAUDE_PROJECT_DIR") or (data or {}).get("cwd") or os.getcwd()
    return os.path.realpath(r)


def real_path(root, raw, cwd=None):
    """Absolute, symlink-resolved path for a tool's file argument."""
    base = cwd or root
    return os.path.realpath(raw if os.path.isabs(raw) else os.path.join(base, raw))


def rel_path(root, raw, cwd=None):
    """Resolve raw (maybe relative, maybe via symlink or ..) to a project-relative lower-case posix path.
    Returns None if it resolves outside the project."""
    real = real_path(root, raw, cwd)
    rel = os.path.relpath(real, root)
    if rel == ".." or rel.startswith(".." + os.sep):
        return None
    return rel.replace(os.sep, "/").lower()


def is_protected(rel):
    return rel in PROTECTED_EXACT or any(rel.startswith(p) for p in PROTECTED_PREFIX)


def allowed_for(agent, rel):
    """True if os-* agent `agent` may write project-relative path `rel`."""
    if rel is None or is_protected(rel):
        return False
    if not rel.endswith(AGENT_FILE_SUFFIX):
        return False
    allow = tuple(ALLOW.get(agent, DEFAULT_ALLOW)) + (FLAGS_DIR,)
    return any(rel == a or (a.endswith("/") and rel.startswith(a)) for a in allow)


def sha256_text(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def utc_now_iso(now=None):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now if now is not None else time.time()))


def append_chained(path, record):
    """Append one JSON line whose 'prev' is the sha256 of the previous line (tamper-evident chain)."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a+", encoding="utf-8") as f:
        if fcntl:
            fcntl.flock(f, fcntl.LOCK_EX)
        f.seek(0)
        lines = f.read().splitlines()
        prev = sha256_text(lines[-1]) if lines else ZERO
        rec = dict(record)
        rec["prev"] = prev
        f.write(json.dumps(rec, sort_keys=True) + "\n")
    return rec


def verify_chain(path):
    """Return (ok, problem). A missing file is ok=True with problem 'missing'. Detects edits, deletions, reordering."""
    if not os.path.exists(path):
        return True, "missing"
    prev = ZERO
    with open(path, encoding="utf-8") as f:
        for n, line in enumerate(f.read().splitlines(), 1):
            try:
                rec = json.loads(line)
            except ValueError:
                return False, "line %d is not valid JSON" % n
            if rec.get("prev") != prev:
                return False, "chain broken at line %d" % n
            prev = sha256_text(line)
    return True, None


def log_dir(root):
    return os.path.join(root, "data", "ai-os", "log")


def log_event(root, event):
    path = os.path.join(log_dir(root), time.strftime("%Y-%m-%d", time.gmtime()) + ".jsonl")
    ev = {"ts": utc_now_iso()}
    ev.update(event)
    return append_chained(path, ev)


# ---------------------------------------------------------------------------------------------------------
# Finding 3 (exfiltration): break the "lethal trifecta" (untrusted content + private data + outbound channel).
# The web-capable agents may fetch from allow-listed hosts but may READ only non-private project docs.
# Every other os-* agent reads private data but has no network tool at all (enforced by a test on frontmatter).
# ---------------------------------------------------------------------------------------------------------
READ_TOOLS = ("Read", "Grep", "Glob")
WEB_AGENTS = ("os-seo", "os-market", "os-pain-point", "os-prospect")
NETWORK_TOOLS = ("WebFetch", "WebSearch")
WEB_READ_ROOTS = ("docs/ai-os/ops/", "docs/ai-os/rules/", "docs/marketing-context/", ".claude/skills/ai-entrepreneur-os/")
FETCH_ALLOWLIST = "docs/ai-os/rules/fetch-allowlist.txt"
MAX_URL_LEN = 300
MAX_QUERY_LEN = 120
MAX_TOKEN_RUN = 60  # a single path/query chunk this long of base64-ish characters looks like smuggled data


def read_allowed(agent, rel):
    """May os-* `agent` read project-relative `rel`? Only the web agents are restricted."""
    if agent not in WEB_AGENTS:
        return True
    if rel is None:
        return False
    return any(rel.startswith(r) for r in WEB_READ_ROOTS)


def load_allowlist(root):
    path = os.path.join(root, *FETCH_ALLOWLIST.split("/"))
    if not os.path.exists(path):
        return []
    out = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.split("#", 1)[0].strip().lower()
            if line:
                out.append(line)
    return out


def fetch_verdict(url, allowlist):
    """Return None if an os-* agent may fetch `url`, otherwise a reason string."""
    import ipaddress
    import re
    from urllib.parse import urlsplit
    if not url or len(url) > MAX_URL_LEN:
        return "URL empty or longer than %d characters" % MAX_URL_LEN
    try:
        u = urlsplit(url)
        host = (u.hostname or "").lower()
        port = u.port
    except ValueError:
        return "URL does not parse"
    if u.scheme != "https":
        return "only https is allowed"
    if u.username or u.password or "@" in u.netloc:
        return "credentials or '@' in the URL"
    if port not in (None, 443):
        return "non-default port"
    if not host or "." not in host:
        return "host has no dot (localhost/intranet)"
    try:
        ipaddress.ip_address(host)
        return "IP-address hosts are not allowed"
    except ValueError:
        pass
    if not allowlist:
        return "allow-list %s is missing or empty (all fetches blocked)" % FETCH_ALLOWLIST
    if not any(host == d or host.endswith("." + d) for d in allowlist):
        return "host %s is not in %s" % (host, FETCH_ALLOWLIST)
    if len(u.query) > MAX_QUERY_LEN:
        return "query string longer than %d characters" % MAX_QUERY_LEN
    for chunk in re.split(r"[/?&=;]", u.path + "?" + u.query):
        if len(chunk) >= MAX_TOKEN_RUN and re.fullmatch(r"[A-Za-z0-9+_=%-]+", chunk):
            return "a %d-character encoded-looking chunk (possible smuggled data)" % len(chunk)
    return None


# ---------------------------------------------------------------------------------------------------------
# Finding 4 (outbound connectors in the main session). Connector tools that can send, change or spend are
# put behind a human confirmation ("ask") for EVERY caller; os-* agents may not call connectors at all.
# Unknown verbs fall on the cautious side. Owner can switch it off at launch: OS_OUTBOUND_MODE=off.
# ---------------------------------------------------------------------------------------------------------
WRITE_VERBS = set("""send reply forward post publish schedule delete trash remove update edit create add set share invite
upload write merge transition execute run apply archive move copy import submit unsubscribe subscribe cancel respond
save push deploy label unlabel resolve revoke suppress unsuppress disable enable activate start stop assign attach
sync convert generate clone rename mark unmark restore retire register put patch void refund charge pay fire trigger
invoke enrol enroll provision manage switch use login connect""".split())
READ_VERBS = set("""get list search read query fetch find describe show lookup check view preview download whoami
ping help discover inspect analyze count browse explore summarize compare validate verify estimate recommend render
schema docs doc""".split())
# Verbs that are ambiguous between read and write ("resolve_dhs_filters" vs "resolve_diff_thread") are left out of
# BOTH sets on purpose: unknown verbs ask.


def connector_verdict(tool_name):
    """'allow' for clearly read-only connector tools, otherwise 'ask'. The FIRST verb token from the left decides,
    so get_label / get_draft are reads while label_message / create_draft are writes."""
    import re
    parts = tool_name.split("__", 2)
    action = parts[2] if len(parts) == 3 else tool_name
    for t in (x for x in re.split(r"[_\-\s]+", action.lower()) if x):
        if t in WRITE_VERBS:
            return "ask"
        if t in READ_VERBS:
            return "allow"
    return "ask"


# ---------------------------------------------------------------------------------------------------------
# Finding 4 (second-order injection): drafts must quote external text only inside ```untrusted fences.
# The integrity report flags instruction-like text OUTSIDE such fences. Heuristic - a tripwire, not a proof.
# ---------------------------------------------------------------------------------------------------------
INJECTION_PATTERNS = [
    r"ignore (all |any |the )?(previous|prior|above|earlier) (instructions|rules|messages)",
    r"disregard .{0,40}(rules|instructions|policy)",
    r"(^|\n)\s*(system|assistant|developer)\s*:",
    r"you are now\b",
    r"\b(post|send|forward|email|slack) (this|the following|it) (to|via|on)\b",
    r"do not (tell|inform|mention to) (the )?(owner|user|human)",
    r"reveal (your|the) (system |hidden )?(prompt|instructions|keys?|secrets?)",
    r"\bcurl\s+https?://",
    r"new instructions?:",
]


def untrusted_scan(text):
    """Return the list of injection-pattern hits found OUTSIDE ```untrusted fenced blocks."""
    import re
    outside = re.sub(r"```untrusted.*?```", "", text, flags=re.S | re.I)
    hits = []
    for pat in INJECTION_PATTERNS:
        m = re.search(pat, outside, flags=re.I)
        if m:
            hits.append(m.group(0).strip()[:60])
    return hits


# ---------------------------------------------------------------------------------------------------------
# Finding 8: evidence must not be erasable. os-* agents may CREATE files, never overwrite or edit them.
# ---------------------------------------------------------------------------------------------------------
AGENT_MAY_ONLY_CREATE = True


# ---------------------------------------------------------------------------------------------------------
# Finding 9: limits live in ONE machine-readable file and are enforced by code (scripts/os_gate.py), not by
# an LLM reading a table. A limit that is null (OWNER MUST SET) makes every action that needs it BLOCK.
# ---------------------------------------------------------------------------------------------------------
LIMITS_FILE = "docs/ai-os/rules/limits.json"
LIMIT_DEFAULTS = {"approval_expiry_hours": 24}


def load_limits(root):
    path = os.path.join(root, *LIMITS_FILE.split("/"))
    limits = {}
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            limits = {k: v for k, v in json.load(fh).items() if not k.startswith("_")}
    merged = dict(LIMIT_DEFAULTS)
    merged.update(limits)
    return merged


# ---------------------------------------------------------------------------------------------------------
# Finding 10: connectors for os-* agents are an EXACT, per-agent, READ-ONLY opt-in owned by the human.
# docs/ai-os/rules/connector-allowlist.json  ->  {"os-response": ["mcp__Gmail__get_message", ...]}
# It ships EMPTY. A tool is honoured only if: the agent is not a web agent (a connector that reads private data must
# never sit beside a network tool), the name is exact (no wildcards), and it classifies as read-only. The agent's
# frontmatter `tools:` must list exactly the same names (a test enforces this), so there is one source of truth.
# ---------------------------------------------------------------------------------------------------------
CONNECTOR_ALLOWLIST = "docs/ai-os/rules/connector-allowlist.json"
CONNECTOR_NAME = r"mcp__[A-Za-z0-9_\-]+__[A-Za-z0-9_\-]+"


def load_connector_allowlist(root):
    """{agent: (exact tool names)}; anything malformed is dropped (fail closed)."""
    import re
    path = os.path.join(root, *CONNECTOR_ALLOWLIST.split("/"))
    if not os.path.exists(path):
        return {}
    try:
        with open(path, encoding="utf-8") as fh:
            raw = json.load(fh)
    except ValueError:
        return {}
    out = {}
    if not isinstance(raw, dict):
        return {}
    for agent, tools in raw.items():
        if agent.startswith("_") or not agent.startswith(AGENT_PREFIX) or not isinstance(tools, list):
            continue
        good = tuple(t for t in tools if isinstance(t, str) and re.fullmatch(CONNECTOR_NAME, t) and connector_verdict(t) == "allow")
        if good:
            out[agent] = good
    return out


def connector_allowed(root, agent, tool):
    if agent in WEB_AGENTS:
        return False
    return tool in load_connector_allowlist(root).get(agent, ())
