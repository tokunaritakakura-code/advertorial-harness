import sys,re,html
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s):
        super().__init__();s.out=[];s.tag=None;s.skip=0
    def handle_starttag(s,t,a):
        if t in('script','style','noscript','svg'):s.skip+=1
        if t in('h1','h2','h3','h4','p','li','button'):s.tag=t
    def handle_endtag(s,t):
        if t in('script','style','noscript','svg'):s.skip-=1
        if t==s.tag:s.tag=None
    def handle_data(s,d):
        d=d.strip()
        if s.skip or not d or not s.tag:return
        s.out.append((s.tag,d))
p=P();p.feed(open(sys.argv[1],errors='ignore').read())
seen=set();n=0
for t,d in p.out:
    if d in seen:continue
    seen.add(d)
    if t in('h1','h2','h3'):print(f'[{t}] {d[:160]}')
    elif n<int(sys.argv[2]) and len(d)>25:print('   '+d[:180]);n+=1
