#!/bin/sh
set -x
python test_tnrs.py 'Pan trolodytes'
python test_taxo_argus_source.py
