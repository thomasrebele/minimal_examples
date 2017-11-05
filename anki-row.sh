#!/bin/bash

desc=$(grep '% description' $1 | sed 's/.*description: \(.*\)/\1/')

code=$(sed 's/\t/\&#9;/g' $1 | awk '
	BEGIN { first=1; out=0; } 
	/% start/ { 
		out=1; 
		if(first==1) {first=0} 
		else {print("...")};
		next
	} 
	/% end/ {out=0} 
	out==1 { print $0}' | sed 's/$/<br\/>/g' | tr -d '\n')

img="<img src=\"latex/${1%.tex}.png\">"

if [ "$no_hierarchy" == "1" ]; then
	img=${img//\//-}
fi

desc_lines=$(echo "$desc" | wc -l)
if [ "$desc_lines" != "1" ]; then
	echo "one line of description needed, got $desc_lines in $1" 1>&2
elif [ "$code" == "" ]; then
	echo "start/end tag missing in $1" 1>&2
else
	echo "$img"$'\t'"$desc"$'\t'"$code"
fi
