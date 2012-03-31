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

doconce format sphinx bioinf PRIMER_BOOK=False EBOOK=False --skip_inline_comments $main
doconce sphinx_dir author="H. P. Langtangen and G. K. Sandve" title="Illustrating Python via Examples from Bioinformatics" version=0.1 theme=pyramid $main
python automake-sphinx.py

doconce format pdflatex bioinf PRIMER_BOOK=False EBOOK=False --skip_inline_comments $main
ptex2tex -DMINTED $main
pdflatex $main
pdflatex $main

# Move
cp -r sphinx-rootdir/_build/html ../tutorial/
mv $main.pdf ../tutorial/bioinf-py.pdf
mv $main.html ../tutorial/bioinf-py.html



