#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

keyword=$1
outfile=${keyword// /_}
tweet_outfile="${outfile}.json"
csv_outfile="${outfile}.csv"
wordcloud_outfile="${outfile}.png"

eval "python3 ${DIR}/get_week_tweets.py \"${keyword}\" ${DIR}/../data/$tweet_outfile"
eval "python2 ${DIR}./analyzer.py ${DIR}../data/$tweet_outfile ${DIR}/../results/$csv_outfile"
eval "${DIR}./wordcloud.sh ${DIR}../results/$csv_outfile ${DIR}../images/$wordcloud_outfile"
