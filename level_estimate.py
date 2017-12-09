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

def get_level(l):
    s = sum(l)
    x = [i / s for i in l]
    return -x[0] + x[2]


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
    card_to_level = defaultdict(lambda: 0)

    # initialize
    pair_count = 0
    for c1, d in data.items():
        for c2, l in d.items():
            pair_count += 1
            card_to_level[c1] += get_level(l)
            card_to_level[c2] += get_level(list(reversed(l)))


    normalize(card_to_level, min_level, max_level)

    for it in range(100):
        # initialize
        for c1, d in data.items():
            for c2, l in d.items():
                card_to_level[c1] += card_to_level[c2] * get_level(l)
                card_to_level[c2] += card_to_level[c1] * get_level(list(reversed(l)))

        normalize(card_to_level, min_level, max_level)

    normalize(card_to_level, min_level, max_level)
    n = len(card_to_level)
    print("level for " + str(n) + " cards")
    print("assessments " + str(int(pair_count / (0.5*(n-1)**2 + 0.5*(n-1))*1000)/10) + "%")


