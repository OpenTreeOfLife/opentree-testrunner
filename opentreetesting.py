#!/usr/bin/env python
import os, sys, json
from peyotl.utility import ConfigWrapper, create_overrides_from_config
from ConfigParser import SafeConfigParser
import gzip
from cStringIO import StringIO

def config(overrides=None):
    '''Returns a config object with the settings in test.conf overriding
    the peyotl configuration, and the settings in the `overrides` dict
    having the highest priority.
    '''
    _CONFIG_FN = os.path.abspath('test.conf')
    _CONFIG = SafeConfigParser()
    _CONFIG.read(_CONFIG_FN)
    d = create_overrides_from_config(_CONFIG, _CONFIG_FN)
    if overrides is not None:
        d.update(overrides)
    return ConfigWrapper(None, overrides=d)

def summarize_json_response(resp):
    sys.stderr.write('Sent request to %s\n' %(resp.url))
    resp.raise_for_status()
    try:
        results = resp.json()
    except:
        print 'Non json resp is:', resp.text
        return False
    if isinstance(results, unicode) or isinstance(results, str):
        print results
        er = json.loads(results)
        print er
        print json.dumps(er, sort_keys=True, indent=4)
        sys.stderr.write('Getting JavaScript string. Object expected.\n')
        return False
    print json.dumps(results, sort_keys=True, indent=4)
    return True

def summarize_gzipped_json_response(resp):
    sys.stderr.write('Sent request to %s\n' %(resp.url))
    resp.raise_for_status()
    try:
        uncompressed = gzip.GzipFile(mode='rb', fileobj=StringIO(resp.content)).read()
        results = uncompressed
    except:
        raise 
    if isinstance(results, unicode) or isinstance(results, str):
        er = json.loads(results)
        print json.dumps(er, sort_keys=True, indent=4)
        return True
    else:
        print 'Non gzipped response, but not a string is:', results
        return False
