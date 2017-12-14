#!/bin/bash

#x description="list of all branches"
#x state="empty directory"

git init
echo "# Hello world" > readme.md
git add readme.md
git commit -m "init"

git branch b1 $(git log --format=format:%H | head -n 1)

echo "# Hello world 2" > readme.md
git commit -am "first commit"

git branch b2 $(git log --format=format:%H | head -n 1)

echo "# Hello world 3" > readme.md
git commit -am "second commit"

# make annotation in output file
x "pre={"
vis_git .
x "}"

# track code and output
x "post={"
#x code={
git branch --list
#x }
x "}"



