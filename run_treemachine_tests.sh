#!/bin/sh
set -x
python test_gols_tree_ids.py
python test_gols_get_id_of_draft.py
python test_gols_get_source_newick.py
python test_gols_get_source_arguson.py
