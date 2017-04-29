#! /usr/bin/env bash

for f in ../data/*; do
    O="$(basename $f)"
    Z=${O%.json}
    echo "python2 analyzer.py $f ../results/${Z}.csv"
done

for f in ../data/*; do
    O="$(basename $f)"
    Z=${O%.json}
    echo "./wordcloud.sh ../results/${Z}.csv ../images/${Z}.png"
done
