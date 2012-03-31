#!/bin/sh
cd src-bioinf
sh clean.sh
cd ..

doconce clean
rm -rf *_ch*.p.tex _static* automake-sphinx.py .*.exerinfo

