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
import operator
import nltk
import analyzer

def most_frequent_n_adjectives(tweets, n):
    '''
    most_frequent_n_adjectives: returns a list of the n most used adjectives in the tweets and their counts
    '''
    # dictionary variables to populate, count variable to stop the loop
    adjective_frequencies = {}
    top_frequencies = {}
    count = 0

    # tags used by nltk to mark adjectives
    adj_tags = ["JJ","JJR","JJS"]

    # for every tweets
    for tweet in tweets:
        # break the tweet into words
        words = nltk.word_tokenize(tweet['text'])   
        # tag the words with their part of speech
        tagged_words = nltk.pos_tag(words)
        # for every tagged word
        for pair in tagged_words:
            # if the tag is an adjective
            if pair[1] in adj_tags:
                # increment the dictionary of all of the frequencies
                if pair[0] in adjective_frequencies:
                    adjective_frequencies[pair[0]] += 1
                else:
                    adjective_frequencies[pair[0]] = 1
    # iterate through the dictionary to get the n most frequent adjectives, store them in top_frequencies
    for key,value in sorted(adjective_frequencies.items(), key = operator.itemgetter(1), reverse=True):
        if count == n:
            break
        count += 1
        top_frequencies[key] = value
    # return the top n frequent adjectives
    return top_frequencies

def main():
    # check the number of arguments and exit if the wrong number was supplied
    if len(sys.argv) != 3:
        print("Usage: frequent_words.py path/to/tweet/file.json num_adjectives")
        exit(1)

    # get the arguments into variables
    tweet_file = sys.argv[1]

    # load the file into a list of tweets
    tweets = [json.loads(line) for line in open(tweet_file)]
    
    tweets = analyzer.clean_text(tweets)
    # analyze the frequency of words in the tweet file
    print(most_frequent_n_adjectives(tweets, 10))

if __name__ == '__main__':
    main()
