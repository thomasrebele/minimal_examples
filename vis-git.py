#!/usr/bin/env python3

import subprocess

def run(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = []
    for line in p.stdout.readlines():
        out += [line.decode("utf-8")]
    return out

class Commit:
    pass

idToCommit = {}
commits = []

for line in run("git log --format=format:%H'\t'%P'\t'%s'\t'%an"):
    c = Commit()
    c.commit, c.parents, c.message, c.author = line.split('\t')
    if c.parents == '':
        c.parents = []
    else:
        c.parents = c.parents.split(' ')
    idToCommit[c.commit] = c
    commits += [c]

for c in commits:
    parents = []
    print(c.parents)
    for p in c.parents:
        parents += [idToCommit[p]]
    c.parents = parents


