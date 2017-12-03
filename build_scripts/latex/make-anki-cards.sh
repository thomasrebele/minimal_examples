#!/bin/bash

source build_scripts/latex/common.sh

for i in $files; do
	./anki_row.py $i
done

