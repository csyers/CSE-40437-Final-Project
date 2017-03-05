#!/usr/bin/env python

# analyzer.py - does sentiment analysis on a file of json tweets
# March 4, 2017


import tweepy
import json
import sys
import os
import getopt
def sentiment(tweet_file):
    print("sentiment")
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
