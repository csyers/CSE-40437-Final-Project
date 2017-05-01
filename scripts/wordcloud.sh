#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# get the file temp.txt to make the cloud out if
${DIR}/create_word_cloud_file.py $1

# execute the worldcloud_cli tool to create the file supplied in second argument
eval 'python2 ${DIR}/./wordcloud_cli.py --imagefile $2 --text temp.txt --background "rgb(255,255,255)" --no_collocations'

# remove the temporary file
rm temp.txt
