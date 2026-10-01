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
# approvals.md is written only by scripts/os_approvals.py on a real terminal; log/ only by the hooks.
PROTECTED_EXACT = ("data/ai-os/approvals.md",)
PROTECTED_PREFIX = ("data/ai-os/log/",)

# Where each os-* agent may write (relative to the project root, lower-case). Anything else is denied.
DEFAULT_ALLOW = ("data/ai-os/drafts/",)
ALLOW = {
    "os-chief-of-staff": ("data/ai-os/drafts/", "data/ai-os/morning/"),
    "os-approval": ("data/ai-os/drafts/", "data/ai-os/approval-queue.md"),
    "os-watchdog": ("data/ai-os/drafts/", "data/ai-os/watchdog/"),
}
AGENT_PREFIX = "os-"
AGENT_FILE_SUFFIX = ".md"


def project_root(data=None):
    r = os.environ.get("CLAUDE_PROJECT_DIR") or (data or {}).get("cwd") or os.getcwd()
    return os.path.realpath(r)


def rel_path(root, raw, cwd=None):
    """Resolve raw (maybe relative, maybe via symlink or ..) to a project-relative lower-case posix path.
    Returns None if it resolves outside the project."""
    base = cwd or root
    p = raw if os.path.isabs(raw) else os.path.join(base, raw)
    real = os.path.realpath(p)
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
    allow = ALLOW.get(agent, DEFAULT_ALLOW)
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
