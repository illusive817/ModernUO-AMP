#!/usr/bin/env python3
from pathlib import Path
import json, re
p=Path(__file__).resolve().parent
errors=[]
for n in ('manifest.json','modernuoconfig.json','modernuometaconfig.json','modernuoports.json'):
 try: json.loads((p/n).read_text())
 except Exception as ex:errors.append(f'{n}: {ex}')
kvp=(p/'modernuo.kvp').read_text()
settings={}
for line in kvp.splitlines():
 if line and not line.startswith('#'):
  if '=' not in line: errors.append(f'bad KVP line: {line}')
  else:
   k,v=line.split('=',1)
   if k in settings:errors.append(f'duplicate KVP key {k}')
   settings[k]=v
for k in ('Meta.AppConfigId','Meta.ConfigManifest','Meta.MetaConfigManifest','Meta.ConfigRoot','App.Ports','App.UpdateSources'):
 if k not in settings:errors.append('missing '+k)
for k,v in settings.items():
 for filename in re.findall(r'@IncludeJson\[([^]]+)\]',v):
  if not (p/filename).is_file():errors.append(f'{k}: missing include {filename}')
try:
 m=json.loads((p/'manifest.json').read_text())
 for k in ('id','origin','url','prefix','repotype'):
  if not m.get(k):errors.append('manifest missing '+k)
except Exception:pass
print('PASS: local file/JSON/KVP basic checks (not an AMP runtime test)' if not errors else '\n'.join('ERROR: '+s for s in errors))
raise SystemExit(bool(errors))
