#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

keyword=$1
start_date=$2 
end_date=$3
outfile=${keyword// /_}
tweet_outfile="${outfile}.json"
csv_outfile="${outfile}.csv"
wordcloud_outfile="${outfile}.png"

eval "python3 ${DIR}/get_old_tweets.py \"${keyword}\" $start_date $end_date ${DIR}/../data/$tweet_outfile"
eval "python2 ${DIR}./analyzer.py ${DIR}../data/$tweet_outfile ${DIR}/../results/$csv_outfile"
eval "${DIR}./wordcloud.sh ${DIR}../results/$csv_outfile ${DIR}../images/$wordcloud_outfile"
