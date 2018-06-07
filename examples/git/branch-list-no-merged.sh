#!/bin/bash

#x description="list of all branches"
#x state="empty directory"

git init
add_commit "init"
add_commit "m"

git checkout HEAD^
git checkout -b b1
add_commit "b1"

git checkout HEAD^
git checkout -b b2
add_commit "b2"

git checkout master

git merge --strategy=ours b1

# make annotation in output file
x "pre={"
vis_git .
x "}"

# track code and output
x "post={"
#x step={
git branch --list --no-merged
#x }
x "}"



