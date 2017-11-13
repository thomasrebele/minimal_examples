#!/usr/bin/env python3

import subprocess
from jinja2 import Environment

import os
import sys
script_dir=os.path.dirname(os.path.realpath(__file__))
git_dir = sys.argv[1]

def run(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=git_dir)
    out = []
    for line in p.stdout.readlines():
        out += [line.decode("utf-8")]
    return out

class Commit:
    pass

id_to_commit = {}
commits = []

# parse git log
for line in run("git log --all --reflog --format=format:%H'\t'%P'\t'%s'\t'%an'\t'%d"):
    c = Commit()
    c.commit, c.parent_ids, c.message, c.author, c.branches = line.split('\t')
    if c.parent_ids == '':
        c.parent_ids = []
    else:
        c.parent_ids = c.parent_ids.split(' ')
    c.children = []
    id_to_commit[c.commit] = c
    commits += [c]

# replace c.parents by objects
for c in commits:
    parents = []
    for p in c.parent_ids:
        parent_commit = id_to_commit[p]
        parent_commit.children += [c]
        parents += [parent_commit]
    c.parents = parents

used_cols = []

for c in commits:
    if hasattr(c, "col"): continue
    c.firstChild = True

    if len(c.children) > 0:
        child = c.children[0]
        if child.firstChild:
            c.col = child.col
            child.firstChild = False
            continue

    new_col = 0 if len(used_cols) == 0 else max(used_cols) + 1
    c.col = new_col
    used_cols += [new_col]

tikz = ""

for i, c in enumerate(commits):
    c.name = chr(64+len(commits)-i)
    tikz += "\\node[commit] (" + c.name + ") at (" + str(c.col*0.35) + "," + str(i) + ") {" + c.name + "};\n"

for c in commits:
    for p in c.parents:
        tikz += "\\draw (" + c.name + ") to (" + p.name + ");\n"

tikz += "\\node[fit="
for c in commits:
    tikz += "(" + c.name + ")"
tikz += "] (tree) {};\n"

for i, c in enumerate(commits):
    tikz += "\\node[message] at (tree.east |- 0.5," + str(i) + ") {" + c.message + "};"

with open(script_dir + "/template.tex") as f:
    template = f.read()
print(Environment().from_string(template).render(tikz=tikz))

