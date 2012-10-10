#!/usr/bin/env python
import os, sys
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
