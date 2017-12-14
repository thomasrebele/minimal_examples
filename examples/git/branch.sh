#!/bin/bash

#x description="create local repository"
#x state="empty directory"

git init
echo "# Hello world" > readme.md
git add readme.md
git commit -m "init"

echo "# Hello world 2" > readme.md
git commit -am "first commit"

git checkout $(git log --format=format:%H | head -n 1)
git branch -d master

# make annotation in output file
x "pre={"
vis_git .
x "}"

#x code={
git branch mybranch
#x }

# make annotation in output file
x "post={"
vis_git .
echo "(triangle marks HEAD)"
x "}"

