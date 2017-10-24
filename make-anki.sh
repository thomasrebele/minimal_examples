#!/bin/bash

if [ ! "$*" == "" ]; then 
	files="$*";
else
	files=$(find -name '*.tex' | sed 's:^\./::')
fi

for i in $files; do
	./anki-row.sh $i
done
