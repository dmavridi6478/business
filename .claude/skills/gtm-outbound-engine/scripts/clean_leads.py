#!/usr/bin/env python3
"""Clean, deduplicate and normalise a lead CSV (step 2 of the gtm-outbound-engine pipeline).

Usage: python3 clean_leads.py input.csv output.csv [--report report.txt]

Expected columns (case-insensitive, any subset): first_name, last_name, email,
title / job_title, company, company_domain / domain / website, linkedin_url, phone.
Stdlib only.
"""
import csv, re, sys
from urllib.parse import urlparse

TITLE_MAP = [  # (pattern, normalised title, seniority)
    (r"\b(ceo|chief executive)\b", "CEO", "C-level"),
    (r"\b(cfo|chief financial)\b", "CFO", "C-level"),
    (r"\b(cmo|chief marketing)\b", "CMO", "C-level"),
    (r"\b(cto|chief technology)\b", "CTO", "C-level"),
    (r"\b(coo|chief operating)\b", "COO", "C-level"),
    (r"\b(cro|chief revenue)\b", "CRO", "C-level"),
    (r"\bfounder|co-?founder\b", "Founder", "C-level"),
    (r"\b(vp|vice president)\b", "VP", "VP"),
    (r"\b(head of)\b", "Head", "Director"),
    (r"\bdirector\b", "Director", "Director"),
    (r"\bmanager|mgr\b", "Manager", "Manager"),
    (r"\b(lead|principal)\b", "Lead", "Individual"),
]
FUNCTIONS = ["marketing", "sales", "revenue", "operations", "finance", "procurement",
             "engineering", "product", "hr", "people", "it", "medical", "clinical", "growth"]
FREE_MAIL = {"gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "icloud.com", "me.com",
             "live.com", "aol.com", "proton.me", "protonmail.com", "gmx.com", "yahoo.gr"}
EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")


def col(row, *names):
    for n in names:
        for k, v in row.items():
            if k and k.strip().lower() == n:
                return (v or "").strip()
    return ""


def norm_domain(value):
    v = value.strip().lower()
    if not v:
        return ""
    if "@" in v:
        v = v.split("@", 1)[1]
    if "://" not in v:
        v = "http://" + v
    host = urlparse(v).netloc.split(":")[0]
    return host[4:] if host.startswith("www.") else host


def norm_title(raw):
    t = re.sub(r"\s+", " ", raw.replace("&", " and ")).strip()
    low = t.lower()
    level, seniority = "", "Individual"
    for pat, name, sen in TITLE_MAP:
        if re.search(pat, low):
            level, seniority = name, sen
            break
    func = next((f.title() for f in FUNCTIONS if re.search(rf"\b{f}\b", low)), "")
    clean = t.title() if t.isupper() or t.islower() else t
    clean = re.sub(r"\b(Of|And|The|For)\b", lambda m: m.group(1).lower(), clean)
    clean = re.sub(r"\b(Vp|Svp|Evp|Ceo|Cfo|Cmo|Cto|Coo|Cro|Hr|It|Gtm|Revops|B2B|Seo)\b",
                   lambda m: {"Revops": "RevOps", "B2B": "B2B"}.get(m.group(1), m.group(1).upper()), clean)
    return clean, level, func, seniority


def norm_name(s):
    s = re.sub(r"\s+", " ", s).strip()
    return s.title() if s.isupper() or s.islower() else s


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    src, dst = sys.argv[1], sys.argv[2]
    report_path = sys.argv[sys.argv.index("--report") + 1] if "--report" in sys.argv else None
    with open(src, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    seen, out, stats = set(), [], {"in": len(rows), "dup": 0, "bad_email": 0, "free_mail": 0}
    for r in rows:
        email = col(r, "email", "work_email").lower()
        domain = norm_domain(col(r, "company_domain", "domain", "website") or email)
        linkedin = col(r, "linkedin_url", "linkedin").lower().rstrip("/").split("?")[0]
        first, last = norm_name(col(r, "first_name", "firstname")), norm_name(col(r, "last_name", "lastname"))
        title, level, func, seniority = norm_title(col(r, "title", "job_title"))
        valid = bool(EMAIL_RE.match(email)) if email else False
        if email and not valid:
            stats["bad_email"] += 1
        free = email.split("@")[-1] in FREE_MAIL if valid else False
        stats["free_mail"] += free
        key = email if valid else (linkedin or f"{first}|{last}|{domain}".lower())
        if key in seen:
            stats["dup"] += 1
            continue
        seen.add(key)
        out.append({"first_name": first, "last_name": last, "email": email if valid else "",
                    "email_status": "valid_format" if valid else ("invalid" if email else "missing"),
                    "free_mail": "yes" if free else "no", "title": title, "title_level": level,
                    "function": func, "seniority": seniority,
                    "company": re.sub(r"\s+", " ", col(r, "company", "company_name")).strip(),
                    "company_domain": domain, "linkedin_url": linkedin,
                    "phone": re.sub(r"[^\d+]", "", col(r, "phone", "mobile"))})
    fields = list(out[0].keys()) if out else ["email"]
    with open(dst, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(out)
    stats["out"] = len(out)
    msg = (f"Input rows: {stats['in']}\nDuplicates removed: {stats['dup']}\n"
           f"Invalid email format: {stats['bad_email']}\nFree-mail addresses (not B2B): {stats['free_mail']}\n"
           f"Output rows: {stats['out']}\n")
    print(msg, end="")
    if report_path:
        open(report_path, "w").write(msg)


if __name__ == "__main__":
    main()
