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

def anki_row(path):
    try:
        annotations, fields = read_annotations(path, slc="%x")
    except Exception as err:
        print_err("problem with " + path)
        raise err

    base_path = path.replace("examples/", "")
    base_path = base_path[0:base_path.rfind("/")]

    img_path = path.replace("examples/", "").replace(".tex", ".png")
    if no_hierarchy:
        img_path = img_path.replace("/", "-")
    img="<img src=\"latex/" + str(img_path) + "\">"

    if not "description" in fields:
        print_err("description missing in " + path)
        return None

    desc=escape(base_path + ": " + fields["description"]["value"])
    step=escape(fields["step"]["value"]).replace("\n", "<br/>").replace("\t", "&#9;")

    l = [str(i) for i in [img, desc, step]]
    return l

if __name__ == '__main__':
    arguments = docopt(__doc__, version='read_annotations')

    desc_idx = 1
    description_to_card = {}
    description_to_path = {}
    for path in arguments["<file>"]:
        row = anki_row(path)
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


