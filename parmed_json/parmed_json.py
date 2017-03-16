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


def main():
    gmx = pmd.load_file('test.top', xyz='test.gro')
    print(json.dumps(gmx, cls=ParmedEncoder, indent=2))

if __name__ == '__main__':
    main()