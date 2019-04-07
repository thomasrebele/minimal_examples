
import shutil
import subprocess
from subprocess import call
import pathlib

def generate_field(field):
    def fn(path, annotations, fields, field=field, **keywords):
        found = False
        r = []
        for a in annotations:
            if a["type"] == "other":
                r.append(a["value"])
            if a["type"] == "field" and a["name"] == field:
                r.append(a["value"])
                found = True
        if found:
            # write file
            tmp_path = pathlib.Path("tmp/" + path + "-" + field + ".tex")
            pdf_path = pathlib.Path("tmp/" + path + "-" + field + ".pdf")
            png_path = pathlib.Path("tmp/" + path + "-" + field + ".png")
            tmp_path.parent.mkdir(parents=True, exist_ok=True)

            with open(tmp_path, "w") as f:
                doc = "\n".join(r)
                f.write(doc)

            call(["pdflatex", "-interaction", "nonstopmode", tmp_path.name], cwd=tmp_path.parent)


            convert_options=["-define", "png:compression-level=9", "-define", "png:compression-filter=2", "-define", "png:compression-strategy=1"]
            call(["montage", "-density", "600",  pdf_path, "-resize", "50%", "-tile", "1x",  "-geometry", "+1+5", "-background", "none"] + convert_options + [png_path])

            output_path = path + "-" + field + ".png"
            shutil.copyfile(png_path, "output/img/" + output_path)


            return "<img src='" + str(output_path) + "'/>"
        return ""
    return fn


