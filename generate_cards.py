#!/usr/bin/env python3

# Copyright (C) 2017-2018  Thomas Rebele
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""generate_cards

Usage:
  generate_cards.py [options] <file>...

Options:
  -h --help                     Show this screen.

"""


from docopt import docopt
from html import escape
from sys import stderr
import contextlib

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

@contextlib.contextmanager
def file_iterator(path):
    with open(path) as f:
        it = iter(f)
        yield it

def generate_cards(path, config):
    """create a flashcard for a spaced repetition tool (e.g., Anki) in TSV format.
    path: the example file (e.g. examples/rust/hello_world.rs).
    config: specifies which markup tag to use """
    try:
        fn = config.get("generator", {}).get("iterator") or file_iterator

        with fn(path) as it:
            annotations, fields = read_annotations(it, slc=config.get("slc", None), mlc=config.get("mlc", None))
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
            if config.get("escape_html", {}).get(field, True):
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

    logo = config.get("logo")
    if logo:
        logo = "<img src='" + logo + "'/>"
    else:
        logo = base_path

    card["description"] = logo + ": " + card["description"]
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
        card = generate_cards(path,config)
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
    for ex in example_to_level:
        if not ex in example_to_index:
            print_err("not found " + str(ex))

    cards_levels = [(c, example_to_level.get(c["example"], 100)) for c in cards]
    sorted_cards_levels =  sorted(cards_levels, key = lambda t: t[1])
    cards = [c for (c,l) in sorted_cards_levels]

    for card in cards:
        fields = ["example", "description", "pre", "step", "post", "explanation"]
        print("\t".join([str(card.get(f, "")) for f in fields]))


