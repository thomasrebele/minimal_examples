#!/usr/bin/env python3

"""anki_row

Usage:
  anki_row.py [options] [<file>...]

Options:
  -h --help                     Show this screen.

"""

from docopt import docopt
from collections import defaultdict

from common import *

def get_level(comp, c1l, c2l):
    s = sum(comp)
    x = [i / s for i in comp]
    diff = abs(c1l - c2l)
    mid = (c1l+c2l)/2
    new_l = [mid-1-diff, mid, mid+1+diff]


    return sum([x[i] * new_l[i] for i in range(3)])


def normalize(card_to_level, min_level, max_level):
    lower = min(card_to_level.values())
    upper = max(card_to_level.values())
    if upper == max_level and lower == 0:
        return

    for c, l in card_to_level.items():
        new_l = (l - lower) / (upper - lower) * (max_level - min_level) + min_level
        card_to_level[c] = float(int(new_l))


if __name__ == '__main__':
    data = from_json_file("output/level_data.json")

    min_level = 1
    max_level = 100
    card_to_level = defaultdict(lambda: 1)

    # initialize
    pair_count = 0
    for c1, d in data.items():
        for c2, l in d.items():
            pair_count += 1

    for it in range(100):
        # initialize
        card_count = defaultdict(lambda: 1)
        for c1, d in data.items():
            for c2, comp in d.items():
                c1l = card_to_level[c1]
                c2l = card_to_level[c2]
                if "ownership-move2" in c1: print("comp " + str(comp) + " c1l/c2l " + str([c1l, c2l]) + " level " + str(get_level(comp, c1l, c2l)))
                card_to_level[c1] += get_level(comp, c1l, c2l)
                card_to_level[c2] += get_level(list(reversed(comp)), c2l, c1l)

                card_count[c1] += 1
                card_count[c2] += 1
        for card, count in card_count.items():
            card_to_level[card] /= count

        normalize(card_to_level, min_level, max_level)

    lst = sorted(list(card_to_level.items()), key = lambda t: t[1])

    #print([c for c,l in lst])
    for cl in lst:
        print(str(cl))

    n = len(card_to_level)
    print("level for " + str(n) + " cards")
    print("assessments " + str(int(pair_count / (0.5*(n-1)**2 + 0.5*(n-1))*1000)/10) + "%")


