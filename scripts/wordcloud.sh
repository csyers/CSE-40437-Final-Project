#!/usr/bin/env bash

./create_word_cloud.py $1 $2

eval 'python2 ./wordcloud_cli.py --imagefile $2 --text temp.txt --background "rgb(255,255,255)"'

#rm temp.txt
