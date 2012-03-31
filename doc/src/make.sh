#!/bin/sh

rm -rf _static
mkdir _static

# Generate pygments versions of Python files
cd src-bioinf
pyg="pygmentize -f html -O full,style=emacs"
for file in *.py; do
  $pyg -o ../_static/$file.html -l python $file
done
cd ..

doconce format sphinx wrap_bioinf
doconce sphinx_dir author="H. P. Langtangen and G. K. Sandve" title="Illustrating Python via Examples from Bioinformatics" version=0.1 theme=pyramid wrap_bioinf

