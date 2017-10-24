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

img="<img src=\"latex/${1/tex/png}\">"

echo "$img"$'\t'"$desc"$'\t'"$code"
