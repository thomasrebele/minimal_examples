#!/bin/bash

source build_scripts/latex/common.sh

for i in $files; do
	./generate_cards.py $i
done

