#!/bin/bash

# output directory
texout="out/"
imgout="img/"

mkdir -p $texout $imgout

files=*.tex
if [ ! "$*" == "" ]; then files="$*"; fi

for i in $files; do

	pdflatex -output-directory $texout $i
	convert -density 600 $texout/${i/tex/pdf} -resize 50% $imgout/${i/tex/png}

done
