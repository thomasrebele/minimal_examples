#!/bin/bash

if [ "$1" == "" ]; then
	echo "usage: <example.sh>"
	exit 1
fi

basedir=$(pwd)
tex_dir=$basedir/tmp/tex/$1
log_dir=$basedir/tmp/log/$1
img_dir=$basedir/output/img

out_prefix=$img_dir/${1%.sh}
git_dir=tmp/$1

i=0

vis_git() {
	$basedir/build_scripts/git/vis_git.py "$@" > $tex_dir/$i.tex
	(
		cd $tex_dir
		pdflatex -interaction nonstopmode $i.tex > $i.output

		convert_options="-define png:compression-level=9  -define png:compression-filter=2 -define png:compression-strategy=1"
		png=$out_prefix-$i.png
		montage -density 600 $i.pdf -resize 50% -tile 1x -geometry +1+5 -background none $convert_options $png >> $i.output
		convert $png -trim +repage $png
		if type pngquant > /dev/null; then
			pngquant --ext .png --force $png
		fi
		echo "<img src=\"${png#$img_dir/}\">"
	)
	export i=$(( i+1 ))
}

x() {
	echo "#x $@"
}

cid=0
# usage: add_commit <message>
# adds a new file (different filename to avoid conflicts)
add_commit() {
	echo "#$cid" > $cid.txt
	git add $cid.txt
	git commit -m "$1"
	export cid=$(( cid+1 ))
}


rm -rf $git_dir
mkdir -p $git_dir $tex_dir $log_dir
(
	echo "generating $1"
	cd $git_dir
	source $basedir/$1 > $log_dir/output
)

