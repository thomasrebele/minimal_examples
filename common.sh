#!/bin/bash

# command line parsing from https://stackoverflow.com/a/29754866/1562506
getopt --test > /dev/null
if [[ $? -ne 4 ]]; then echo "getopt failed"; exit 1; fi

OPTIONS=h
LONGOPTIONS=no-hierarchy,help
PARSED=$(getopt --options=$OPTIONS --longoptions=$LONGOPTIONS --name "$0" -- "$@")
if [[ $? -ne 0 ]]; then exit 2; fi
eval set -- "$PARSED"

while true; do
	case "$1" in
		-h|-\?|--help)
			echo "Usage: [OPTIONS] [FILES]"
			echo " -h, --help          Show help message"
			echo " --no-hierachy       Don't use subfolders to organize files"
			exit 0;;
		--no-hierarchy)
			no_hierarchy=1; shift;;
		--)
			shift; break;;
		*)
			echo "error while parsing $1"; exit 3;;
	esac
done

if [ ! "$*" == "" ]; then 
	files="$*";
else
	files=$(find examples -name '*.tex' | sed 's:^\./::')
fi

html_encode() {
	sed 's/&/\&amp;/g; s/</\&lt;/g; s/>/\&gt;/g; s/"/\&quot;/g; s/'"'"'/\&#39;/g'
}
