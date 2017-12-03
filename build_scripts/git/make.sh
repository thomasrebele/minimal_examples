#!/bin/bash

imgout="output/img/"

source build_scripts/git/common.sh

for i in $files; do
	dir=$(dirname $i)
	file=$(basename $i)
	mkdir -p $imgout/$dir

	png=$imgout/${i%.sh}-0.png

	[ ! -e $png -o $i -nt $png ] && (
		./build_scripts/git/run-example.sh $i
	)
done
