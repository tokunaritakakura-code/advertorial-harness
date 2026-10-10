#!/bin/bash
# usage: fx.sh ID [ID...]  -> author likes text (and article text if any)
for id in "$@"; do curl -s "https://api.fxtwitter.com/status/$id" | python3 -I -c "
import sys,json
d=json.load(sys.stdin).get('tweet',{})
print('@'+d.get('author',{}).get('screen_name',''),d.get('likes'),'|',d.get('text','')[:2500])
a=d.get('article')
if a:
  print('ARTICLE:',a.get('title'))
  bl=a.get('content',{}).get('blocks',[])
  print('\n'.join(b.get('text','') for b in bl)[:8000])
"; echo ---; done
