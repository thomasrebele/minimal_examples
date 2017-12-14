#!/bin/bash

#x description="rebase"

git init

add_commit "init"

add_commit "first commit"
git checkout -b fix HEAD^
 
add_commit "bugfix"

# make annotation in output file
x "pre={"
vis_git .
x "}"

#x code={
git rebase master
#x }

# make annotation in output file
x "post={"
vis_git .
x "}"

