
dir=$1
out=/home/tr/projects/anki/minimal-git-examples/test/

(ps a | grep -v "grep" | grep -e "evince .*test.pdf" || evince $out/test.pdf &)&

python3 /home/tr/projects/anki/minimal-git-examples/vis-git.py $dir > $out/test.tex

(cd $out;
pdflatex -interaction nonstopmode test.tex
)

