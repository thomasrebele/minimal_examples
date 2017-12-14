#!/bin/bash

#x description="merge"

git init
echo "# Hello world" > readme.md
git add readme.md
git commit -m "init"

echo "# Hello world 2" > readme.md
git commit -am "first commit"

git checkout HEAD^

echo "# Hello world 3" > license.md
git add license.md
git commit -am "other commit"

git branch "other"

git checkout master

# make annotation in output file
x "pre={"
vis_git .
x "}"

#x step={
git merge other
#x }

# make annotation in output file
x "post={"
vis_git .
x "}"

