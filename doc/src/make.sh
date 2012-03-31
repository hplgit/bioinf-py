#!/bin/sh

main=wrap_bioinf

doconce format html $main

static=static-bioinf
rm -rf $static
mkdir $static

# Generate pygments versions of Python files
cd src-bioinf
pyg="pygmentize -f html -O full,style=emacs"
for file in *.py; do
  $pyg -o ../$static/$file.html -l python $file
done
cp *.py ../$static
cd ..

doconce format sphinx $main PRIMER_BOOK=False EBOOK=False --skip_inline_comments
rm -rf sphinx-rootdir
doconce sphinx_dir author="H. P. Langtangen and G. K. Sandve" title="Illustrating Python via Examples from Bioinformatics" version=0.9 theme=pyramid $main
python automake-sphinx.py
# Note: duplicate links warnings occur, but that is okay (we use the
# same repeated link text for local files)

doconce format pdflatex $main PRIMER_BOOK=False EBOOK=False --skip_inline_comments
ptex2tex -DMINTED $main
pdflatex -shell-escape $main
makeindex $main
pdflatex -shell-escape $main
pdflatex -shell-escape $main

# Move
cp -r sphinx-rootdir/_build/html ../tutorial/
cp $main.pdf ../tutorial/bioinf-py.pdf
cp $main.html ../tutorial/bioinf-py.html



