#!/usr/bin/env python3

import build_config.common_latex as common_latex

config = {
    "read_everything": True,
    "slc" : "%x",
    "logo": "examples/math/math.svg",
    "generator": {
        f:common_latex.generate_field(f) for f in ["pre", "post", "step"]
    }
}


