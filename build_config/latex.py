#!/usr/bin/env python3

def generate_post_field(path, annotations, fields, **keywords):
    ### TODO: latex compilation
    img_path = path.replace(".tex", ".png")
    if keywords.get("no_hierarchy", False):
        img_path = img_path.replace("/", "-")
    img="<img src=\"" + str(img_path) + "\">"

    return img


config = {
    "slc" : "%x",
    "generator": {
        "post": generate_post_field
    }
}




