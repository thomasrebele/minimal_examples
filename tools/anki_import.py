#!/usr/bin/env python3

# Imports the generated anki deck and synchronizes with the server

import sys

sys.path.insert(0, "/usr/share/anki/")
import anki
import anki.sync
from anki.importing.apkg import AnkiPackageImporter

sys.path.insert(0, "../genanki/")
import genanki.util as util


deck_name = "General::IT"
ac = anki.Collection("/home/tr/.local/share/Anki2/test/collection.anki2")


deck_id = ac.decks.id(deck_name)
ac.decks.select(deck_id)


importer = AnkiPackageImporter(ac, "/tmp/output.apkg")

print("Import")
importer.run()

for i in importer.log:
    if i.startswith("[Identical]"):
        continue

    if i and i.strip():
        print("> " + i)

ac.save()

print()

################################################################################
# sync
################################################################################

import aqt.profiles

pm = aqt.profiles.ProfileManager()
pm.setupMeta()
pm.openProfile("test")
pm.ensureProfile()

hkey = pm.profile['syncKey']
hostNum = pm.profile.get("hostNum")

print("Synchronize")

server = anki.sync.RemoteServer(hkey, hostNum) # incremental
syncer = anki.sync.Syncer(ac, server)
sync_result = syncer.sync()

print(sync_result)

