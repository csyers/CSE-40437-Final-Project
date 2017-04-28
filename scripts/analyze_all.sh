#! /usr/bin/env bash

for f in ../data/*; do
    O="$(basename $f)"
    Z=${O%.json}
    eval "python2 analyzer.py $f ../results/${Z}.csv"
done

for f in ../data/*; do
    O="$(basename $f)"
    Z=${O%.json}
    eval "./wordcloud.sh ../results/${Z}.csv ../images/${Z}.png"
done
