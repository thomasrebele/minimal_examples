#!/bin/bash

if [ ! "$*" == "" ]; then 
	files="$*";
else
	files=$(find -name '*.tex')
fi

for i in $files; do
	./anki-row.sh $i
done
