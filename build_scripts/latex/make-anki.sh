#!/bin/bash

echo "make.sh"
./build_scripts/latex/make.sh
echo "make-anki.sh"
./build_scripts/latex/make-anki-cards.sh > output/out.tsv 
echo "rsync"
rsync -av --delete output/img/examples/ ~/.local/share/Anki2/$1/collection.media/examples/
