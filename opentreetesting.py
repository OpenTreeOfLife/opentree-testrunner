#!/usr/bin/env python
import os, sys, json
from ConfigParser import SafeConfigParser

_CONFIG = None
_CONFIG_FN = None
def config(section=None, param=None):
    '''
    Returns the config object if `section` and `param` are None, or the 
        value for the requested parameter.
    
    If the parameter (or the section) is missing, the exception is logged and
        None is returned.
    '''
    global _CONFIG, _CONFIG_FN
    if _CONFIG is None:
        _CONFIG_FN = os.path.abspath('test.conf')
        _CONFIG = SafeConfigParser()
        _CONFIG.read(_CONFIG_FN)
    if section is None and param is None:
        return _CONFIG
    try:
        v = _CONFIG.get(section, param)
        return v
    except:
        sys.stderr.write('Config file "%s" does not contain option "%s in section "%s"\n' % (_CONFIG_FN, param, section))
        return None

def summarize_json_response(resp):
    sys.stderr.write('Sent POST to %s\n' %(resp.url))
    resp.raise_for_status()
    try:
        results = resp.json()
    except:
        print 'Non json resp is:', resp.text
        return False
    if isinstance(results, unicode) or isinstance(results, str):
        print "repr(res.json)=>  %s" % repr(results)
        er = eval(results)
        print type(er)
        print json.dumps(er, sort_keys=True, indent=4)
        sys.stderr.write('Getting JavaScript string. Object expected.\n')
        return False
    print json.dumps(results, sort_keys=True, indent=4)
    return True
