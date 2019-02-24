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

"""level_assessment
Browser-based tool to assign difficulty/easiness/level to cards by comparing them.
The actual level can calculated with level_estimate.py

Usage:
  level_assessment.py [options] <file>...

Options:
  --search-orphans=<prefix>     Looks for orphans in comparison-json
                                (considering only files in <prefix>)
  -h --help                     Show this screen.

"""

from docopt import docopt

import datetime
import random

import signal
import sys
from collections import defaultdict

import generate_cards
from http_dialog import *
from common import *


def card_to_id(card):
    if type(card) == str:
        return card

    return card["example"]

def card_to_html(card):
    def code(s):
        if not s: return ""
        return "<pre class=code><code>" + str(s) + "</code></pre>"

    if type(card) == str:
        return card

    r = ""
    if "example" in card:
        r += card["example"]
        r += "<br>"
    if "pre" in card:
        r += code(card["pre"])
        r += "<br>"
    if "description" in card:
        r += card["description"]
        r += "<br>"
    if "step" in card:
        r += code(card["step"])
        r += "<br>"
    if "post" in card:
        r += code(card["post"])
        r += "<br>"
    if "explanation" in card:
        r += card["explanation"]
    return r

def rand_card(weights):
    """index of random card, prefering cards which have not much data yet"""
    total = sum(weights)
    r = random.uniform(0,total)
    orig_r = r

    for i, w in enumerate(weights):
        r -= w
        if r <= 0:
            return i

    r = random.randrange(len(weights))
    return r

def inverse_count_weights():
    weights = []
    for c in cards:
        weight = 1
        card_id = card_to_id(c)
        if card_id in card_to_count:
            weight = 1./(card_to_count[card_id]+1)
        weights += [weight]
    return weights

def breadth_first_search(start, max_dist, init, visit_fn):
    """Walks over data graph starting with nodes specified in start.
    visit_fn is a function for updating a dictionary of nodes to values"""
    node_to_val = {}
    for node in start:
        if callable(init):
            node_to_val[node] = init(node)
        else:
            node_to_val[node] = init
    queue = list(start)
    for i in range(1,max_dist):
        new_queue = [ ]
        def visit(card, neighbor, node_to_val=node_to_val, new_queue=new_queue):
            if visit_fn(card, neighbor, i, node_to_val):
                new_queue += [neighbor]

        for card in queue:
            if card in data:
                for neighbor in data[card]:
                    visit(card, neighbor)
            for neighbor,d in data.items():
                if card in d:
                    visit(card, neighbor)
        queue = new_queue
    return node_to_val

def distance(start, max_dist = 10):
    def visit(card, neighbor, dist, node_to_val):
        if not neighbor in node_to_val:
            node_to_val[neighbor] = dist
            return True

    return breadth_first_search(start, max_dist, 0, visit)

def reachability(start, max_dist):
    def visit(c1, c2, dist, node_to_val):
        rel1 = node_to_val.setdefault(c1, set())
        rel2 = node_to_val.setdefault(c2, set())
        rel1.add(c2)
        rel2.add(c1)
        rel1.update(rel2)
        rel2.update(rel1)

    node_to_val = breadth_first_search(start, max_dist, lambda x: set(), visit)
    return node_to_val

def reachability_coefficient(start, max_dist=10):
    reach = reachability(start, max_dist)
    def calc(node):
        if not node in reach:
            return 0
        else:
            return len(reach[node])/float(len(cards))
    coefficient = [calc(card_to_id(card)) for card in cards]
    return coefficient

def distance_weights(dist, max_dist):
    weights = [dist.get(card_to_id(c), max_dist)**4 for c in cards]
    return weights


use_reachability = True
def card_pair():
    """select next two cards which should be compared"""
    global use_reachability
    if use_reachability:
        weights = [(1-i)**2 for i in reachability_coefficient(card_to_count)]
        use_reachability = sum(weights) >= 1

    if not use_reachability:
        weights = inverse_count_weights()

    aidx = rand_card(weights)

    max_dist = 10
    start = card_to_id(cards[aidx])
    dist = distance([start], max_dist)
    dist_weights = distance_weights(dist, 10000)

    bidx = rand_card(dist_weights)
    if aidx == bidx:
        return card_pair()

    key = card_to_id(cards[bidx])
    return (cards[aidx], cards[bidx], str(dist.get(key, "inf")))


    ### installing signal handler
def signal_handler(signal, frame):
    save()
    sys.exit(0)

def save(path="output/level_data.json"):
    if len(data) > 0:
        with open(path, "w") as f:
            f.write(to_json(data))
            print("saved to " + path)

def stat():
    global card_to_count
    # initialize
    pair_count = 0
    covered = set()
    for c1, d in data.items():
        if not c1 in card_to_count: continue
        covered.add(c1)
        for c2, l in d.items():
            if not c2 in card_to_count: continue
            covered.add(c2)
            pair_count += 1

    stat = ""
    n = len(cards)
    stat += " " + str(n) + " cards\n"
    stat += " " + str(pair_count) + " pairs\n"
    stat += "card coverage " + str(int(len(covered) / float(len(cards))*1000)/10) + "%\n"
    stat += "pair coverage " + str(int(pair_count / (0.5*(n-1)**2 + 0.5*(n-1))*1000)/10) + "%\n"
    coefficient = reachability_coefficient(card_to_count, max_dist=2)
    reachability = sum(coefficient) / len(cards)
    stat += "reachability: " + str(int(reachability*1000)/10) + "%\n"
    stat += "not reachable: " + str(len([i for i in coefficient if i == 0])) + "\n"
    return stat


if __name__ == '__main__':
    # setup: signal handler
    signal.signal(signal.SIGINT, signal_handler)

    arguments = docopt(__doc__, version='read_annotations')
    path_to_cards = generate_cards.read_cards(arguments["<file>"])
    cards = list(path_to_cards.values())

    print(cards[0])

    cards = ["A","B", "C"]

    ### data that is changed by the dialog
    # card1 to card2 to (card1_easier, equals, card2_easier)
    data = {}
    data = from_json_file("output/level_data.json")
    i = datetime.datetime.now()

    if arguments["--search-orphans"]:
        prefix = arguments["--search-orphans"]
        if prefix.startswith("examples/"):
            prefix = prefix[9:]
        data_examples = set()
        for c1, d in data.items():
            if c1.startswith(prefix):
                data_examples.add(c1)
            for c2 in data:
                if c2.startswith(prefix):
                    data_examples.add(c2)
        missing = data_examples.difference([c["example"] for c in cards])
        if len(missing) > 0:
            print("missing: ")
            for ex in missing:
                print("  " + ex)

    else:
        save("output/backup/" + i.isoformat())

        # index for better sampling
        card_to_count = dict([(card_to_id(c), 0) for c in cards])
        for c1,d in data.items():
            if not c1 in card_to_count: continue
            for c2, l in d.items():
                if not c2 in card_to_count: continue
                card_to_count[c1] = card_to_count.setdefault(c1, 0) + sum(l)
                card_to_count[c2] = card_to_count.setdefault(c2, 0) + sum(l)

        print(stat())

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
                if path.endswith(".png"):
                    self.file("output/img/" + path[1:])
                    return
                if path.endswith(".ico"):
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
                            choice = card_to_id(req_pair[0])
                        elif choice == "right":
                            choice = card_to_id(req_pair[1])

                        keys = [card_to_id(i) for i in req_pair[0:2]]
                        keys = sorted(keys)
                        l = data.setdefault(keys[0], {}).setdefault(keys[1], [0,0,0])
                        change = True
                        if keys[0] == choice:
                            l[0] += 1
                        elif keys[1] == choice:
                            l[2] += 1
                        elif choice == "equal":
                            l[1] += 1
                        else:
                            change = False
                            print("unknown choice " + choice)

                        if change:
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
                print("next request id: " + str(req_id))

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
                self.write(stat().replace("\n", "; "))
                keys = [card_to_id(i) for i in req_pair[0:2]]
                self.write(" left seen? " + str(card_to_count.get(keys[0], 0)) + "x")
                self.write(" right seen? " + str(card_to_count.get(keys[1], 0)) + "x")

                keys = sorted(keys)
                pair_seen = sum(data.get(keys[0], {}).get(keys[1], [0]))
                self.write(" pair seen? " + str(pair_seen) + "x")
                self.write(" dist? " + str(req_pair[2]))
                self.write("<br>")
                s = "<a href=\"/?id="  + str(req_id) + "&choice="
                self.write(s + "left\" id=\"left\">left is easier (1)</a> &nbsp; ")
                self.write(s + "equal\" id=\"equal\">equally difficult (2)</a> &nbsp; ")
                self.write(s + "right\" id=\"right\">right is easier (3)</a> &nbsp;")
                self.write(s + "skip\" id=\"skip\">skip (4)</a> &nbsp;")
                self.write("<a href=\"/quit\" id=\"quit\">quit (5)</a>")
                self.write("</div>")

                self.write("""<script>
                    document.addEventListener("keyup",function(e){
                       var key = e.which||e.keyCode;
                       console.log(key);
                       switch(key){
                          case 49: document.getElementById("left").click(); break;
                          case 50: document.getElementById("equal").click(); break;
                          case 51: document.getElementById("right").click(); break;
                          case 52: document.getElementById("skip").click(); break;
                          case 53: document.getElementById("quit").click(); break;
                       }
                    });
                    </script>""")

                self.write("</body>")


        http_dialog(port=8000, handler=Handler)

        save()

