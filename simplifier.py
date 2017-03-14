#!/usr/bin/env python

# simplifier.py - given a file of JSON tweets, it simplifies it to the reduced form size with tweet id, text, and timestamp
# March 14, 2017


import tweepy
import json
import sys
import os

def main():

    # check the number of arguments and exit if the wrong number was supplied
    if len(sys.argv) != 3:
        print("Usage: ./simplifier.py full_json_tweets.json outfile.txt")
        exit(1)
    
    # get the arguments into variables
    json_file = sys.argv[1]
    outfile = sys.argv[2]

    # load all the tweets from each of the input files into a list
    tweets = [json.loads(line) for line in open(json_file)]

    # get a list of the simplified format
    tweets_simplified = [tweet['text'].replace('\n',' ') + "::" + str(tweet['id']) + "::" + tweet['created_at'] for tweet in tweets]

    # write each tweet to the file specified in the second argument
    with open(outfile, 'w+') as f:
        for tweet_simplified in tweets_simplified:
            f.write(tweet_simplified + '\n')

if __name__ == '__main__':
    main()
