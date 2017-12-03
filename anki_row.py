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
    try:
        annotations, fields = read_annotations(path, slc=config["slc"])
    except Exception as err:
        print_err("problem with " + path)
        raise err

    base_path = path.replace("examples/", "")
    base_path = base_path[0:base_path.rfind("/")]

    card = {"example" : path.replace("examples/", "")}
    for field in ["description", "pre", "step", "post", "explanation"]:
        val = ""
        if field in fields:
            val = fields[field]["value"]
        val = val.replace("\n", "<br/>").replace("\t", "&#9;")
        card[field] = val

    if card["description"] == "":
        print_err("error: " + path + " has no description")
        return None

    card["description"] = base_path + ": " + card["description"]
    return card


def config_for_example(path):
    """determines which configuration to use for an example"""

    config = None
    dirs = ["build_config"] + path.split("/")[1:-1]
    # look for config in build_config/..., starting with most specific path
    for j in range(len(dirs),1,-1):
        # try to load config
        conf_path = ".".join(dirs[0:j])
        try:
            config = import_from(conf_path, "config")
            break
        except ModuleNotFoundError:
            pass

    if not config:
        raise FileNotFoundError("no config found for " + path)

    return config

if __name__ == '__main__':
    arguments = docopt(__doc__, version='read_annotations')

    description_to_card = {}
    description_to_path = {}
    for path in arguments["<file>"]:
        config = config_for_example(path)
        card = anki_row(path,config)
        if card:
            desc = card["description"]
            if desc in description_to_path:
                print_err("duplicate description: '" + desc + "'")
                print_err("   in path " + description_to_path[desc])
                print_err("   and     " + path)
                del(description_to_card[desc])
                continue

            description_to_card[desc] = card
            description_to_path[desc] = path

    for d in description_to_card:
        card = description_to_card[d]
        fields = ["example", "description", "pre", "step", "post", "explanation"]
        print("\t".join([str(card.get(f, "")) for f in fields]))


