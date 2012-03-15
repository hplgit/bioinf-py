#!/bin/sh
doconce format latex bioinf PRIMER_BOOK=True EBOOK=False

doconce replace Section Chapter bioinf.p.tex
doconce replace bpycod bcod bioinf.p.tex
doconce replace epycod ecod bioinf.p.tex
doconce replace bpypro bpro bioinf.p.tex
doconce replace epypro epro bioinf.p.tex

# Grab regions
doconce grab --from 'Mixing Loops,' --to- 'Examples from Analyzing DNA' bioinf.p.tex > bioinf_ch3.p.tex
doconce grab --from 'Examples from Analyzing DNA' --to- 'Dot Plots from Pair of DNA' bioinf.p.tex > bioinf_ch6.p.tex
doconce grab --from 'Finding Base Frequencies' --to- 'Random Mutation of Genes' bioinf.p.tex >> bioinf_ch6.p.tex

doconce grab --from 'Random Mutation of Genes' --to- 'Classes for DNA' bioinf.p.tex > bioinf_ch8.p.tex

doconce grab --from 'Classes for DNA' --to- 'Exercises' bioinf.p.tex > bioinf_ch9.p.tex

# Exercises too
