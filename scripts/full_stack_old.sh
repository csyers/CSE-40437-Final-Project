#!/usr/bin/env bash


keyword=$1
start_date=$2 
end_date=$3
outfile=${keyword// /_}
tweet_outfile="${outfile}.json"
csv_outfile="${outfile}.csv"
wordcloud_outfile="${outfile}.png"

eval "python3 ./get_old_tweets.py \"${keyword}\" $start_date $end_date ../data/$tweet_outfile"
eval "python2 ./analyzer.py ../data/$tweet_outfile ../results/$csv_outfile"
eval "./wordcloud.sh ../results/$csv_outfile ../images/$wordcloud_outfile"
