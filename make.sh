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
	pdf=$texout/${i/tex/pdf}
	png=$imgout/${i/tex/png}

	[ $i -nt $pdf ] && pdflatex -output-directory $texout/$dir $i
	[ $pdf -nt $png ] && convert -density 600 $pdf -resize 50% $png

done
