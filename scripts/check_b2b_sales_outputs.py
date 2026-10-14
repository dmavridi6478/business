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
NUM=re.compile(r'(?<![\w.#/-])\$?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?%?')
DUR=re.compile(r'^\s*[-–]?\s*(minutes?|mins?|min\b|hours?|hrs?|days?|weeks?|months?|seconds?|touches|touch|steps?|emails?|calls?|messages?)',re.I)
WORDS={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,'twenty':20,'thirty':30,'forty':40,'fifty':50,'sixty':60,'seventy':70,'eighty':80,'ninety':90,'hundred':100}
def nums(text):
    out=set()
    for w,v in WORDS.items():
        if re.search(r'\b'+w+r'\b',text,re.I): out.add(str(v))
    for m in re.finditer(r'\b('+'|'.join(WORDS)+r')\s+(?:percent|per cent)\b',text,re.I): out.add(str(WORDS[m.group(1).lower()])+'%')
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
    lines=result.splitlines(); hdr_tag={}
    for i,l in enumerate(lines):  # a table whose header row carries a [calc]/[assumption] tag tags all its rows
        if l.lstrip().startswith('|'):
            j=i
            while j>0 and lines[j-1].lstrip().startswith('|'): j-=1
            hdr_tag[i]=bool(re.search(r'\[calc|\[assumption',' '.join(lines[j:min(j+2,len(lines))]),re.I))
    for ln,line in enumerate(lines,1):
        if re.search(r'\[calc|\[assumption',line,re.I) or hdr_tag.get(ln-1): continue
        if re.match(r'^\s*\|?[\s:|-]+\|?\s*$',line): continue
        for m in NUM.finditer(line):
            raw=m.group(0); v=raw.lstrip('$').replace(',','').rstrip('%')
            if v in allowed or raw.lstrip('$').replace(',','') in allowed: continue
            if re.fullmatch(r'\d{1,2}',v) and int(v)<=12 and not raw.startswith('$') and not raw.endswith('%'): continue
            if re.fullmatch(r'20(2[4-9])',v): continue
            tail=line[m.end():m.end()+14]; head=line[max(0,m.start()-8):m.start()]
            if re.search(r'(day|week|step|email|touch|month|skill|\bw)s?\s*$',head,re.I) and float(v)<=120: continue
            if re.match(r'^\s*[-–]\s*\d+\s*(minutes?|mins?|hours?|days?|weeks?)\b',tail,re.I) and float(v)<=120: continue
            if not raw.startswith('$') and not raw.endswith('%') and DUR.match(tail) and float(v)<=120: continue
            fails.append(f'line {ln}: untagged number {raw!r}: {line.strip()[:90]}')
    if case.get('quotes'):
        src=norm(inputs_text+' '+case['request'])
        # an opening quote follows line start, space or an opening bracket; this stops mispairing of stray quote marks
        for m in re.finditer(r'(?:(?<=^)|(?<=[\s(\[{:;\u2014-]))"([^"\n]{15,})"(?![A-Za-z])',norm(result),re.M):
            q=m.group(1).strip().rstrip('.,;')
            if q.lower().strip('.')=='' or q.endswith('?'): continue
            parts=[p.strip().rstrip('.,;') for p in re.split(r'\s*\.\.\.\s*|\s*…\s*',q) if len(p.strip())>=8]
            if parts and not all(p.lower() in src.lower() for p in parts): fails.append(f'quote not an exact excerpt: "{q[:80]}"')
    if case.get('draft') and not re.search(r'draft[^.\n]{0,60}need(s)?\s+(approval|review)',result,re.I): fails.append('missing "draft, needs approval" label')
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
