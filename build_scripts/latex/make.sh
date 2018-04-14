#!/bin/bash

# output directory
texout="output/pdf/"
imgout="output/img/"

mkdir -p $texout $imgout

source build_scripts/latex/common.sh

for i in $files; do
	dir=$(dirname $i)
	dir=${dir}
	file=$(basename $i)
	mkdir -p $texout/$dir $imgout/$dir
	pdf=$texout/$dir/${file%.tex}.pdf
	png=$imgout/$dir/${file%.tex}.png

	[ ! -e $pdf -o $i -nt $pdf ] && (
		cd $dir
		rel=$(echo "$dir" | sed 's:^./::; s:[^/]*:..:g')
		cmd="pdflatex -interaction nonstopmode -output-directory $rel/$texout/$dir $file"
		echo " "
		echo "dir $dir"
		echo "compiling: $cmd"
		# TODO: specify compilation in doc
		$cmd
		$cmd
		$cmd
	)

	if [ ! -e $png -o $pdf -nt $png ]; then
		convert_options="-define png:compression-level=9  -define png:compression-filter=2 -define png:compression-strategy=1"
		montage -density 600 $pdf -resize 50% -tile 1x -geometry +1+5 -background none $convert_options $png
		convert $png -trim +repage $png
		if type pngquant > /dev/null; then
			pngquant --ext .png --force $png
		fi
	fi

	if [ "$no_hierarchy" == "1" ]; then
		nohDir=${imgout/img/img-nh}
		noh=${i/tex/png}
		noh=$nohDir/latex-${noh//\//-}
		mkdir -p $nohDir
		if [ ! -e $noh ]; then
			ln $png $noh
		fi
	fi

done
