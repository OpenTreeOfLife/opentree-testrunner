#!/usr/bin/env python
import sys
import requests
import json
#curl -X POST http://opentree-dev.bio.ku.edu:7474/db/data/ext/TNRS/graphdb/doTNRSForNames -H "Content-Type: Application/json" -d '{"queryString": "Pan trodlogytes, Homo sapphire, Plantago, Morpho peleides, Eleocharis"}'
from opentreetesting import config
DOMAIN = config('host', 'tnrshost')
prefix = DOMAIN + "/db/data/ext/GetJsons/node/";
suffix = "/getConflictTaxJsonAltRel";
# @TEMP assuming ottol
if len(sys.argv) == 1:
    nodeID = '805080'
else:
    nodeID = sys.argv[1]
SUBMIT_URI = prefix + nodeID + suffix
ds = "ottol"
payload = {
    "domSource": ds
}
if len(sys.argv) > 1:
    payload['queryString'] = ', '.join(sys.argv[1:])

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
    #print 'results =', str(results)
except:
    print 'Non json resp is:', resp.text
    sys.exit(1)
if isinstance(results, unicode) or isinstance(results, str):
    print "repr(res.json)=>  %s" % repr(results)
    er = eval(results)
    print type(er)
    print json.dumps(er, sort_keys=True, indent=4)
    sys.exit('Getting JavaScript string. Object expected.')
else:
    print json.dumps(results, sort_keys=True, indent=4)
