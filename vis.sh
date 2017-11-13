
dir=$1
out=/home/tr/projects/anki/minimal-git-examples/test/

python3 /home/tr/projects/anki/minimal-git-examples/vis-git.py $dir > $out/test.tex

(cd $out;
pdflatex -interaction nonstopmode test.tex
)

