#!/usr/bin/env python3

import contextlib
import itertools

@contextlib.contextmanager
def generate_iterator(path, **keywords):
    with open(path) as f:
        log_file = "tmp/log/" + path + "/output"
        with open(log_file) as log:
            it_example = iter(f)
            it_log = iter(log)
            yield itertools.chain(it_example, it_log)




config = {
    "slc" : "#x",
    "logo": "examples/logos/git.svg",
    "generator": {
        "iterator": generate_iterator
    },
    "escape_html": {
        "post": False,
        "pre": False
    }
}




