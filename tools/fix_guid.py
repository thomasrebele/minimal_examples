#!/usr/bin/env python3

# Example how to make the guids already imported cards compatible with genanki

import sys

sys.path.insert(0, "/usr/share/anki/")
import anki

sys.path.insert(0, "../genanki/")
import genanki.util as util


deck_name = "General::IT"
ac = anki.Collection("/home/tr/.local/share/Anki2/test/collection.anki2")


deck_id = ac.decks.id(deck_name)
ac.decks.select(deck_id)

notes = ac.findNotes("deck:" + deck_name)

changed = 0
for nid in notes:
    note = ac.getNote(nid)

    new_guid = util.guid_for(note["example"])
    if note.guid != new_guid:
        note.guid = new_guid
        note.flush(mod=True)
        print("updated " + note["example"] + ": " + str(note.guid))
        changed += 1


ac.save()

print("modified: " + str(changed))

