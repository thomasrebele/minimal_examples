#!/usr/bin/env python3

"""read_annotations

Usage:
  read_annotations.py [options] <file>

Options:
  -h --help                     Show this screen.
  --single-line=<start>         Single line comment
  --multi-line="<start> <end>"  Multi line comment
  --version                     Show version.
  --author=<val>                Show commit author [default: false].

"""
from docopt import docopt

import string

class ParserReader:
    def __init__(self, text):
        self.text = text
        self.pos = 0 # position

    def peek(self):
        return self.text[self.pos]

    def read_while(self, fn):
        j = self.pos
        while j<len(self.text) and fn(self.text[j], j):
            j+=1
        if j > self.pos:
            r = self.text[self.pos:j]
            self.pos = j
            return r
        else: return None

    def space(self):
        return self.read_while(lambda c, i: c == " ")

    def name(self):
        return self.read_while(lambda c, i: c in string.ascii_letters)

    def constant(self):
        self.consume(['"'])
        constant = self.read_while(lambda c, i: c != '"')
        self.expect(['"'])
        return constant

    def consume(self, lst):
        """try to read one string in s from text, return it if found"""
        if type(lst) == str: lst = list(lst)
        for s in lst:
            if self.text[self.pos:self.pos+len(s)] == s:
                self.pos += len(s)
                return s
        return None

    def expect(self, lst):
        found = self.consume(lst)
        if found:
            return found
        raise Exception("parsing error, expected one of " + str(lst) + ", got '" + self.text[self.pos:self.pos+50] + "', in '" + self.text + "'")


def parse(s):
    result = {}

    pr = ParserReader(s)
    pr.space()
    name = pr.name()
    if name:
        pr.space()
        op = pr.consume(["="])
        if op:
            pr.space()
            result["type"] = "field"
            result["name"] = name
            result["op"] = op
            if pr.peek() == '"':
                result["value"] = pr.constant()
            elif pr.peek() == '{':
                result["type"] = "field-start"
            return result
    elif pr.peek() == '}':
        result["type"] = "field-end"
        return result


def read_annotations(path, slc, mlc):
    """
        path: input file
        slc: single line comment
        mlc: multi line comment
    """
    # multi line comment start and end
    mlc1, mlc2 = None, None
    if mlc:
        print("MULTILINE COMMENTS NOT YET IMPLEMENTED")
        mlc1, mlc2 = mlc.split(' ')

    # helper function
    def parse_comment(line):
        p = None
        if slc and slc in line:
            comment = line[line.find(slc)+len(slc):]
            p = parse(comment)
        return p

    result = []
    fields = {}
    with open(path) as f:
        #lines = f.read()
        it = iter(f)
        for line in it:
            line = line.replace('\n','')
            p = parse_comment(line)

            if not p: continue
            if p["type"] == "field":
                fields[p["name"]] = p
                result += [p]
            elif p["type"] == "field-start":
                content = ""
                while True:
                    line = it.__next__()
                    tmp = parse_comment(line)
                    if tmp and tmp["type"] == "field-end":
                        break
                    content += line
                op = p["op"]
                if p["name"] in fields:
                    p = fields[p["name"]]
                    p["value"] += "...\n" + content
                else:
                    p["type"] = "field"
                    p["value"] = content
                    fields[p["name"]] = p
                    result += [p]

    return result


if __name__ == '__main__':
    arguments = docopt(__doc__, version='read_annotations')
    annotations = read_annotations(
            arguments["<file>"],
            arguments["--single-line"],
            arguments["--multi-line"]
        )
    for i in annotations:
        print(i)

