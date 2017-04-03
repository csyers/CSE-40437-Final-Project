#!/usr/bin/env python

# frequent_words.py - analyzes the frequency of certain words in a list of tweets
# April 2, 2017

import csv
import datetime
import tweepy
import json
import sys
import os
import getopt

def frequent_words(tweet_file):
    '''
    frequent_words: function that takes in a list of tweets and returns the ten most frequent adjectives in the corpus
    '''
    return 1

def main():
    # check the number of arguments and exit if the wrong number was supplied
    if len(sys.argv) != 2:
        print("Usage: frequent_words.py path/to/tweet/file.json")
        exit(1)

    # get the arguments into variables
    tweet_file = sys.argv[1]

    # load the file into a list of tweets
    tweets = [json.loads(line) for line in open(tweet_file)]

    # analyze the frequency of words in the tweet file
    print(frequent_words(tweet_file))

if __name__ == '__main__':
    main()
