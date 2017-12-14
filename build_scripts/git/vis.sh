
out=/tmp/vis_git/
mkdir -p $out

python3 build_scripts/git/vis_git.py $@ > $out/test.tex

(cd $out;
pdflatex -interaction nonstopmode test.tex
)

