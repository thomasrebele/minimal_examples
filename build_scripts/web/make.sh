#!/bin/bash

# output directory
imgout="output/img/"

mkdir -p $imgout

source common.sh


for i in $files; do
	dir=$(dirname $i)
	file=$(basename $i)
	mkdir -p $imgout/$dir
	png=$imgout/${i%.html}.png

	if [ ! -e $png -o $i -nt $png ]; then
		full=$(full_path $i)
		cutycapt --url=file:$full --out=$png
		convert $png -trim +repage $png
		if type pngquant > /dev/null; then
			pngquant --ext .png --force $png
		fi
	fi

	if [ "$no_hierarchy" == "1" ]; then
		nohDir=${imgout/img/img-nh}
		noh=${i/html/png}
		noh=$nohDir/web-${noh//\//-}
		mkdir -p $nohDir
		if [ ! -e $noh ]; then
			ln $png $noh
		fi
	fi

done
