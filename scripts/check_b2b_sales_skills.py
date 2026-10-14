#!/usr/bin/env python3
"""Structural check of the 50 b2b-sales skills (stdlib only). Run: python3 -I scripts/check_b2b_sales_skills.py
Checks frontmatter, section order, step and check counts, numbering, stage counts and cross-references.
It cannot judge whether the advice is good; see tests/b2b-sales for the behavioural test."""
import os,re,sys
ROOT=os.environ.get('B2B_SKILLS_ROOT') or os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','.claude','skills')
STAGE_COUNTS={1:7,2:8,3:7,4:7,5:6,6:8,7:7}
SECTIONS=['When to use','Inputs','Method','Output','Quality checks','Do not','Related']
def main():
    errs=[];dirs=sorted(d for d in os.listdir(ROOT) if re.match(r'b2b-sales-\d\d-',d))
    names=set(os.listdir(ROOT)); stage_seen={}
    if len(dirs)!=50: errs.append(f'expected 50 skill folders, found {len(dirs)}')
    if 'b2b-sales-standard' not in names: errs.append('b2b-sales-standard is missing')
    nums=[int(d[10:12]) for d in dirs]
    if nums!=list(range(1,51)): errs.append(f'numbering is not 1..50: {nums}')
    for d in dirs:
        p=os.path.join(ROOT,d,'SKILL.md'); e=lambda m: errs.append(f'{d}: {m}')
        if not os.path.exists(p): e('SKILL.md missing'); continue
        t=open(p).read()
        m=re.match(r'---\nname: (.+)\ndescription: (.+)\n---\n',t)
        if not m: e('bad frontmatter'); continue
        if m.group(1)!=d: e(f'name {m.group(1)!r} differs from folder')
        desc=m.group(2)
        if len(desc)>1024: e('description over 1024 characters')
        if 'Use ' not in desc: e('description has no "Use when" trigger')
        heads=re.findall(r'^## (.+)$',t,re.M)
        if heads!=SECTIONS: e(f'sections are {heads}, expected {SECTIONS}')
        body={}
        parts=re.split(r'^## (.+)$',t,flags=re.M)
        for i in range(1,len(parts),2): body[parts[i]]=parts[i+1]
        steps=re.findall(r'^\d+\. ',body.get('Method',''),re.M)
        if len(steps)<5: e(f'only {len(steps)} method steps')
        outs=re.findall(r'^- `## (.+)`$',body.get('Output',''),re.M)
        if len(outs)<5 or outs[-1]!='Assumptions and what could be wrong': e('output headings missing or last heading is not "Assumptions and what could be wrong"')
        if len(re.findall(r'^- ',body.get('Quality checks',''),re.M))<6: e('fewer than 6 quality checks')
        if len(re.findall(r'^- ',body.get('Do not',''),re.M))<3: e('fewer than 3 "do not" items')
        if 'b2b-sales-standard' not in t: e('does not reference b2b-sales-standard')
        for ref in re.findall(r'`(b2b-sales-\d\d-[a-z0-9-]+)`',t):
            if ref not in names: e(f'broken reference {ref}')
        if re.search(r'\bguarantee[sd]?\b',body.get('Method',''),re.I): e('method uses "guarantee"')
        st=re.search(r'Stage (\d) of 7',t); 
        if not st: e('no stage line')
        else: stage_seen[int(st.group(1))]=stage_seen.get(int(st.group(1)),0)+1
        if len(t.splitlines())<45: e('shorter than 45 lines')
    if stage_seen!=STAGE_COUNTS: errs.append(f'stage counts {stage_seen} differ from {STAGE_COUNTS}')
    for x in errs: print('FAIL',x)
    print(f'{len(dirs)} skills checked, {len(errs)} problems')
    return 1 if errs else 0
if __name__=='__main__': sys.exit(main())
