#!/usr/bin/env python3

"""anki_row

Usage:
  anki_row.py [options] <file>...

Options:
  -h --help                     Show this screen.

"""

from docopt import docopt

import anki_row
from http_dialog import *

if __name__ == '__main__':
    arguments = docopt(__doc__, version='read_annotations')

    path_to_cards = anki_row.read_cards(arguments["<file>"])
    cards = list(path_to_cards.values())

    print("len" + str(len(cards)))

    def card_to_html(card):
        def code(s):
            if not s: return ""
            return "<pre class=code><code>" + str(s) + "</code></pre>"
        r = ""
        r += code(card["pre"])
        r += "<br>"
        r += card["description"]
        r += "<br>"
        r += code(card["step"])
        r += "<br>"
        r += code(card["post"])
        r += "<br>"
        r += card["explanation"]
        return r

    class Handler(RequestHandler):
        def get(self):
            path = self.req_path()
            if path.endswith(".css"):
                self.file(path[1:])
                return

            self.write("<html><head><link rel=\"stylesheet\" href=\"dialog.css\"><meta charset=\"utf-8\" /> </head>")
            self.write("<div class=\"row\">")
            self.write("<div class=\"column\">")
            # left col

            self.write(card_to_html(cards[0]))

            self.write("</div>")
            self.write("<div class=\"column\">")
            # right col

            self.write("right")

            self.write("</div>")
            self.write("</div>")


    http_dialog(port=8000, handler=Handler)

