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
	file=$(basename $i)
	mkdir -p $texout/$dir $imgout/$dir
	pdf=$texout/${i/tex/pdf}
	png=$imgout/${i/tex/png}

	echo " "
	[ ! -e $pdf -o $i -nt $pdf ] && (
		cd $dir
		rel=$(echo "$dir" | sed 's:^./::; s:[^/]*:..:g')
		cmd="pdflatex -interaction nonstopmode -output-directory $rel/$texout/$dir $file"
		echo "dir $dir"
		echo "compiling: $cmd"
		$cmd
	)

	if [ ! -e $png -o $pdf -nt $png ]; then
		convert_options="-define png:compression-level=9  -define png:compression-filter=2 -define png:compression-strategy=1"
		convert -density 600 $pdf -resize 50% $convert_options $png
		if type pngquant > /dev/null; then
			pngquant --ext .png --force $png
		fi
	else
		echo "$png is newer than $pdf"
	fi

done
