#!/usr/bin/env python3

"""vis_git

Usage:
  vis_git.py [options] <git-folder>

Options:
  -h --help         Show this screen.
  --version         Show version.

  --repo=<val>      Name of repository [default: ].
  --author=<val>    Show commit author [default: false].
  --files=<val>     Show files [default: false].
  --content=<val>   Show content of files [default: false]. (not yet implemented)

"""

# TODO
# - remotes? \node{\faGlobe}; & \node[message]{origin}; & \\

from docopt import docopt

import subprocess
from jinja2 import Environment

import os
import sys
import distutils
script_dir=os.path.dirname(os.path.realpath(__file__))


# https://stackoverflow.com/a/1633483/1562506
def iter_first_last(iterator):
    """Iterator which marks the first and the last item.
    Usage: for item, is_first, is_last in iter_first_last(...)
    """

    iterator = iter(iterator)
    prev = next(iterator)
    first = True
    for item in iterator:
        yield prev, first, False
        first = False
        prev = item
    # Last item
    yield prev, first, True

def dirty_files(path):
    staged = {}
    modified = {}
    for line in run("git status --porcelain", cwd=path):
        if len(line) < 3: continue
        f = line[3:]
        if line[0] != " ":
            staged[f] = ""
        if line[1] != "":
            modified[f] = ""
    return staged, modified


def run(cmd, cwd=None):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=cwd)
    out = []
    for line in p.stdout.readlines():
        out += [line.decode("utf-8")]
    return out

class Commit:
    is_head = False
    branches = []
    parents = []
    message = ""
    files = {}

def vis_git_folder(path, repo_name=None, show_authors=False, show_files=False, show_content=False):
    id_to_commit = {}
    commits = []

    # parse git log
    for line in run("git log --date-order --all --reflog --format=format:%H'\t'%P'\t'%s'\t'%an'\t'%d", cwd=path):
        c = Commit()
        c.commit, c.parent_ids, c.message, c.author, c.branches = line.replace('\n','').split('\t')
        if c.parent_ids == '':
            c.parent_ids = []
        else:
            c.parent_ids = c.parent_ids.split(' ')

        branches = []
        #if "HEAD" in c.branches:
        #    branches += ["HEAD"]
        #    c.branches = c.branches.replace("HEAD -> ", "").replace("HEAD", "")
        c.branches = c.branches.replace("HEAD -> ", "\head ")
        c.branches = c.branches[2:-1]
        if c.branches != '':
            branches += c.branches.split(", ")
        c.branches = [i.strip() for i in branches if i != ""]

        c.is_head = "HEAD" in c.branches
        if c.is_head:
            c.branches.remove("HEAD")

        c.children = []
        id_to_commit[c.commit] = c
        commits += [c]

    # replace c.parents by objects
    for c in commits:
        parents = []
        for p in c.parent_ids:
            parent_commit = id_to_commit[p]
            if len(parent_commit.children) == 0:
                c.first_child = True
            parent_commit.children += [c]
            parents += [parent_commit]
        c.parents = parents

    used_cols = []
    for c in commits:
        if hasattr(c, "col"): continue

        if len(c.children) > 0:
            child = c.children[0]
            if child.first_child:
                c.col = child.col
                child.first_child = False
                continue

        new_col = 0 if len(used_cols) == 0 else max(used_cols) + 1
        c.col = new_col
        used_cols += [new_col]

    num_cols = max(used_cols)

    tikz = ""

    staged, modified = dirty_files(path)
    ## TODO: get staged/modified files
    if len(staged) > 0:
        c = Commit()
        c.col = 0
        c.message = "staged"
        c.name = "s"
        c.files = staged
        commits = [c] + commits

    if len(modified) > 0:
        c = Commit()
        c.col = 0
        c.message = "modified"
        c.name = "?"
        c.files = modified
        commits = [c] + commits

    tikz += "\\matrix[commit table] {\n"
    if repo_name:
        tikz += "\\node {\\faServer}; & \\node[message]{\\bf " + repo_name + "}; & \\\\\n"
    for i, c in enumerate(commits):
        if not hasattr(c, "name"):
            c.name = chr(64+len(commits)-i)
        for j in range(num_cols+1):
            if j == c.col:
                tikz += "\\node[commit] (" + c.name + ")  {"
                if c.is_head:
                    tikz += "\\head "
                tikz += c.name + "};"

            tikz += " & "
        tikz += "\\commitmessage{"
        for branch in c.branches:
            tikz += "\\branch{" + branch + "}"
        tikz += c.message + "} &"
        if show_authors:
            tikz += "\\node[author]  {" + c.author + "}; &"
        tikz += "\\\\"

        has_branches = len(c.branches) > 0
        if show_files:
            for (f,content), is_first, is_last in iter_first_last(c.files.items()):
                dist = -1
                if is_first and not has_branches: dist -= 1
                if show_content and not content:
                    f += " {\\tiny(empty)}"
                tikz += "[" + str(dist) + "ex]\n & \\file{" + f + "} & \\\\"
                if show_content and content:
                    tikz += "[-1ex]\n & \\content{" + content + "} & \\\\"
        tikz += "\n"
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
        repo_name=arguments["--repo"],
        show_authors=str_to_bool(arguments["--author"]),
        show_files=str_to_bool(arguments["--files"]),
        show_content=str_to_bool(arguments["--content"])
    )

