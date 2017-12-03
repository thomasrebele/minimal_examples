
out=/home/tr/projects/anki/minimal-git-examples/test/

python3 /home/tr/projects/anki/minimal-git-examples/vis_git.py $@ > $out/test.tex

(cd $out;
pdflatex -interaction nonstopmode test.tex
)

