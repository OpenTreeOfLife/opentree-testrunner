#!/usr/bin/env python
import sys
from peyotl.utility import get_test_config
from peyotl.api import APIWrapper
names = ['Pan trodlogytes', 'Homo sapphire', 'Plantago', 'Morpho peleides', 'Eleocharis',]

def test_v2_tnrs_no_fuzzy():
    cfg = get_test_config()
    taxo = APIWrapper(config=cfg).taxomachine
    resp = taxo.TNRS(names, context_name="All life", fuzzy_matching=False)
    print resp
    assert len(resp['matched_name_ids']) == 3
    assert 'Homo sapphire' in resp['unmatched_name_ids'] 
    assert 'Pan trodlogytes' in resp['unmatched_name_ids'] 

def test_v2_tnrs_fuzzy():
    cfg = get_test_config()
    taxo = APIWrapper(config=cfg).taxomachine
    names = ['Pan trodlogytes', 'Homo sapphire', 'Plantago', 'Morpho peleides', 'Eleocharis',]
    resp = taxo.TNRS(names, context_name="All life", fuzzy_matching=True)
    print resp
    assert len(resp['matched_name_ids']) == 4
    assert resp['unmatched_name_ids'] == [u'Homo sapphire']

def test_v1_tnrs():
    cfg = get_test_config({'apis': {'api_version': '1'}})
    taxo = APIWrapper(config=cfg).taxomachine
    names = ['Pan trodlogytes', 'Homo sapphire', 'Plantago', 'Morpho peleides', 'Eleocharis',]
    resp = taxo.TNRS(names, context_name="All life")
    assert len(resp['matched_name_ids']) == 4
    assert resp['unmatched_name_ids'] == [u'Homo sapphire']