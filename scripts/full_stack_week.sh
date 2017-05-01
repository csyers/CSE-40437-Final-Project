#!/usr/bin/env bash


keyword=$1
outfile=${keyword// /_}
tweet_outfile="${outfile}.json"
csv_outfile="${outfile}.csv"
wordcloud_outfile="${outfile}.png"

eval "python3 ./get_week_tweets.py \"${keyword}\" ../data/$tweet_outfile"
eval "python2 ./analyzer.py ../data/$tweet_outfile ../results/$csv_outfile"
eval "./wordcloud.sh ../results/$csv_outfile ../images/$wordcloud_outfile"
