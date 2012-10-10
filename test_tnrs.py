#!/usr/bin/env python
#curl -X POST http://opentree-dev.bio.ku.edu:7474/db/data/ext/TNRS/graphdb/doTNRSForNames -H "Content-Type: Application/json" -d '{"queryString":"Pan trodlogytes, Homo sapphire, Plantago, Morpho peleides, Eleocharis"}'
from opentreetesting import config
host = config('host', 'tnrshost')
print host
