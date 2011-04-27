#!/bin/bash

export TEXINPUTS="${HOME}/texmf:`pwd`/chapter1//:`pwd`/chapter2//:`pwd`/chapter3//:`pwd`/chapter4//:`pwd`:"
export BIBINPUTS="${HOME}/texmf/bibtex:`pwd`/chapter1//:`pwd`/chapter2//:`pwd`/chapter3//:`pwd`/chapter4//:"
export BSTINPUTS="${HOME}/texmf/bibtex:"

#TEX_CMD='latex -output-format=dvi'
TEX_CMD='pdflatex'
TEX_OPTS="-output-directory=output -halt-on-error \
-file-line-error -no-shell-escape"

if [[ "$1" == "clean" ]]; then
    find output/ -type f -exec rm "{}" \;
elif [[ "$1" == "log" ]]; then
    ${PAGER} output/thesis.log
elif [[ "$1" == "nag" ]]; then
    grep 'Package nag' output/thesis.log
else
    ${TEX_CMD} ${TEX_OPTS} thesis.tex || exit 1
#    (cd output && bibtex thesis) || exit 1
    ${TEX_CMD} ${TEX_OPTS} thesis.tex || exit 1
    ${TEX_CMD} ${TEX_OPTS} thesis.tex || exit 1
fi
