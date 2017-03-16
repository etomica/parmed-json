from sys import argv
from parmed_json import parmed_json


def main():
    parmed_json.parse_gromacs(argv[1], argv[2])