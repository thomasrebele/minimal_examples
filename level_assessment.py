#!/usr/bin/env python3

"""anki_row

Usage:
  anki_row.py [options] <file>...

Options:
  -h --help                     Show this screen.

"""

from docopt import docopt

import datetime
import random

import signal
import sys
from collections import defaultdict

import anki_row
from http_dialog import *
from common import *

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

def rand_card(weights):
    """index of random card, prefering cards which have not much data yet"""
    total = sum(weights)
    r = random.uniform(0,total)

    for i, w in enumerate(weights):
        r -= w
        if r <= 0: return i
    return random.randrange(len(weights))

def inverse_count_weights():
    weights = []
    for c in cards:
        weight = 1
        if c["example"] in card_to_count:
            weight = 1./(card_to_count[c["example"]]+1)
        weights += [weight]
    return weights

def graph_algo(start, max_dist, visit_fn):
    node_to_val = {}
    for node in start:
        node_to_val[node] = 0
    queue = list(start)
    for i in range(1,max_dist):
        new_queue = [ ]
        def visit(neighbor, node_to_val=node_to_val, new_queue=new_queue):
            if visit_fn(neighbor, i, node_to_val):
                new_queue += [neighbor]

        for card in queue:
            if card in data:
                for neighbor in data[card]:
                    visit(neighbor, node_to_val)
            for neighbor,d in data.items():
                if card in d:
                    visit(neighbor, node_to_val)
        queue = new_queue
    return node_to_val

def distance(start, max_dist = 10):
    def visit(neighbor, dist, node_to_val):
        if not neighbor in node_to_val:
            node_to_val[neighbor] = dist
            return True

    return graph_algo(start, max_dist, visit)

def distance_weights(card_idx):
    max_dist = 10
    start = cards[card_idx]["example"]
    dist = distance([start], max_dist=max_dist)
    weights = [dist.get(c["example"], max_dist) for c in cards]
    return weights


def card_pair():
    """select next two cards which should be compared"""
    aidx = rand_card(inverse_count_weights())
    bidx = rand_card(inverse_count_weights())
    if aidx == bidx:
        return card_pair()

    return (cards[aidx], cards[bidx])


    ### installing signal handler
def signal_handler(signal, frame):
    save()
    sys.exit(0)

def save(path="output/level_data.json"):
    if len(data) > 0:
        with open(path, "w") as f:
            f.write(to_json(data))
            print("saved to " + path)



if __name__ == '__main__':
    # setup: signal handler
    signal.signal(signal.SIGINT, signal_handler)

    arguments = docopt(__doc__, version='read_annotations')

    path_to_cards = anki_row.read_cards(arguments["<file>"])
    cards = list(path_to_cards.values())

    ### data that is changed by the dialog
    # card1 to card2 to (card1_easier, equals, card2_easier)
    data = {}
    data = from_json_file("output/level_data.json")
    i = datetime.datetime.now()

    for i in range(2):
        print(distance_weights(i))
    xyz()

    save("output/backup/" + i.isoformat())

    # index for better sampling
    card_to_count = {}
    for c1,d in data.items():
        for c2, l in d.items():
            card_to_count[c1] = card_to_count.setdefault(c1, 0) + sum(l)
            card_to_count[c2] = card_to_count.setdefault(c2, 0) + sum(l)

    req_count = 0
    req_id = 0
    req_pair = []
    class Handler(RequestHandler):
        def get(self):
            global req_pair, req_id, req_count, data, card_to_count

            path = self.req_path()
            if path.endswith(".css"):
                self.file(path[1:])
                return

            if path == "/quit":
                #TODO: self.write("<script>window.close();</script>")
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

                    # update index
                    card_to_count[keys[0]] = card_to_count.setdefault(keys[0], 0) + 1
                    card_to_count[keys[1]] = card_to_count.setdefault(keys[1], 0) + 1

                    req_count += 1
                    if req_count % 10 == 0:
                        save()
                else:
                    print("request id wrong: " + str(self.args()["id"]) + " and " + req_id)


            ### next round
            req_pair = card_pair()
            req_id = str(random.randrange(0, 9999999999))

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
            self.write(s + "left\" id=\"left\">left is easier (1)</a> &nbsp; ")
            self.write(s + "equal\" id=\"equal\">equally difficult (2)</a> &nbsp; ")
            self.write(s + "right\" id=\"right\">right is easier (3)</a> &nbsp;")
            self.write("<a href=\"/quit\" id=\"quit\">quit</a>")
            self.write("</div>")

            self.write("""<script>
                document.addEventListener("keyup",function(e){
                   var key = e.which||e.keyCode;
                   console.log(key);
                   switch(key){
                      case 49: document.getElementById("left").click(); break;
                      case 50: document.getElementById("equal").click(); break;
                      case 51: document.getElementById("right").click(); break;
                      case 52: document.getElementById("quit").click(); break;
                   }
                });
                </script>""")

            self.write("</body>")


    http_dialog(port=8000, handler=Handler)

    save()

