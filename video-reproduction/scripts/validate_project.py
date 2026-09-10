"""Validate project references and timing, without third-party dependencies."""
import json, math, sys
from pathlib import Path

STAGES={'received','analyzed','designed','instructions_ready','frames_ready','tested','delivered'}
STATUSES={'planned','ready','submitted','generated','accepted','accepted_with_deviation','failed'}

def validate(path):
    path=Path(path); data=json.loads(path.read_text(encoding='utf-8')); errors=[]
    def check(ok,msg):
        if not ok: errors.append(msg)
    def number(x): return isinstance(x,(int,float)) and not isinstance(x,bool) and math.isfinite(x)
    check(data.get('schema_version')=='1.0','schema_version must be 1.0')
    check(data.get('stage') in STAGES,'invalid stage')
    check(data.get('delivery_scope') in {'instructions','images','clips','film'},'invalid delivery_scope')
    for key in ['source','confirmed','units','transition_groups','assets','tasks','attempts','unknowns','next_action']:
        check(key in data,'missing '+key)
    indexes={}
    for key in ['units','transition_groups','assets','tasks']:
        items=data.get(key,[]); ids=[x.get('id') for x in items]
        check(all(isinstance(i,str) and i for i in ids),key+': nonempty ids required')
        check(len(ids)==len(set(ids)),key+': duplicate ids')
        indexes[key]=set(ids)
    duration=data.get('source',{}).get('duration_seconds');units=data.get('units',[])
    if data.get('stage')!='received':
        check(bool(data.get('project_id')),'project_id required')
        check(number(duration) and duration>0,'positive source duration required')
        check(bool(units),'analyzed units required')
    prev=0.0
    for u in units:
        a,b=u.get('start_seconds'),u.get('end_seconds')
        check(u.get('kind') in {'shot','phase'},str(u.get('id'))+': invalid kind')
        if number(a) and number(b):
            check(a>=0 and b>a,str(u['id'])+': invalid time range')
            check(abs(a-prev)<=0.05,str(u['id'])+': gap, overlap or unsorted range');prev=b
        else: errors.append(str(u.get('id'))+': numeric timestamps required')
        for ref in u.get('dependencies',[]):check(ref in indexes['units'],str(u['id'])+': unknown dependency '+str(ref))
    if units and number(duration):check(abs(prev-duration)<=0.05,'units do not cover source duration')
    for g in data.get('transition_groups',[]):
        for ref in g.get('unit_ids',[]):check(ref in indexes['units'],str(g['id'])+': unknown unit')
    for a in data.get('assets',[]):
        if a.get('status')=='ready':
            value=a.get('path');check(bool(value),str(a['id'])+': ready asset needs path')
            if value:
                p=Path(value);p=p if p.is_absolute() else path.parent/p
                check(p.is_file(),str(a['id'])+': ready asset missing')
        for ref in a.get('derived_from',[]):check(ref in indexes['assets'],str(a['id'])+': unknown parent asset')
    for t in data.get('tasks',[]):
        ident=str(t['id']);check(t.get('status') in STATUSES,ident+': invalid task status')
        check(bool(t.get('unit_ids')),ident+': unit_ids required')
        check(bool(t.get('criteria')),ident+': criteria required')
        check(bool(t.get('prompt')),ident+': prompt required')
        for ref in t.get('unit_ids',[]):check(ref in indexes['units'],ident+': unknown unit')
        for key in ['input_asset_ids','output_asset_ids']:
            for ref in t.get(key,[]):check(ref in indexes['assets'],ident+': unknown asset '+str(ref))
        if t.get('status') in {'generated','accepted','accepted_with_deviation'}:
            check(bool(t.get('output_asset_ids')),ident+': output required')
        if t.get('status') in {'accepted','accepted_with_deviation'}:
            review=t.get('review',{});check(bool(review.get('method')) and bool(review.get('scope')),ident+': review method and scope required')
            check(bool(review.get('criteria_results')),ident+': criteria results required')
            if t['status']=='accepted_with_deviation':check(bool(review.get('deviations')),ident+': deviation detail required')
    for attempt in data.get('attempts',[]):check(attempt.get('task_id') in indexes['tasks'],'attempt references unknown task')
    cap=data.get('capability_check')
    if cap is not None:
        check(isinstance(cap,dict),'capability_check must be object')
        if isinstance(cap,dict):
            check(cap.get('status') in {'not_checked','partial','checked'},'invalid capability check status')
            check(cap.get('scope') in {None,'instructions','images','clips','film'},'invalid capability scope')
            if cap.get('scope') is not None:check(cap['scope']==data.get('delivery_scope'),'capability scope differs from delivery scope')
            check(cap.get('route') in {None,'agent_tools','assisted','instructions_only'},'invalid capability route')
            rows=cap.get('capabilities',[])
            check(isinstance(rows,list),'capabilities must be list')
            if isinstance(rows,list):
                ids=[]
                for row in rows:
                    if not isinstance(row,dict):errors.append('capability row must be object');continue
                    ident=row.get('id');ids.append(ident)
                    check(isinstance(ident,str) and bool(ident),'capability id required')
                    check(isinstance(row.get('needed'),bool),'capability needed must be boolean')
                    check(row.get('status') in {'verified','unverified','unavailable','not_needed'},'invalid capability status')
                    check(row.get('executor') in {'agent','external_tool','human','unassigned'},'invalid capability executor')
                    if row.get('status')=='verified':
                        check(bool(row.get('evidence')),'verified capability requires evidence')
                        check(row.get('executor')!='unassigned','verified capability requires executor')
                    if row.get('needed') is True:check(row.get('status')!='not_needed','needed capability cannot be not_needed')
                check(len([i for i in ids if isinstance(i,str)])==len(set(i for i in ids if isinstance(i,str))),'duplicate capability ids')
    return errors

if __name__=='__main__':
    try: problems=validate(sys.argv[1])
    except (IndexError,OSError,ValueError,TypeError,KeyError,AttributeError) as e:
        print('FAIL: '+str(e));sys.exit(1)
    print('\n'.join('FAIL: '+x for x in problems) if problems else 'PASS: project structure, timing and references')
    sys.exit(bool(problems))
