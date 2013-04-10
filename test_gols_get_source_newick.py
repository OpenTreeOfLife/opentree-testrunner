#!/usr/bin/env python
import sys
import requests
import json
from opentreetesting import config
DOMAIN = config('host', 'golshost')



SUBMIT_URI = DOMAIN + '/db/data/ext/GoLS/graphdb/getSourceTreeNewick'
payload = {'souretreeid': 'WangEtAl2009-studyid-15'
}
if len(sys.argv) > 1:
    payload['souretreeid'] = sys.argv[1:]
headers = {
    'content-type' : 'application/json',
    'accept' : 'application/json',
}
resp = requests.post(SUBMIT_URI,
                     headers=headers,
                     data=json.dumps(payload),
                     allow_redirects=True)
sys.stderr.write('Sent POST to %s\n' %(resp.url))
resp.raise_for_status()
try:
    results = resp.json()
    print 'results =', str(results)
except:
    print 'Non json resp is:', resp.text
    sys.exit(1)
print results