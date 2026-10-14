#!/usr/bin/env python3
"""Mechanical pre-launch checks for static HTML files (stdlib only).

Covers the items of the "20 things to check before you launch" list that can be
decided from page source alone. Everything else is reported as CAN'T CHECK, never guessed.

Usage:  python3 -I scripts/prelaunch_check.py page.html [more.html ...]
Exit status: 0 if no FAIL, 1 if any FAIL.
"""
import re
import sys
from html.parser import HTMLParser

SECRET_PATTERNS = [
    (r"sk-[A-Za-z0-9]{20,}", "OpenAI-style key"),
    (r"AKIA[0-9A-Z]{16}", "AWS access key id"),
    (r"ghp_[A-Za-z0-9]{30,}", "GitHub token"),
    (r"xox[baprs]-[A-Za-z0-9-]{10,}", "Slack token"),
    (r"AIza[0-9A-Za-z_-]{30,}", "Google API key"),
    (r"(?i)(api[_-]?key|secret|password|token)\s*[:=]\s*['\"][^'\"]{12,}['\"]", "hard-coded credential"),
]


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.meta, self.links, self.imgs, self.forms, self.inputs = {}, [], [], 0, []
        self.html_lang = None
        self.title = ""
        self._in_title = False
        self.anchors = []
        self.text = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.html_lang = a.get("lang")
        elif tag == "title":
            self._in_title = True
        elif tag == "meta":
            key = a.get("name") or a.get("property")
            if key:
                self.meta[key.lower()] = a.get("content", "")
        elif tag == "link":
            self.links.append(a)
        elif tag == "img":
            self.imgs.append(a)
        elif tag == "form":
            self.forms += 1
        elif tag in ("input", "textarea", "select"):
            self.inputs.append(a)
        elif tag == "a":
            self.anchors.append(a.get("href", ""))

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        self.text.append(data)


def check(path):
    src = open(path, encoding="utf-8", errors="replace").read()
    p = Page()
    p.feed(src)
    out = []

    def add(n, name, status, why):
        out.append((n, name, status, why))

    hits = [label for pat, label in SECRET_PATTERNS if re.search(pat, src)]
    add(1, "Secrets off the frontend", "FAIL" if hits else "PASS",
        "found: " + ", ".join(hits) if hits else "no key-like strings matched (pattern check only, not proof)")
    http = re.findall(r"""(?:src|href|action)=["']http://[^"']+""", src)
    add(2, "Force HTTPS", "FAIL" if http else "CAN'T CHECK",
        f"{len(http)} http:// resource link(s)" if http else "server redirect and HSTS cannot be seen from the file")
    hrefs = " ".join(p.anchors).lower()
    add(3, "Privacy policy page", "PASS" if "privacy" in hrefs else "FAIL", "link containing 'privacy'" if "privacy" in hrefs else "no link to a privacy page")
    add(4, "Terms & conditions page", "PASS" if re.search(r"terms|conditions", hrefs) else "FAIL", "link containing 'terms'" if re.search(r"terms|conditions", hrefs) else "no link to a terms page")
    cookie = re.search(r"cookie|consent|cookiebot|onetrust", src, re.I)
    add(5, "Cookie consent banner", "PASS" if cookie else "CAN'T CHECK", "cookie/consent code present" if cookie else "no banner code in this file; may be injected by a script")
    if p.forms:
        bad = [i for i in p.inputs if i.get("type", "text") in ("text", "email", "tel") and "required" not in i and "pattern" not in i]
        add(6, "Form validation", "FAIL" if bad else "PASS", f"{len(bad)} text/email field(s) without required or pattern" if bad else "fields carry required/pattern (client side only; server must validate too)")
        spam = re.search(r"recaptcha|hcaptcha|turnstile|honeypot", src, re.I)
        add(7, "Spam protection", "PASS" if spam else "FAIL", "captcha/honeypot code found" if spam else "form without captcha or honeypot")
    else:
        add(6, "Form validation", "CAN'T CHECK", "no form in this file")
        add(7, "Spam protection", "CAN'T CHECK", "no form in this file")
    t, d = p.title.strip(), p.meta.get("description", "").strip()
    ok = 10 <= len(t) <= 65 and 50 <= len(d) <= 170
    add(8, "Meta titles + descriptions", "PASS" if ok else "FAIL", f"title {len(t)} chars, description {len(d)} chars (aim 10-65 and 50-170)")
    og = p.meta.get("og:image")
    add(9, "Social preview image", "PASS" if og else "FAIL", "og:image set" if og else "no og:image meta tag")
    fav = any("icon" in (l.get("rel") or "").lower() for l in p.links)
    add(10, "Favicon", "PASS" if fav else "FAIL", "icon link present" if fav else "no <link rel=icon>")
    add(11, "Sitemap + robots.txt", "CAN'T CHECK", "lives at the site root, not in this file")
    noalt = [i for i in p.imgs if not i.get("alt")]
    add(12, "Alt text on images", "FAIL" if noalt else ("PASS" if p.imgs else "CAN'T CHECK"), f"{len(noalt)} of {len(p.imgs)} <img> without alt" if p.imgs else "no <img> in this file")
    add(13, "Compress images", "CAN'T CHECK", "file sizes are not visible in the HTML")
    add(14, "Page load speed", "CAN'T CHECK", "needs a real run: use Lighthouse and paste the result")
    add(15, "Color contrast", "CAN'T CHECK", "needs rendered colours: use a contrast checker or Lighthouse")
    vp = "viewport" in p.meta
    add(16, "Mobile friendly", "PASS" if vp else "FAIL", "viewport meta present (layout itself not tested)" if vp else "no viewport meta tag")
    add(17, "Custom 404 page", "CAN'T CHECK", "needs a request to a missing URL")
    add(18, "Fix broken links", "CAN'T CHECK", "needs network requests; empty/placeholder hrefs: " + str(sum(1 for h in p.anchors if h in ("", "#"))))
    an = re.search(r"gtag\(|googletagmanager|plausible|matomo|posthog|umami|analytics", src, re.I)
    add(19, "Set up analytics", "PASS" if an else "FAIL", "analytics snippet present" if an else "no analytics snippet found")
    cta = re.search(r"<(a|button)[^>]*>\s*(get started|sign up|book|buy|contact|start|subscribe|try)", src, re.I)
    add(20, "One clear call to action", "PASS" if cta else "CAN'T CHECK", "button/link with an action verb found" if cta else "no obvious action button; judge by eye")
    return out


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    failed = False
    for path in argv[1:]:
        print(f"== {path}")
        for n, name, status, why in check(path):
            failed |= status == "FAIL"
            print(f"{n:>2}. {status:<11} {name} - {why}")
        print()
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
