#!/bin/bash

files=*.tex
if [ ! "$*" == "" ]; then files="$*"; fi

for i in $files; do
	./anki-row.sh $i
done
