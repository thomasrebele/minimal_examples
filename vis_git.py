#!/usr/bin/env python3

"""vis_git

Usage:
  vis_git.py [options] <git-folder>

Options:
  -h --help       Show this screen.
  --version       Show version.
  --author=<val>  Show commit author [default: false].

"""
from docopt import docopt

import subprocess
from jinja2 import Environment

import os
import sys
import distutils
script_dir=os.path.dirname(os.path.realpath(__file__))

def run(cmd, cwd=None):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=cwd)
    out = []
    for line in p.stdout.readlines():
        out += [line.decode("utf-8")]
    return out

class Commit:
    pass

def vis_git_folder(path, show_authors=False):
    id_to_commit = {}
    commits = []

    # parse git log
    for line in run("git log --all --reflog --format=format:%H'\t'%P'\t'%s'\t'%an'\t'%d", cwd=path):
        c = Commit()
        c.commit, c.parent_ids, c.message, c.author, c.branches = line.replace('\n','').split('\t')
        if c.parent_ids == '':
            c.parent_ids = []
        else:
            c.parent_ids = c.parent_ids.split(' ')

        branches = []
        if "HEAD" in c.branches:
            branches += ["HEAD"]
            c.branches = c.branches.replace("HEAD -> ", "").replace("HEAD", "")
        c.branches = c.branches[2:-1]
        if c.branches != '':
            branches += c.branches.split(", ")
        c.branches = [i for i in branches if i != ""]

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

    num_cols = max(used_cols)

    tikz = ""

    tikz += "\\matrix[commit table] {\n"
    for i, c in enumerate(commits):
        c.name = chr(64+len(commits)-i)
        for j in range(num_cols+1):
            if j == c.col:
                tikz += "\\node[commit] (" + c.name + ")  {" + c.name + "};"

            tikz += " & "
        tikz += "\\node[message] {"
        for branch in c.branches:
            tikz += "\\branch{" + branch + "}"
        if len(c.branches) > 0:
            tikz += " "
        tikz += c.message + "}; &"
        if show_authors:
            tikz += "\\node[author]  {" + c.author + "}; &"
        tikz += "\\\\\n"
    tikz += "};\n"

    for c in commits:
        for p in c.parents:
            tikz += "\\draw (" + c.name + ") to (" + p.name + ");\n"

    with open(script_dir + "/template.tex") as f:
        template = f.read()
    print(Environment().from_string(template).render(tikz=tikz))

def str_to_bool(s):
    s = s.lower()
    if s in ["true", "yes", "y"]: return True
    if s in ["false", "no", "n"]: return False
    raise ValueError("no boolean: " + str(s))

if __name__ == '__main__':
    arguments = docopt(__doc__, version='vis_git')
    vis_git_folder(arguments["<git-folder>"],
        show_authors=str_to_bool(arguments["--author"])
    )

