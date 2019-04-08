

import contextlib
from html import escape
from sys import stderr
from read_annotations import *

# for importing/exporting data
import json
def to_json(obj):
    return json.dumps(obj, cls=json.JSONEncoder, indent=2)

# https://stackoverflow.com/a/20830343/1562506
def print_err(*args, **kwargs):
    print(*args, file=stderr, **kwargs)

def from_json_file(path):
    try:
        with open(path) as f:
            data = json.load(f)
            return data
            for i in data:
                return i
    except FileNotFoundError:
        return json.loads("{}")
    pass

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

def generate_card_from_file(path, config):
    """create a flashcard for a spaced repetition tool (e.g., Anki) in TSV format.
    path: the example file (e.g. examples/rust/hello_world.rs).
    config: specifies which markup tag to use """
    try:
        fn = config.get("generator", {}).get("iterator") or file_iterator

        with fn(path) as it:
            annotations, fields = read_annotations(it, slc=config.get("slc", None), mlc=config.get("mlc", None), read_everything=config.get("read_everything", False))
    except Exception as err:
        print_err("problem with " + path)
        raise err

    base_path = path.replace("examples/", "")
    base_path = base_path[0:base_path.rfind("/")]

    card = {"example" : path.replace("examples/", "")}
    for field in ["description", "pre", "step", "post", "explanation"]:
        val = ""

        if "generator" in config and field in config["generator"]:
            fn = config["generator"][field]
            val = fn(path=path, annotations=annotations, fields=fields)
            if val == None:
                continue
        elif field in fields:
            val = fields[field]["value"]
            if val and config.get("escape_html", {}).get(field, True):
                val = val.replace("<", "&lt;").replace(">", "&gt;")

        if val:
            val = val.replace("\n", "<br/>").replace("\t", "&#9;")
            card[field] = val

    for field in ["step", "description"]:
        if not field in card or card[field] == "":
            print_err("error: " + path + " has no " + field)
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
        card = generate_card_from_file(path,config)
        if card:
            path_to_cards[path] = card
    return path_to_cards
