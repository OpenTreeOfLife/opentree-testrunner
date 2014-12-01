#!/bin/sh
set -x
nosetests test_taxon_tnrs.py
python test_taxo_argus_source.py
