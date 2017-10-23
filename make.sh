#!/bin/bash

# output directory
texout="output/pdf/"
imgout="output/img/"

mkdir -p $texout $imgout

if [ ! "$*" == "" ]; then 
	files="$*";
else
	files=$(find -name '*.tex')
fi

for i in $files; do
	dir=$(dirname $i)
	mkdir -p $texout/$dir $imgout/$dir
	pdflatex -output-directory $texout/$dir $i
	convert -density 600 $texout/${i/tex/pdf} -resize 50% $imgout/${i/tex/png}

done
