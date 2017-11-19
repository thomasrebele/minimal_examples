#!/bin/bash

#x description="create local repository"
#x before="empty directory"

#x code={
git init
echo "# Hello world" > readme.md
git add readme.md
git commit -m "first commit"
#x }

# make annotation in output file
x "after={"
vis_git .
x "}"




