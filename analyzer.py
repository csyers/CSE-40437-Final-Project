#!/usr/bin/env python

# analyzer.py - does sentiment analysis on a file of json tweets
# March 4, 2017

import datetime
import tweepy
import json
import sys
import os
import getopt

sentiment_analysis_file = "sentiment_analysis/AFINN/AFINN-111.txt"

def initialize_sentiment_dict():
    '''
    initialize_sentiment_dict: function that creates a mapping from word to sentiment score
    used to get the overall sentiment score of a given tweet
    '''
    sentiment_scores = {}
    lines = [line.split() for line in open(sentiment_analysis_file)]
    for line in lines:
        sentiment_scores[line[0]] = line[1]
    return sentiment_scores

def separate_tweets_by_day(tweets):
    '''
    separate_tweets_by_day: function that given a list of tweets, returns a dictionary that maps from dates to tweets on that day
    used to get the rating score of a single day
    '''
    tweets_by_day = {}
    for tweet in tweets:
        date_object = proper_date = datetime.datetime.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y').date()
        if date_object in tweets_by_day:
            tweets_by_day[date_object].append(tweet)
        else:
            tweets_by_day[date_object] = []
            tweets_by_day[date_object].append(tweet)
    return tweets_by_day

def sentiment(tweet_file):
    scores = initialize_sentiment_dict()
    tweets = [json.loads(line) for line in open(tweet_file)]
    tweets_by_day = separate_tweets_by_day(tweets)
    
    
def opinion_and_sentiment(tweet_file):
    print("opiniot")

def main():
    # get the option flags from the command line
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'sbh')
    except getopt.GetoptError:
        print("Usage: ./analyzer.py [option] tweets.json")
        exit(1)
    # if there were more than one option flag or more than one additional agrument, exit
    if len(opts) != 1 or len(args) != 1:
        print("Usage: ./analyzer.py [option] tweets.json")
        exit(1)
    # get the option
    opt = opts[0][0]
    # help option
    if opt == '-h':
        print("Usage: ./analyzer.py [option] tweets.json")
        exit(0)
    # sentiment analysis only option
    elif opt == '-s':
        sentiment(args[0])
    # both opinion analysis and sentiment analysis
    elif opt == '-b':
        opinion_and_sentiment(args[0])
    # unkown option
    else:  
        print("Error: bad option.")
        exit(1)

if __name__ == '__main__':
    main()
