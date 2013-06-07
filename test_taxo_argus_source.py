#!/usr/bin/env python
import sys
import requests
import json
#curl -X POST http://opentree-dev.bio.ku.edu:7474/ext/TNRS/graphdb/doTNRSForNames -H "Content-Type: Application/json" -d '{"queryString": "Pan trodlogytes, Homo sapphire, Plantago, Morpho peleides, Eleocharis"}'
from opentreetesting import config, summarize_json_response
DOMAIN = config('host', 'tnrshost')
prefix = DOMAIN + "/ext/GetJsons/node/";
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
summarize_json_response(resp) or sys.exit(1)