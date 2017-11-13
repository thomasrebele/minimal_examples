#!/bin/bash

if [ "$1" == "" ]; then
	echo "usage: <example.sh>"
	exit 1
fi

file=$(pwd)/$1
dir=tmp/$1

rm -rf $dir
mkdir -p $dir
(
	cd $dir
	source $file
)

