#!/usr/bin/env bash

tmp_dir=$(realpath .)/tmp/cpp
mkdir -p $tmp_dir

source build_scripts/cpp/common.sh

for i in $files; do
	f=$(realpath $i)
	dir=$(dirname $i)
	dir=${dir}
	file=$(basename $i)

	if [ "$f" -nt "$tmp_dir/$file.out" ]; then
		pushd "$tmp_dir"
		g++ "$f" -o "$file.out"
		./"$file.out"
		popd
	fi

done
