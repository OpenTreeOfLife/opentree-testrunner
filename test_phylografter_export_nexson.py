#!/usr/bin/env python
'''
Test of code for looking up bibliographic info from DOI.

Coded based on guidelines in http://crosscite.org/cn/
using the requests package for python

'''
import sys
import requests
import json
from opentreetesting import config, summarize_gzipped_json_response
try:
    study_id = sys.argv[1]
except:
    study_id = '9'
headers = {
    'accept-encoding' : 'gzip',
    'content-type' : 'application/json',
    'accept' : 'application/json',
}
DOMAIN = config('host', 'phylografterapp')
SUBMIT_URI = DOMAIN + '/study/export_gzipNexSON.json/' + study_id
resp = requests.get(SUBMIT_URI,
                     headers=headers,
                     allow_redirects=True)
summarize_gzipped_json_response(resp) or sys.exit(1)