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

from read_annotations import *
from level_estimate import *

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
            val = val.replace("<", "&lt;").replace(">", "&gt;")
        elif "generator" in config and field in config["generator"]:
            fn = config["generator"][field]
            val = fn(path=path, annotations=annotations, fields=fields)
            if val == None:
                continue

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

def read_cards(paths):
    """reads cards from the specified example/... paths
    returns a dictionary from path to card"""
    path_to_cards = {}
    for path in paths:
        config = config_for_example(path)
        card = anki_row(path,config)
        if card:
            path_to_cards[path] = card
    return path_to_cards

def find_duplicates(path_to_cards):
    """check for duplicate descriptions
    returns list of cards"""
    description_to_path_to_card = {}
    for path, card in path_to_cards:
        desc = card["description"]
        description_to_path_to_card.setdefault(desc, {})[path] = card

    # find duplicates
    cards = []
    for desc, path_to_card in description_to_path_to_card.items():
        if len(path_to_card) == 1:
            cards += list(path_to_card.values())
        elif len(path_to_card) > 1:
            print_err("duplicate description: '" + desc + "', paths ")
            print_err("in paths ")
            for path in path_to_card:
                print_err("   " + path)
    return cards

def index_cards(cards):
    return dict([(c["example"], i) for i,c in enumerate(cards)])

if __name__ == '__main__':
    arguments = docopt(__doc__, version='read_annotations')

    path_to_cards = read_cards(arguments["<file>"]).items()
    cards = find_duplicates(path_to_cards)

    example_to_index = index_cards(cards)
    example_to_level = calculate_levels(cards)
    cards = [cards[example_to_index[c]] for c,i in sorted(list(example_to_level.items()), key = lambda t: t[1])]

    for card in cards:
        fields = ["example", "description", "pre", "step", "post", "explanation"]
        print("\t".join([str(card.get(f, "")) for f in fields]))


