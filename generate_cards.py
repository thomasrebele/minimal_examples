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

from os import chdir
import pathlib
from docopt import docopt
import traceback

try:
    genanki = None
    import genanki.genanki as genanki
except Exception as e:
    clone_cmd_https = "git clone https://github.com/kerrickstaley/genanki.git"
    clone_cmd_ssh = "git clone git@github.com:kerrickstaley/genanki.git"
    print("genanki not found, please execute")
    print("    " + clone_cmd_ssh)
    print("or")
    print("    " + clone_cmd_https)
    print()
    raise e


from level_estimate import *
from common import *

# TODO:
no_hierarchy=False
prevent_duplicate_descriptions=False


def load_cards(path_to_cards, prevent_duplicate_descriptions):
    """check for duplicate descriptions
    returns list of cards"""
    description_to_path_to_card = {}
    for path, card in path_to_cards:
        desc = card["description"]
        description_to_path_to_card.setdefault(desc, {})[path] = card

    # find duplicates
    cards = []
    for desc, path_to_card in description_to_path_to_card.items():
        if len(path_to_card) == 1 or not prevent_duplicate_descriptions:
            cards += list(path_to_card.values())
        elif len(path_to_card) > 1:
            print_err("duplicate description: '" + desc + "', paths ")
            print_err("in paths ")
            for path in path_to_card:
                print_err("   " + path)
    return cards

def index_cards(cards):
    return dict([(c["example"], i) for i,c in enumerate(cards)])

################################################################################
# genanki
################################################################################

minex_deck = None

if genanki:

    def read_model_file(path):
        return pathlib.Path(path).read_text()

    minex_model = genanki.Model(
      1508403096468,
      'General::IT',
      fields=[
        {'name': 'example'},
        {'name': 'description'},
        {'name': 'pre'},
        {'name': 'step'},
        {'name': 'post'},
        {'name': 'explanation'},
      ],
      templates=[
            {
                "name": "Card 1",
                "qfmt": read_model_file("model/question"),
                "afmt": read_model_file("model/answer")
            }
        ],
      css=read_model_file("model/style.css"))

    class MinExNote(genanki.Note):
        @property
        def guid(self):
            return genanki.guid_for(self.fields[0])

    minex_deck = genanki.Deck(
      1509187590598,
      'General::IT')


################################################################################
# main
################################################################################

if __name__ == '__main__':
    arguments = docopt(__doc__, version='read_annotations')

    path_to_cards = read_cards(arguments["<file>"]).items()
    cards = load_cards(path_to_cards, prevent_duplicate_descriptions)

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
        values=[str(card.get(f, "")) for f in fields]
        print("\t".join(values))

        if minex_deck:
            minex_note = MinExNote(
              model=minex_model,
              fields=values)

            minex_deck.add_note(minex_note)

    output_file = "/tmp/output.apkg"
    if minex_deck:
        package = genanki.Package(minex_deck)
        package.write_to_file(output_file)
        print("wrote Anki deck to " + str(output_file))


