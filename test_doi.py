#!/usr/bin/env python
import sys
import requests
import xml.etree.ElementTree as ET

DOMAIN = 'http://www.crossref.org'
SUBMIT_URI = DOMAIN + '/openurl'
doi = sys.argv[1]
if not doi.startswith('doi'):
    doi = 'doi:' + doi
payload = {
    "pid" : ENTER_YOUR_CROSSREF_REGISTERED_EMAIL_HERE,
    "id" : doi,
    "noredirect" : "true",
    "format" : "unixref"
}
headers = {
    'content-type' : 'application/json',
    'accept' : 'application/json',
    }
resp = requests.get(SUBMIT_URI,
                    params=payload,
                    allow_redirects=False)
sys.stderr.write('Sent GET to %s\n' %(resp.url))
resp.raise_for_status()
root = ET.fromstring(resp.text)
sys.stdout.write('%s\n' % resp.text)
