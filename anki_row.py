#!/usr/bin/env python3

"""anki_row

Usage:
  anki_row.py [options] <file>

Options:
  -h --help                     Show this screen.

"""

from docopt import docopt
from html import escape

from minimal_examples_common.read_annotations import *

def anki_row(path):
    annotations, fields = read_annotations(path, slc="%x")

    img_path = path.replace("examples/", "").replace(".tex", ".png")
    img="<img src=\"latex/" + str(img_path) + "\">"
    base_path = img_path[0:img_path.rfind("/")]

    desc=escape(base_path + ": " + fields["description"]["value"])
    code=escape(fields["code"]["value"]).replace("\n", "<br/>").replace("\t", "&#9;")
    return str(img) + "\t" + str(desc) + "\t" + str(code)

if __name__ == '__main__':
    arguments = docopt(__doc__, version='read_annotations')
    row = anki_row(
            arguments["<file>"]
        )

    print(row)
