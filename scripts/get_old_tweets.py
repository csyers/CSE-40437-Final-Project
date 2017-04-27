#!/usr/bin/env python

# get_old_tweets.py - given a keyword, retrieves a lot of old tweets containing that keyword
# Apirl 9, 2017

import os
import sys
import got3
import json
from datetime import timedelta, date, datetime

def main():
    
    # exit if used incorrectly
    if len(sys.argv) != 5:
        print("Usage: get_old_tweets.py keyword since_date until_date outfile.json")
        exit(1)
    
    # store input parameters
    keyword = sys.argv[1]
    since_date = sys.argv[2]
    until_date = sys.argv[3]
    outfile = sys.argv[4]

    # get the list of tweets that follow the criteria
    tweetCriteria = got3.manager.TweetCriteria().setQuerySearch(keyword).setSince(since_date).setUntil(until_date)
    tweets = got3.manager.TweetManager.getTweets(tweetCriteria)

    # write the tweets to a file in the proper format
    with open(outfile, 'a+') as f:
        for tweet in tweets:
            tweet_json_limited = {}
            tweet_json_limited['text'] = tweet.text
            tweet_json_limited['id'] = int(tweet.id)
            tweet_json_limited['retweets'] = int(tweet.retweets)
            date_string = tweet.date.strftime("%a %b %d %X +0000 %Y")
            tweet_json_limited['created_at'] = date_string
            json.dump(tweet_json_limited, f)
            f.write('\n')

if __name__ == '__main__':
    main()
