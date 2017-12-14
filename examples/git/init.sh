#!/bin/bash

#x description="create local repository"
#x state="empty directory"

#x code={
git init
echo "# Hello world" > readme.md
git add readme.md
git commit -m "first commit"
#x }

# make annotation in output file
x "post={"
vis_git .
echo "(triangle marks HEAD)"
x "}"

