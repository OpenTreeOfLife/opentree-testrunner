#!/bin/sh
echo skipping 'cat data/doi_list.txt | python test_phylografter_doi.py'
echo skipping 'cat data/bad/doi_list.txt | python test_phylografter_doi.py 0'
python test_phylografter_export_nexson.py 2500