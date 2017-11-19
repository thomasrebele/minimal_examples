#!/bin/bash

source common.sh

for i in $files; do
	./anki_row.py $i
done

