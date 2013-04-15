#!/bin/sh
python test_tnrs.py 'Pan trolodytes'
python test_gols_tree_ids.py
python test_gols_get_source_newick.py
python test_taxo_argus_source.py
cat data/doi_list.txt | python test_phylografter_doi.py
cat data/bad/doi_list.txt | python test_phylografter_doi.py 0
