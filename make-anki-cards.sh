#!/bin/bash

source common.sh

for i in $files; do
	source anki-row.sh $i
done

