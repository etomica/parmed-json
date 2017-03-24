from sys import argv
from parmed_json import parmed_json


def main():
	if len(argv) == 3:
		parmed_json.parse_file(argv[1], argv[2])
	elif len(argv) == 2:
		parmed_json.parse_file(argv[1])
