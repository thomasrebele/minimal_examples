#!/usr/bin/env python3

import subprocess

def run(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = ""
    for line in p.stdout.readlines():
        out += line.decode("utf-8")
    return out



print(run("git log --format=format:%H$'\t'%P$'\t'%s$'\t'%an"))
