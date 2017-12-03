#!/bin/bash

imgout="output/img/"

source common.sh

for i in $files; do
	dir=$(dirname $i)
	file=$(basename $i)
	mkdir -p $imgout/$dir

	png=$imgout/${i%.sh}-0.png

	[ ! -e $png -o $i -nt $png ] && (
		./run-example.sh $i
	)
done
