#!/usr/bin/env python3
"""Deterministic checks of b2b-sales skill outputs (stdlib only).
Usage: python3 -I scripts/check_b2b_sales_outputs.py [results_dir]   (default tests/b2b-sales/results)
Each case in tests/b2b-sales/cases.json names the skill, its input files and flags. For each result file
<id>.md the script checks:
  1 headings: the skill's Output headings all appear, in order, and the last heading is the assumptions one
  2 numbers: every number not in the inputs or the request is small (<= 12), a year, a duration, or sits on a line
    tagged [calc ...] or [assumption ...]. Percentages and currency amounts are never exempt except by tag.
  3 quotes (cases with quotes=true): every quoted span of 15+ characters is an exact excerpt of the inputs
  4 draft label (cases with draft=true): "draft, needs approval" appears
  5 expectations (negative cases): regexes that must or must not match
Limits: a script cannot judge quality. Numbers inside tagged lines are not verified; durations such as '20 minutes' are
allowed because plans propose them; quotes are checked only where a skill promises exact excerpts."""
import json,os,re,sys
ROOT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
def skill_dir(n):
    for d in os.listdir(os.path.join(ROOT,'.claude','skills')):
        if d.startswith(f'b2b-sales-{n:02d}-'): return d
def norm(t): return re.sub(r'\s+',' ',t.replace('“','"').replace('”','"').replace('’',"'").replace('‘',"'"))
NUM=re.compile(r'(?<![\w.#/-])\$?\d[\d,]*(?:\.\d+)?%?')
DUR=re.compile(r'^\s*[-–]?\s*(minutes?|mins?|min\b|hours?|hrs?|days?|weeks?|months?|seconds?|touches|touch|steps?|emails?|calls?|messages?)',re.I)
def nums(text):
    out=set()
    for m in NUM.finditer(text):
        v=m.group(0).lstrip('$').replace(',','')
        out.add(v.rstrip('%')); out.add(v)
    return out
def check(case,result,inputs_text):
    fails=[]
    sd=skill_dir(case['skill']); sk=open(os.path.join(ROOT,'.claude','skills',sd,'SKILL.md')).read()
    out_sec=re.search(r'## Output\n(.*?)\n## ',sk,re.S).group(1)
    heads=re.findall(r'^- `## (.+)`$',out_sec,re.M)
    got=[h.strip() for h in re.findall(r'^## (.+)$',result,re.M)]
    gl=[g.lower() for g in got]
    exp=case.get('expect',{})
    stops_early=bool(exp.get('must_not_match'))  # negative cases that may legitimately stop
    pos=-1
    if not stops_early:
        for h in heads:
            try: i=gl.index(h.lower(),pos+1)
            except ValueError: fails.append(f'missing or out-of-order heading: {h}'); continue
            pos=i
        if got and got[-1].lower()!=heads[-1].lower(): fails.append(f'last heading is "{got[-1]}", expected "{heads[-1]}"')
    allowed=nums(inputs_text+' '+case['request'])
    for ln,line in enumerate(result.splitlines(),1):
        if re.search(r'\[calc|\[assumption',line,re.I): continue
        if re.match(r'^\s*\|?[\s:|-]+\|?\s*$',line): continue
        for m in NUM.finditer(line):
            raw=m.group(0); v=raw.lstrip('$').replace(',','').rstrip('%')
            if v in allowed or raw.lstrip('$').replace(',','') in allowed: continue
            if re.fullmatch(r'\d{1,2}',v) and int(v)<=12 and not raw.startswith('$') and not raw.endswith('%'): continue
            if re.fullmatch(r'20(2[4-9])',v): continue
            tail=line[m.end():m.end()+14]
            if not raw.startswith('$') and not raw.endswith('%') and DUR.match(tail) and float(v)<=120: continue
            fails.append(f'line {ln}: untagged number {raw!r}: {line.strip()[:90]}')
    if case.get('quotes'):
        src=norm(inputs_text+' '+case['request'])
        for m in re.finditer(r'"([^"\n]{15,})"',norm(result)):
            q=m.group(1).strip().rstrip('.,;')
            if q.lower().strip('.')=='' : continue
            parts=[p.strip().rstrip('.,;') for p in re.split(r'\s*\.\.\.\s*|\s*…\s*',q) if len(p.strip())>=8]
            if parts and not all(p in src for p in parts): fails.append(f'quote not an exact excerpt: "{q[:80]}"')
    if case.get('draft') and 'draft, needs approval' not in result.lower(): fails.append('missing "draft, needs approval" label')
    for rx in exp.get('must_match',[]):
        if not re.search(rx,result,re.I|re.M): fails.append(f'expected pattern not found: {rx}')
    for rx in exp.get('must_not_match',[]):
        if re.search(rx,result,re.I|re.M): fails.append(f'forbidden pattern found: {rx}')
    return fails
def main():
    rd=sys.argv[1] if len(sys.argv)>1 else os.path.join(ROOT,'tests','b2b-sales','results')
    cases=json.load(open(os.path.join(ROOT,'tests','b2b-sales','cases.json')))
    bad=0;done=0;missing=[]
    for c in cases:
        p=os.path.join(rd,c['id']+'.md')
        if not os.path.exists(p): missing.append(c['id']); continue
        txt=''.join(open(os.path.join(ROOT,'tests','b2b-sales',x)).read()+'\n' for x in c['inputs'])
        f=check(c,open(p).read(),txt); done+=1
        manual=' (manual review also required)' if c.get('expect',{}).get('manual') else ''
        print(('PASS ' if not f else 'FAIL ')+c['id']+' '+skill_dir(c['skill'])+manual)
        for x in f: print('     -',x)
        bad+=bool(f)
    print(f'{done} results checked, {bad} failed, {len(missing)} missing {missing if missing else ""}')
    return 1 if bad or missing else 0
if __name__=='__main__': sys.exit(main())
