from itertools import chain

from fabric.api import env
from fabric import api as fab

from hepfab.util import genrange
from hepfab.commands import *

env.shell = "/bin/sh -c"

# Compute nodes.
computenodes = dict(
    g4  = genrange("g4", 20),
    g5  = genrange("g5", 20),
    g6  = genrange("g6", 20),
    g7  = genrange("g7", 27),
    g8  = genrange("g8", 6),
    g9  = genrange("g9", 45),
    g10 = genrange("g10", 24),
    g12 = genrange("g12", 32),
    g14 = genrange("g14", 32),
    g16 = genrange("g16", 57),
    g18 = genrange("g18", 32),
    g19 = genrange("g19", 32),
)

storagenodes = dict(
    s5  = genrange("s5", 9),
    s15 = genrange("s15", 10),
    s17 = genrange("s17", 10),
)

servers = dict(
    afs = ["anise", "rosemary"],
    web = ["web"],
    mail = ["mail"],
    cfengine = ["ginseng", "anise"],
)

groups = dict(
    computenodes = computenodes,
    storagenodes = storagenodes,
    servers = servers,
)

env.roledefs.update(dict(
    nodes =         chain(*(storagenodes.values() + computenodes.values())),
))

for name, group in groups.items():
    env.roledefs[name] = chain(*group.values())

del(chain, genrange)
