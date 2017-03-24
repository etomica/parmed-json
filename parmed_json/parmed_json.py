import json

import parmed as pmd
import numpy as np


class ParmedEncoder(json.JSONEncoder):

    def default(self, o):
        if hasattr(o, '__getstate__'):
            if(isinstance(o, pmd.Structure)):
                d = o.__getstate__()
                # d['atoms'] = o.atomss
                return d
            return o.__getstate__()
        elif isinstance(o, np.ndarray):
            return o.tolist()
        elif o.__class__.__module__.startswith('parmed'):
            return o.__dict__
        else:
            return json.JSONEncoder().default(o)


def parse_file(topology_file, position_file=None):
    if position_file:
        struct = pmd.load_file(topology_file, xyz=position_file)
    else:
        struct = pmd.load_file(topology_file)

    print(json.dumps(struct, cls=ParmedEncoder))