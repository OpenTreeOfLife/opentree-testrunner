#!/usr/bin/env python
import sys
import requests
import json
from opentreetesting import config, summarize_json_response
DOMAIN = config('host', 'golshost')
p = '/ext/GoLS/graphdb/getStudyIngestMessagesForNexSON'
if DOMAIN.startswith('http://127.0.0.1'):
    p = '/db/data' + p
SUBMIT_URI = DOMAIN + p
payload = {
    'nexsonBlob': open('data/359', 'rU').read()
}

headers = {
    'content-type' : 'application/json',
    'accept' : 'application/json',
}
d = json.dumps(payload)
resp = requests.post(SUBMIT_URI,
                     headers=headers,
                     data=d,
                     allow_redirects=True)
summarize_json_response(resp) or sys.exit(1)