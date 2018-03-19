from datetime import datetime, timedelta, date
from yaml import load
from glob import glob
from sys import stderr
import json, re, markdown, os.path
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

################################################################################
###                         Some helper functions                            ###
################################################################################
def fixworking():
    """change to this script's directory as the working directory"""
    import os, os.path
    os.chdir(os.path.realpath(os.path.dirname(__file__)))


def debug(*args, **kargs):
    """Helper to print to stderr"""
    kargs['file'] = stderr
    print(*args, **kargs)

def prettyjson(d, newlineindent=2, maxinline=79):
    """The way I like to see JSON:
    commas begin lines
    short collections inline
    no extra spaces"""
    s = json.dumps(d, separators=(',',':'))
    indent = 0
    instr = False
    def skipshort(start, maxlen):
        """Given the starting index of a list or dict, returns either
        the same index, if it is too long,
        or the index of the last character of the list/dict"""
        nest = 0
        instr = False
        i = start
        comma = False
        while i < len(s) and ((not comma) or (i < start+maxlen)):
            if instr:
                if s[i] == '\\': i+=1
                elif s[i] == '"': instr = False
            else:
                if s[i] == '"': instr = True
                elif s[i] in '[{': nest += 1
                elif s[i] in ']}':
                    nest -= 1
                    if nest == 0: return i
                elif s[i] == ',': comma = True
            i += 1
        return start
    chunks = []
    i=0
    last=0
    indents = []
    while i < len(s):
        if instr:
            if s[i] == '\\': 
                i+=1
            elif s[i] == '"': instr = False
        elif s[i] == '"': instr = True
        else:
            if s[i] in '[{':
                end = skipshort(i, maxinline-(i-last)-indent)
                if end > i: i = end
                elif (i-last) < 8:
                    indents.append(indent)
                    indent += (i-last)
                else:
                    chunks.append(s[last:i])
                    indents.append(indent)
                    indent += newlineindent
                    chunks.append('\n'+' '*indent)
                    last = i
            elif s[i] in ']}':
                chunks.append(s[last:i])
                chunks.append('\n'+' '*indent + s[i])
                indent = indents.pop()
                last = i+1
            elif s[i] == ',':
                chunks.append(s[last:i])
                chunks.append('\n'+' '*indent)
                last = i
        i += 1
    if last < i: chunks.append(' '*indent + s[last:i])
    return ''.join(chunks)


################################################################################
###                         The main data mungers                            ###
################################################################################

totaling_keys = ('portion', 'drop', 'include', 'exclude')
numgap = re.compile(r'([a-zA-Z])([0-9])')
codeclass = re.compile(r'[{][.][^}]+[}]')

def assignments_json(data):
    import collections
    groups = data['assignments'].get('.groups', {})
    ans = collections.OrderedDict()
    # process exams
    for k,v in data['Special Dates'].items():
        if k.startswith('Exam'):
            ans[k] = {"group":"Exam", "due":v}
            if k.endswith('3'): ans[k]['weight'] = 20/15
            for ex,val in groups.get('Exam', {}).items():
                if not ex.startswith('.') and ex not in totaling_keys and ex not in ans[k]:
                    ans[k][ex] = val
    # and assignments
    for k,v in data['assignments'].items():
        if k.startswith('.'): continue
        if v is None: ans[k] = {}
        else: ans[k] = {_k:_v for _k,_v in v.items() if not (_k.startswith('.') or _k in totaling_keys)}
        if 'group' not in ans[k]:
            for g in groups:
                if k.startswith(g):
                    ans[k]['group'] = g
        for ex,val in groups.get(ans[k].get('group',''), {}).items():
            if ex == '.tester-prefix' and 'files' in ans[k] and 'tester' not in ans[k]:
                if type(ans[k]['files']) is str:
                    ans[k]['tester'] = val + ans[k]['files']
                elif len(ans[k]['files']) == 1:
                    ans[k]['tester'] = val + ans[k]['files'][0]
            if ex.startswith('.') or ex in totaling_keys or ex in ans[k]: continue
            ans[k][ex] = val
        if 'title' not in ans[k] and ans[k].get('group',None) == 'PA' and type(ans[k].get('files',None)) is str:
            ans[k]['title'] = ans[k]['files'][:-3]
    # labs are open for just 1 day
    for k,v in ans.items():
        if v.get('group','') == 'Lab' and 'due' in v and 'open' not in v:
            v['open'] = date(*v['due'].timetuple()[:3])
    # fix date and datetime (to be a str) for JSON export
    for k,v in ans.items():
        for k2 in v:
            if isinstance(v[k2], datetime):
                try: # 3.6 and beyond
                    v[k2] = v[k2].isoformat(sep=' ', timespec='minutes')
                except: # not yet 3.6
                    v[k2] = v[k2].isoformat(sep=' ')[:4+1+2+1+2+1+2+1+2]
            elif isinstance(v[k2], date):
                if k2 == 'open':
                    v[k2] = v[k2].isoformat() + ' 00:00'
                else:
                    v[k2] = v[k2].isoformat() + ' 23:59'
    # sort by due date
    keys = [(v.get('due','~'+k),k) for k,v in ans.items()]
    keys.sort()
    for _,k in keys:
        ans.move_to_end(k)
    return ans

def coursegrade_json(data):
    groups = data['assignments'].get('.groups', {})
    weights, drops, inc, exc = {}, {}, {}, {}
    for k,v in groups.items():
        if 'portion' in v:
            weights[k] = v['portion']
        else:
            weights[k] = 0
        if type(weights[k]) is str:
            try:
                weights[k] = eval(weights[k].replace('%','/100'))
            except: pass
        if 'drop' in v:
            drops[k] = v['drop']
        if 'include' in v:
            inc[k] = v['include']
        if 'exclude' in v:
            exc[k] = v['exclude']
    for k,v in drops.items():
        if type(v) is str:
            v = eval(v.replace('%','/100'))
        if v < 1:
            cnt = 0
            for k,v in assignments_json(data).items():
                if v.get('group','') == k: cnt += 1
            v *= cnt
        drops[k] = int(round(v))
    return {'letters':[
        # {'A+':0.98},
        {'A' :0.93},
        {'A-':0.90},
        {'B+':0.86},
        {'B' :0.83},
        {'B-':0.80},
        {'C+':0.76},
        {'C' :0.73},
        {'C-':0.70},
        {'D+':0.66},
        {'D' :0.63},
        {'D-':0.60},
        {'F' :0.00},
    ],'weights':weights,'drops':drops,'includes':inc,'excludes':exc}

weekdays = ('Mon','Tue','Wed','Thu','Fri','Sat','Sun')

def calendar(data,l001={},l002={},l003={},l1111={}):
    oneday = timedelta(1)
    things = {}
    breaks = [
        (date.min, data['Special Dates']['Courses begin']-oneday), 
        (data['Special Dates']['Courses end']+oneday, date.max), 
    ]
    for k,v in data['Special Dates'].items():
        if 'recess' in k or 'break' in k or 'Reading' in k:
            if type(v) is dict: breaks.append((v['start'], v['end']))
            else: breaks.append((v, v))
        else:
            things.setdefault(v, []).append(k)
    for k,v in data['assignments'].items():
        if k.startswith('.'): continue
        if v is None or 'due' not in v: continue
        d = v['due']
        if isinstance(d, datetime): d = d.date()
        things.setdefault(d, []).append(k)
    d = min(things.keys())
    end = max(things.keys())
    weeks = [[]]
    classidx = 0
    while d <= end:
        wd = weekdays[d.weekday()]
        if wd == 'Sun': weeks.append([])
        noclass = any(a <= d <= b for a,b in breaks)
        if d in things or ((not noclass) and wd in ('Mon','Wed','Fri')):
            today = {'day':wd, 'date':d}
            if any('xam' in _ for _ in things.get(d,[])):
                today['1110'] = today['1111'] = 'exam'
            else:
                if (not noclass) and wd in ('Mon','Wed'): 
                    d1 = data['classes'][classidx] if classidx < len(data['classes']) else ''
                    d2 = data['classes'][classidx+1] if classidx +1 < len(data['classes']) else ''
                    r = data['reading'].get(d1, [])[:]
                    if d2 != d1: r.extend(data['reading'].get(d2, []))
                    today['1111'] = d1 + (' <span class="and">and</span> ' + d2 if d2 != d1 else '') + ('<span class="reading">' + ', '.join(r)+'</span>' if r else '')
                    if d in l1111:
                        links = []
                        for k,v in l1111[d].items():
                            if k != 'files':
                                links.append('['+k+']('+v+')')
                        links.extend('['+os.path.basename(_)+']('+_+')' for _ in l1111[d].get('files',[]))
                        today['1111'] += ' <span class="links l1111">'+', '.join(links)+'</span>'
                if (not noclass) and wd in ('Mon','Wed','Fri'): 
                    d1 = data['classes'][classidx] if classidx < len(data['classes']) else ''
                    r = data['reading'].get(d1, [])
                    classidx += 1
                    today['1110'] = d1 + ('<span class="reading">' + ', '.join(r)+'</span>' if r else '')
                    for dic,nam in (l001,'l001'), (l002,'l002'), (l003,'l003'):
                        if d in dic:
                            links = []
                            for k,v in dic[d].items():
                                if k != 'files':
                                    links.append('['+k+']('+v+')')
                            links.extend('['+os.path.basename(_)+']('+_+')' for _ in dic[d].get('files',[]))
                            today['1110'] += ' <span class="links '+nam+'">'+', '.join(links)+'</span>'
                if (not noclass) and wd == 'Thu': 
                    today['1110'] = 'lab'
            if noclass:
                today['break'] = True
            for k in things.get(d,[]):
                if k in data['assignments']:
                    name = numgap.sub(r'\1 \2', k)
                    if 'title' in data['assignments'][k]:
                        name = '<a href="'+k.lower()+'-'+data['assignments'][k]['title']+'.html">' + name + ' ' + data['assignments'][k]['title']+'</a>'
                    elif k.startswith('PA') and type(data['assignments'][k].get('files',None)) is str:
                        name = '<a href="'+ k.lower()+'-'+data['assignments'][k]['files'][:-3]+'.html">' + name + ' '+data['assignments'][k]['files'][:-3]+'</a>'
                    today.setdefault('due', []).append(name)
                else:
                    today.setdefault('other', []).append(k)
            weeks[-1].append(today)
        d += oneday
    return weeks

def mdinline(txt):
    html = markdown.markdown(codeclass.sub('', txt))
    if html.count('<p>') == 1:
        html = html[3:-4]
    return html
    
def divify(weeks):
    ans = '<div id="schedule" class="agenda">'
    for w in weeks:
        ans += '<div class="week">\n'
        for d in w:
            ans += '<div class="day ' + d['day']
            if d.get('break',False): ans += ' break'
            if d.get('1110',None) == 'exam': ans += ' exam'
            # if d['day'] in ('Thu','Fri') and 'other' not in d and '1111' not in d and all('Lab' in _ for _ in d.get('due',[])):
            #     ans += ' cs1110'
            ans += '"><span class="date">' + d['date'].strftime('%d %b').lstrip('0') + '</span>'
            if 'other' in d:
                ans += '<div class="other">' + '</div><div class="other">'.join(d['other'])+'</div>'
            if '1110' in d: ans += '<div class="cs1110">'+mdinline(d['1110'])+'</div>'
            if '1111' in d: ans += '<div class="cs1111">'+mdinline(d['1111'])+'</div>'
            if 'due' in d:
                ans += '<div class="due">'
                for e in d['due']:
                    ans += ' <span'
                    if 'PA ' in e: ans += ' class="pa"'
                    elif 'Lab ' in e: ans += ' class="lab"'
                    ans += '>' + e + '</span>'
                ans += '</div>'
            ans += '</div>'
        ans += '\n</div>\n'
    return ans + '</div>'

################################################################################
###                            Run as a program                              ###
################################################################################

if __name__ == '__main__':
    fixworking()
    import os.path

    with open('markdown/cal.yaml') as stream:
        data = load(stream, Loader=Loader)

    l001, l002, l003, l1111 = {}, {}, {}, {}    
    try:
        with open('links-001.yaml') as stream:
            l001 = load(stream, Loader=Loader)
        if l001 is None: l001 = {}
    except: pass
    try:
        with open('links-002.yaml') as stream:
            l002 = load(stream, Loader=Loader)
        if l002 is None: l002 = {}
    except: pass
    try:
        with open('links-003.yaml') as stream:
            l003 = load(stream, Loader=Loader)
        if l003 is None: l003 = {}
    except: pass
    try:
        with open('links-1111.yaml') as stream:
            l1111 = load(stream, Loader=Loader)
        if l1111 is None: l1111 = {}
    except: pass
    print(l001, l002, l003, l1111)
    
        
    with open('assignments.json', 'w') as f:
        f.write(prettyjson(assignments_json(data)))
    with open('coursegrade.json', 'w') as f:
        f.write(prettyjson(coursegrade_json(data), maxinline=16))
    
    with open('markdown/schedule.html', 'w') as f:
        f.write("""﻿<style>
    body { font-family: sans-serif; }
    .day a { text-decoration: none; background: rgba(255,127,0,0.125); padding:0ex 0.5ex; border-radius:0.5ex; color: inherit; border: 0.125ex solid rgba(255,127,0,0.25); }
    .due:before { content: "Due: "; font-size: 70.7%; opacity: 0.707;  }
    .other { background: #ffddbb; text-align: center; }
    .exam > .other { background: #ffbb77; text-align: center; }
    .day div.cs1110:before { content: "CS 1110: "; font-size: 70.7%; opacity: 0.707; }
    .day div.cs1111:before { content: "CS 1111: "; font-size: 70.7%; opacity: 0.707; }
    
    .hide, .calendar div.day.hide { display:none; }
    span.and { font-size:70.7%; }
    
    #schedule.calendar { border: 0.5ex solid #dddddd; border-radius:1ex; background-color: #dddddd; }
    .calendar div.day { background-color: white; }
    .calendar div.week, .calendar div.day { vertical-align:top; min-height:1em; }
    .calendar div.day { display:inline-block; width:calc(20% - 2ex); border-radius:1ex; padding:0.5ex; border: solid #dddddd 0.5ex; }
    .calendar div.day.past { opacity:0.7071; }
    .calendar div.day.current { border-color: #ffbb77; background: #fff7f0; }
    .calendar .Tue:first-child { margin-left: 20%; }
    .calendar .Wed:first-child { margin-left: 40%; }
    .calendar .Thu:first-child { margin-left: 60%; }
    .calendar .Fri:first-child { margin-left: 80%; }
    .calendar .Wed + .Fri, .calendar .Tue + .Thu, .calendar .Mon + .Wed { margin-left: 20%; }
    .calendar .day.hide + .day { margin-left: 20%; }
    .calendar .day.Mon.hide + .day.Wed { margin-left: 40%; }
    .calendar .day.hide + .day.hide + .day { margin-left: 40%; }
    /* .calendar div.due { background-color:#ffeedd; } */
    .calendar span.date { float:right; padding: 0ex 0ex 0.5ex 1ex; opacity:0.5; font-size: 70.7%; margin-top: -1.41ex; }
    .calendar .other { margin: -0.5ex -0.5ex 0.25ex -0.5ex; border-radius: 0.5ex 0.5ex 0ex 0ex; }
    .calendar .reading:before { content: "Reading: "; font-size:70.7%; opacity: 0.707; }
    .calendar .reading:not(.hide) { display: block; }
   
    .l001:before { content: "001 files: "; font-size:70.7%; opacity: 0.707; }
    .l002:before { content: "002 files: "; font-size:70.7%; opacity: 0.707; }
    .l003:before { content: "003 files: "; font-size:70.7%; opacity: 0.707; }
    .l1111:before { content: "1111 files: "; font-size:70.7%; opacity: 0.707; }
    .links:not(.hide) { display: block; }

    .calendar div.week { display:flex; flex-direction: row; align-items: flex-stretch; }
    .calendar div.week div.day { flex-grow: 0; flex-shrink: 1; flex-basis: auto; }
    
    
    .agenda div.week { border-top: thick solid #dddddd; min-height: 3em; background:#eeeeee; }
    .agenda .day + .day { border-top: thin dotted #777777; }
    .agenda .day { padding: 0.5ex 0ex; background: white; min-height:1.5em; }
    .agenda div.day.past { opacity:0.7071; }
    .agenda div.day.current { border: 0.25ex solid #ffbb77; padding:0.5ex; border-radius:1ex; background: #fff7f0; }
    .agenda span.date { float:left; opacity:0.5; }
    .agenda .Sun span.date:before { content: "Sun "; }
    .agenda .Mon span.date:before { content: "Mon "; }
    .agenda .Tue span.date:before { content: "Tue "; }
    .agenda .Wed span.date:before { content: "Wed "; }
    .agenda .Thu span.date:before { content: "Thu "; }
    .agenda .Fri span.date:before { content: "Fri "; }
    .agenda .Sat span.date:before { content: "Sat "; }
    .agenda .day div:not(.other) { clear:left; }
    .agenda .reading:before { content: "; see " }
    
.agenda .other { margin-top: -0.5ex; padding-bottom: 0.25ex; }
.agenda .current .other { margin: -0.5ex -0.5ex 0.25ex -0.5ex; }
    
    /* .agenda .day:nth-of-type(2n+1) { background-color: #f7f7f7; } */
</style>
<input type="button" id="tog.cs1110" value="hide 1110" onclick="toggleClass('.cs1110')"/>
<input type="button" id="tog.cs1111" value="hide 1111" onclick="toggleClass('.cs1111')"/>
<input type="button" id="tog.reading" value="hide Reading" onclick="toggleClass('.reading,.links');"/>
<input type="button" id="tog.due" value="hide Assignments" onclick="toggleClass('.due')"/>
<span style="width:2em; display:inline-block;">&nbsp;</span>
<input type="button" id="asAgenda" value="agenda view" onclick="document.getElementById('schedule').setAttribute('class','agenda');"/>
<input type="button" id="asCalendar" value="calendar view" onclick="document.getElementById('schedule').setAttribute('class','calendar')"/>
""")
        f.write(divify(calendar(data, l001, l002, l003, l1111)))
        f.write("""<script>//<!--
var days = document.querySelectorAll('.day');
for(var i=0; i<days.length; i+=1) {
    var date = new Date(days[i].querySelector('.date').innerText + ' """+str(data['Special Dates']['Courses end'].year)+""" 23:59');
    if (date < new Date()) days[i].classList.add('past');
    else { days[i].classList.add('current'); break; }
}
function showClass(cls) {
    var elem = document.querySelectorAll(cls);
    for(var i=0; i<elem.length; i+=1) elem[i].classList.remove('hide');
}
function hideClass(cls) {
    var elem = document.querySelectorAll(cls);
    for(var i=0; i<elem.length; i+=1) elem[i].classList.add('hide');
}
function toggleClass(cls) {
    var remove = false;
    var elem = document.querySelectorAll(cls);
    for(var i=0; i<elem.length; i+=1) 
        if (remove = elem[i].classList.contains('hide')) elem[i].classList.remove('hide');
        else elem[i].classList.add('hide');
        
    var elem = document.querySelectorAll('div.day');
    for(var i=0; i<elem.length; i+=1) {
        var keep = false;
        for(var j=1; j<elem[i].children.length; j+=1)
            keep |= !elem[i].children[j].classList.contains('hide');
        if (keep) elem[i].classList.remove('hide')
        else elem[i].classList.add('hide');
    }
    
    var button = document.getElementById('tog'+cls);
    var end = button.value.substr(5);
    if (!remove) button.value = 'show ' + end;
    else button.value = 'hide ' + end;
}
document.getElementById('asAgenda').click();
//--></script>""")
