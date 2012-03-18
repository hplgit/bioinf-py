#!/bin/sh
doconce format latex bioinf PRIMER_BOOK=True EBOOK=False --skip_inline_comments

doconce replace Section Chapter bioinf.p.tex
doconce replace bpycod bcod bioinf.p.tex
doconce replace epycod ecod bioinf.p.tex
doconce replace bpypro bpro bioinf.p.tex
doconce replace epypro epro bioinf.p.tex
doconce replace 'figs-bioinf/' 'figs/' bioinf.p.tex

# not ebook:
doconce replace '\href' '\myhref' bioinf.p.tex

# Grab regions
doconce grab --from 'Mixing Loops,' --to- 'Examples from Analyzing DNA' bioinf.p.tex > bioinf_ch3.p.tex

doconce grab --from 'Examples from Analyzing DNA' --to- 'Dot Plots from Pair of DNA' bioinf.p.tex > bioinf_ch6.p.tex

doconce grab --from 'Finding Base Frequencies' --to- 'Random Mutations of Genes' bioinf.p.tex >> bioinf_ch6.p.tex

doconce grab --from 'Random Mutations of Genes' --to- 'Classes for DNA' bioinf.p.tex > bioinf_ch8.p.tex

doconce grab --from 'Classes for DNA' --to- '\{Exercises\}' bioinf.p.tex > bioinf_ch9.p.tex

# Exercises too
doconce grab --from 'Find pairs of' --to- 'Allow different types' bioinf.p.tex > bioinf_ch3_ex.p.tex

doconce grab --from 'Allow different types'  --to- 'Speed up Markov chain mutation' bioinf.p.tex > bioinf_ch6_ex.p.tex

doconce grab --from 'Speed up Markov chain mutation' --to- Acknowledgment bioinf.p.tex > bioinf_ch8_ex.p.tex
