#!/usr/bin/env python
import requests
import sys
from peyotl.utility import get_test_config
curator_domain = get_test_config().get_config_setting('apis', 'curator', default='http://devtree.opentreeoflife.org')
print curator_domain
data = {'content': '(a,b);',
        'output': 'nexson',
        'inputFormat': 'newick',
        'nexml2json': '0.0',
        }
url = '{}/curator/default/to_nexson'.format(curator_domain)
r = requests.put(url, params=data)
print r.json()

