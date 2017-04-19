#!/usr/bin/env bash

# get the file temp.txt to make the cloud out if
./create_word_cloud_file.py $1

# execute the worldcloud_cli tool to create the file supplied in second argument
eval 'python2 ./wordcloud_cli.py --imagefile $2 --text temp.txt --background "rgb(255,255,255)" --no_collocations'

# remove the temporary file
rm temp.txt
