#!/usr/bin/env python
'''
Test of code for looking up bibliographic info from DOI.

Coded based on guidelines in http://crosscite.org/cn/
using the requests package for python

'''
import sys
import requests
RETURNS_OBJECT = False
if RETURNS_OBJECT:
    import json

def normalize_doi_for_url(raw):
    '''Take a DOI which may start with doi or doi: and return the DOI needed
    for URL construction.
    '''
    if raw.startswith('doi:'):
        raw = raw[4:]
    elif raw.startswith('doi'):
        raw = raw[3:]
    return raw


DOMAIN = 'http://dx.doi.org'

doi = normalize_doi_for_url(sys.argv[1])

SUBMIT_URI = DOMAIN + '/' + doi

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
resp = requests.get(SUBMIT_URI,
                    params=payload,
                    headers=headers,
                    allow_redirects=True)
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
resp.raise_for_status()
if RETURNS_OBJECT:
    results = resp.json
    print json.dumps(results, sort_keys=True, indent=4)
else:
    print resp.text
