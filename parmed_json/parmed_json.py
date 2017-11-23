import json

import parmed as pmd
import numpy as np
from parmed.unit import Quantity


class ParmedEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, Quantity):
            return str(o)
        elif isinstance(o, np.ndarray):
            return o.tolist()
        elif o.__class__.__module__.startswith('parmed'):
            if hasattr(o, '__getstate__'):
                return o.__getstate__()
            return vars(o)
        else:
            return json.JSONEncoder().default(o)


def parse_file(files):
    struct = pmd.load_file(files[0], xyz=files[1])
    print(json.dumps(struct, cls=ParmedEncoder, skipkeys=True))


def parse_gromacs(topfile, grofile):
    struct = pmd.load_file(topfile, xyz=grofile)
    print(json.dumps(struct, cls=ParmedEncoder, skipkeys=True))
