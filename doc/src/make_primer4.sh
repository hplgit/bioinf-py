#!/bin/sh

rm -rf __tmp.do.txt
doconce spellcheck -d .dict4spell.txt *.do.txt
if [ $? -ne 0 ]; then
  echo "Misspellings!"  # use mydict.txt~.all~ as new dictionary.txt?
  exit 1
fi

#doconce format latex bioinf PRIMER_BOOK=True EBOOK=False --skip_inline_comments
# things are written with mako, EBOOK and PRIMER_BOOK as mako var...but it will work in mako I think

# Grab regions
doconce grab --from 'Mixing Loops,' --to- 'Examples from Analyzing DNA' bioinf.p.tex > bioinf_ch3.p.tex

doconce grab --from 'Examples from Analyzing DNA' --to- 'Dot Plots from Pair of DNA' bioinf.p.tex > bioinf_ch6.p.tex

doconce grab --from 'Finding Base Frequencies' --to- 'Random Mutations of Genes' bioinf.p.tex >> bioinf_ch6.p.tex

doconce grab --from 'Random Mutations of Genes' --to- 'Classes for DNA' bioinf.p.tex > bioinf_ch8.p.tex

doconce grab --from 'Classes for DNA' --to- 'Acknowledgments.' bioinf.p.tex > bioinf_ch9.p.tex

# Exercises too
doconce grab --from 'Find pairs of' --to- 'Allow different types' bioinf.p.tex > bioinf_ch3_ex.p.tex

doconce grab --from 'Allow different types'  --to- 'Speed up Markov chain mutation' bioinf.p.tex > bioinf_ch6_ex.p.tex

doconce grab --from 'Speed up Markov chain mutation' --to- 'Extend the constructor in class Gene' Acknowledgment bioinf.p.tex > bioinf_ch8_ex.p.tex

# drop exer for class.do.txt

# Modify exercises
for file in bioinf_ch*_ex.p.tex; do
doconce subst '\\subsection\{' '\\begin{exercise}\n\\exerentry{' $file
doconce subst '\\emph\{Filename\}: \\code\{(.+?)\}\.' 'Name of program file: \\code{\g<1>}.\n' $file
doconce subst '% --- end of exercise' '\\hfill $\\diamond$\n\\end{exercise}' $file
done

