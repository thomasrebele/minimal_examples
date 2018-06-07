#!/bin/bash

#x description="switch to a branch"

git init

add_commit "init"

git checkout -b b1
add_commit "first branch"
git checkout HEAD^
git checkout master
 
add_commit "msg"

# make annotation in output file
x "pre={"
vis_git .
x "}"

#x step={
git checkout b1
#x }

# make annotation in output file
x "post={"
vis_git .
x "}"

