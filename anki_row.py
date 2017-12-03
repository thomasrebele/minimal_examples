#!/usr/bin/env python3

"""anki_row

Usage:
  anki_row.py [options] <file>...

Options:
  -h --help                     Show this screen.

"""

from docopt import docopt
from html import escape
from sys import stderr

from minimal_examples_common.read_annotations import *

# TODO:
no_hierarchy=False

# https://stackoverflow.com/a/20830343/1562506
def print_err(*args, **kwargs):
    print(*args, file=stderr, **kwargs)

# https://stackoverflow.com/a/8790077/1562506
def import_from(module, name):
    """import a function/attribute from a python script"""
    module = __import__(module, fromlist=[name])
    return getattr(module, name)

def anki_row(path, config):
    """create a flashcard for anki in TSV format.
    path: the example file (e.g. examples/rust/hello_world.rs).
    config: specifies which markup tag to use """

    annotations, fields = read_annotations(path, slc=config["slc"])

    base_path = path.replace("examples/", "")
    base_path = base_path[0:base_path.rfind("/")]

    l = []
    for field in ["description", "pre", "step", "post", "explanation"]:
        val = ""
        if field in fields:
            val = fields[field]["value"]
        val = val.replace("\n", "<br/>").replace("\t", "&#9;")
        l += [val]

    if l[0] == "":
        print_err("error: " + path + " has no description")
        return None

    l[0] = base_path + ": " + l[0]
    return l



path_to_conf = {}
def config_for_example(path):
    """determines which configuration to use for an example"""
    path = path[0:path.rfind("/")]
    tag = "examples/"
    start = path.find(tag) + len(tag)
    path = "build_config." + path[start:]
    path.replace("/",".")

    if not path in path_to_conf:
        path_to_conf[path] = import_from(path, "config")
    return path_to_conf[path]

if __name__ == '__main__':
    arguments = docopt(__doc__, version='read_annotations')

    desc_idx = 0
    description_to_card = {}
    description_to_path = {}
    for path in arguments["<file>"]:
        config = config_for_example(path)
        row = anki_row(path,config)
        if row:
            desc = row[desc_idx]
            if desc in description_to_path:
                print_err("duplicate description: '" + desc + "'")
                print_err("   in path " + description_to_path[desc])
                print_err("   and     " + path)
                del(description_to_card[desc])
                continue

            description_to_card[desc] = row
            description_to_path[desc] = path

    for d in description_to_card:
        print("\t".join([str(f) for f in description_to_card[d]]))


