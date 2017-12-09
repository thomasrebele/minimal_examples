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
from random import randrange

import signal
import sys

# for importing/exporting data
import json
def to_json(obj):
    return json.dumps(obj, cls=json.JSONEncoder, indent=2)

def from_json_file(path):
    with open(path) as f:
        data = json.load(f)
        return data
        for i in data:
            return i
    pass


def card_to_html(card):
    def code(s):
        if not s: return ""
        return "<pre class=code><code>" + str(s) + "</code></pre>"
    r = ""
    r += card["example"]
    r += "<br>"
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

def card_pair():
    """select next two cards which should be compared"""
    aidx = randrange(len(cards))
    bidx = randrange(len(cards))
    if aidx == bidx:
        return card_pair()

    return (cards[aidx], cards[bidx])


    ### installing signal handler
def signal_handler(signal, frame):
    save()
    sys.exit(0)

def save():
    with open("output/level_data.json", "w") as f:
        f.write(to_json(data))
        print("saved to output/level_data.json")

if __name__ == '__main__':
    # setup: signal handler
    signal.signal(signal.SIGINT, signal_handler)

    arguments = docopt(__doc__, version='read_annotations')

    path_to_cards = anki_row.read_cards(arguments["<file>"])
    cards = list(path_to_cards.values())

    print("len" + str(len(cards)))

    ### data that is changed by the dialog
    # card1 to card2 to (card1_easier, equals, card2_easier)
    data = {}

    req_id = 0
    req_pair = []
    class Handler(RequestHandler):
        def get(self):
            global req_pair, req_id, data

            path = self.req_path()
            if path.endswith(".css"):
                self.file(path[1:])
                return

            if path == "/quit":
                self.shutdown()
                return

            # self.write(str(self.args()))
            if "id" in self.args():
                if self.args()["id"][0] == req_id:
                    choice = self.args()["choice"][0]
                    if choice == "left":
                        choice = req_pair[0]["example"]
                    elif choice == "right":
                        choice = req_pair[1]["example"]

                    keys = [i["example"] for i in req_pair]
                    keys = sorted(keys)
                    l = data.setdefault(keys[0], {}).setdefault(keys[1], [0,0,0])
                    if keys[0] == choice:
                        l[0] += 1
                    elif keys[1] == choice:
                        l[2] += 1
                    elif choice == "equal":
                        l[1] += 1

                    data[keys[0]][keys[1]] = l
                else:
                    print("request id wrong: " + str(self.args()["id"]) + " and " + req_id)
            else:
                print("no id in http args")


            ### next round
            req_pair = card_pair()
            req_id = str(randrange(0, 9999999999))

            self.write("<html><head><link rel=\"stylesheet\" href=\"dialog.css\"><meta charset=\"utf-8\" /> </head><body>")
            self.write("<div class=\"row\">")

            # left col
            self.write("<div class=\"column\"><div class=\"cell\">")
            self.write(card_to_html(req_pair[0]))
            self.write("</div></div>")

            # right col
            self.write("<div class=\"column\"><div class=\"cell\">")
            self.write(card_to_html(req_pair[1]))
            self.write("</div></div>")

            self.write("</div>")

            self.write("<div class=\"footer\">")
            s = "<a href=\"/?id="  + str(req_id) + "&choice="
            self.write(s + "left\" id=\"left\">left is easier</a> &nbsp; ")
            self.write(s + "equal\" id=\"equal\">equally difficult</a> &nbsp; ")
            self.write(s + "right\" id=\"right\">right is easier</a> &nbsp;")
            self.write("<a href=\"/quit\">exit</a>")
            self.write("</div>")

            self.write("""<script>
                document.addEventListener("keyup",function(e){
                   var key = e.which||e.keyCode;
                   console.log(key);
                   switch(key){
                      case 49: document.getElementById("left").click(); break;
                      case 50: document.getElementById("equal").click(); break;
                      case 51: document.getElementById("right").click(); break;
                   }
                });
                </script>""")

            self.write("</body>")


    http_dialog(port=8000, handler=Handler)

    save()

