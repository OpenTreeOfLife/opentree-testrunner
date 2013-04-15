#!/usr/bin/env python
'''
Test of code for looking up bibliographic info from DOI.

Coded based on guidelines in http://crosscite.org/cn/
using the requests package for python

'''
import sys
import requests
import json
from opentreetesting import config, summarize_json_response
try:
    should_fail = (sys.argv[1] == '0')
except:
    should_fail = False
DOMAIN = config('host', 'phylografterapp')
for doi in sys.stdin:
    SUBMIT_URI = DOMAIN + '/study/ref_from_doi/' + doi.strip() + '.json'
    print 'Looking up "%s" at  %s ' % (doi.strip(),SUBMIT_URI)
    try:
        resp = requests.get(SUBMIT_URI)
        resp.raise_for_status()
        print json.dumps(resp.json, sort_keys=True, indent=4)
    except Exception as x:
        print x
        if not should_fail:
            sys.exit(1)
    else:
        if should_fail:
            sys.exit('DOI expected to fail, but did not\n')
    

'''


payload = {
}
headers = {
    }
if RETURNS_OBJECT:
    headers['content-type'] = 'application/json'
    headers['Accept'] = 'application/vnd.citationstyles.csl+json, application/rdf+json'
    requested_formats = "JSON citeproc or RDF"
else:
    headers['content-type'] = 'application/tex'
    headers['Accept'] = 'text/x-bibliography; style=apa'
    requested_formats = "Bibliographic citation (text; style=APA)"

sys.stderr.write('Sending GET to "%s"\n' % (SUBMIT_URI))
sys.stderr.write('Sent GET to %s\n' %(resp.url))
if resp.status_code == 404:
    sys.stderr.write('Requested DOI, "%s", does not exist\n' % doi)
    sys.exit(1)
if resp.status_code == 406:
    sys.stderr.write('DOI found, but unavailable in the requested format(s): %s\n' % requested_formats)
    sys.exit(2)
if resp.status_code == 204:
    sys.stderr.write('DOI found, but no bibliographic information was available')
    sys.exit(3)
summarize_json_response(resp) or sys.exit(1)
'''
