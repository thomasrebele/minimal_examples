#!/bin/bash

#x description="change user name"

git init
echo "# Hello world" > readme.md
git add readme.md
git config user.name "user1"
git commit -m "first commit"

#x code={
git config user.name "user2"
git config user.email "user2@mail.com"
#x }

# make annotation in output file
x "pre={"
vis_git --author=true .
x "}"

echo "A" >> readme.md
git add readme.md
git commit -am "my commit"

# make annotation in output file
x "post={"
vis_git --author=true .
x "}"

