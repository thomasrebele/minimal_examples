#!/bin/bash

echo "make.sh"
./make.sh
echo "make-anki.sh"
./make-anki-cards.sh > output/out.tsv 
echo "rsync"
rsync -av --delete output/img/ ~/.local/share/Anki2/$1/collection.media/web/
