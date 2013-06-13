#!/usr/bin/env python
import sys
import requests
import json
from opentreetesting import config, summarize_json_response
DOMAIN = config('host', 'golshost')
SUBMIT_URI = DOMAIN + '/ext/GoLS/graphdb/getDraftTreeID'
payload = {}
headers = {
    'content-type' : 'application/json',
    'accept' : 'application/json',
}
resp = requests.post(SUBMIT_URI,
                     headers=headers,
                     data=json.dumps(payload),
                     allow_redirects=True)
summarize_json_response(resp) or sys.exit(1)