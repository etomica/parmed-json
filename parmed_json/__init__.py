import json
import argparse
from parmed_json import parmed_json
import parmed

from parmed_json.parmed_json import ParmedEncoder


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--type")
    parser.add_argument("file")
    parser.add_argument("secondary_file", nargs="?")
    args = parser.parse_args()

    if args.type == "gromacs":
        struct = parmed.load_file(args.file, xyz=args.secondary_file)
        print(json.dumps(struct, cls=ParmedEncoder, skipkeys=True))
    else:
        struct = parmed.load_file(args.file, args.secondary_file)
        print(json.dumps(struct, cls=ParmedEncoder, skipkeys=True))

