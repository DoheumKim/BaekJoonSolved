import sys,re

db = {'F':'Foundation',
      'C':'Claves',
      'V':'Veritas',
      'E':'Exploration'}
txt = sys.stdin.readline().strip()
p = re.compile('[F,C,V,E]\\d\\d[.]\\d\\d\\dL?')
out = p.match(txt)
if out:print(db[txt[0]])