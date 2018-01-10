from yaml import load
from icalendar import *
import pytz, datetime, re

link = re.compile(r'\[([^\]]*)\]\(([^\)]*)\)')
def deMd(s):
    return link.sub(r'\1 (\2)', s.replace('`', ''))

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def fixworking():
    """change to this script's directory as the working directory"""
    import os, os.path
    os.chdir(os.path.realpath(os.path.dirname(__file__)))

eastern = pytz.timezone('America/New_York')

class RealCal:
    def __init__(self, name):
        self.name = name
        self.cal = Calendar()
        self.cal.add('prodid', '-//University of Virginia//'+name+'//EN')
        self.cal.add('calscale', 'GREGORIAN')
        self.cal.add('version', '2.0')
        self.cal.add('name', name)
    def event(self, name, start, duration=None, location=None, end=None, details=None):
        e = Event()
        e.add('dtstamp', datetime.datetime.now(tz=eastern))
        e.add('uid', name+start.isoformat()[:20].rstrip('0:T-'))
        e.add('dtstart', start)
        if end is not None: e.add('dtend', end)
        elif duration is not None: e.add('dtend', start+duration)
        e.add('summary', name)
        if location is not None: e.add('location', location)
        if details is not None: e.add('description', details)
        self.cal.add_component(e)
    def __str__(self):
        return self.cal.to_ical().decode('utf-8').replace('\r\n','\n').strip()
    def bytes(self):
        return self.cal.to_ical()

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def calendar(data):
    ans = RealCal('cs1110.s2018')

    m50 = datetime.timedelta(0, 50*60)
    m75 = datetime.timedelta(0, 75*60)
    m180 = datetime.timedelta(0, 180*60)
    
    breaks = []
    exams = {}
    for k,v in data['Special Dates'].items():
        if 'recess' in k or 'break' in k or 'Reading' in k:
            if type(v) is dict: breaks.append((v['start'], v['end']))
            else: breaks.append((v, v))
        elif 'xam' in k:
            exams[v] = k

    
    oneday = datetime.timedelta(1)
    d = data['Special Dates']['Courses begin']
    classnum = 0
    while d < data['Special Dates']['Courses end']:
        if not any(d >= b[0] and d <= b[1] for b in breaks):
            if d.weekday() in (0,2,4):
                sec001 = datetime.datetime(d.year, d.month, d.day, 14, 0, 0, tzinfo=eastern)
                sec002 = datetime.datetime(d.year, d.month, d.day, 12, 0, 0, tzinfo=eastern)
                sec003 = datetime.datetime(d.year, d.month, d.day, 11, 0, 0, tzinfo=eastern)

                topic = exams.get(d, data['classes'][classnum])
                if topic in data['reading']: topic = deMd(topic) + '\r\nSee '+deMd(' and '.join(data['reading'][topic])) +' for more'
                else: topic = deMd(topic)
                if d not in exams: classnum += 1

                ans.event('1110-001', sec001, m50, location='CHM 402', details=topic)
                ans.event('1110-002', sec002, m50, location='OLS 120', details=topic)
                ans.event('1110-003', sec003, m50, location='WIL 301', details=topic)
                if d.weekday() != 4:
                    ans.event('1111', sec001, m75, location='THN E303')
            if d.weekday() == 3:
                ans.event('Lab 100', datetime.datetime(d.year, d.month, d.day, 9, 30, 0, tzinfo=eastern), m75, location='OLS 001')
                ans.event('Lab 101', datetime.datetime(d.year, d.month, d.day, 11, 0, 0, tzinfo=eastern), m75, location='OLS 001')
                ans.event('Lab 102', datetime.datetime(d.year, d.month, d.day, 12, 30, 0, tzinfo=eastern), m75, location='OLS 001')
                ans.event('Lab 103', datetime.datetime(d.year, d.month, d.day, 14, 0, 0, tzinfo=eastern), m75, location='OLS 001')
                ans.event('Lab 104', datetime.datetime(d.year, d.month, d.day, 15, 30, 0, tzinfo=eastern), m75, location='OLS 001')
                ans.event('Lab 105', datetime.datetime(d.year, d.month, d.day, 17, 0, 0, tzinfo=eastern), m75, location='OLS 001')
                ans.event('Lab 106', datetime.datetime(d.year, d.month, d.day, 18, 30, 0, tzinfo=eastern), m75, location='OLS 001')
                ans.event('Lab 107', datetime.datetime(d.year, d.month, d.day, 11, 0, 0, tzinfo=eastern), m75, location='MEC 213')
                ans.event('Lab 108', datetime.datetime(d.year, d.month, d.day, 15, 30, 0, tzinfo=eastern), m75, location='MEC 213')
                ans.event('Lab 109', datetime.datetime(d.year, d.month, d.day, 17, 0, 0, tzinfo=eastern), m75, location='MEC 213')
                ans.event('Lab 110', datetime.datetime(d.year, d.month, d.day, 18, 30, 0, tzinfo=eastern), m75, location='MEC 213')
                ans.event('Lab 111', datetime.datetime(d.year, d.month, d.day, 17, 0, 0, tzinfo=eastern), m75, location='Rice 130')
        d += oneday
    
    e3 = data['Special Dates']['Exam 3']
    ans.event('Final Exam', datetime.datetime(e3.year, e3.month, e3.day, 19, 00, 0, tzinfo=eastern), m180, location='TBA')
    
    return ans



if __name__ == '__main__':
    fixworking()
    with open('markdown/cal.yaml') as stream:
        data = load(stream, Loader=Loader)
    cal = calendar(data)
    with open('markdown/cal.ics', 'wb') as f:
        f.write(cal.bytes())
