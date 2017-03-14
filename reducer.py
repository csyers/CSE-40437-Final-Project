#!/usr/bin/env python

# reducer.py - given two files of JSON tweets, get the ones common to both and output to a given filename
# February 27, 2017


import tweepy
import json
import sys
import os

def main():

    # check the number of arguments and exit if the wrong number was supplied
    if len(sys.argv) != 4:
        print("Please specifiy exactly two files to reduce and an output file. Usage: ./reducer.py path/to/tweet/file1.json path/to/tweet/file2.json path/to/output/file.json")
        exit(1)
    
    # get the arguments into variables
    path1 = sys.argv[1]
    path2 = sys.argv[2]
    outfile = sys.argv[3]

    # load all the tweets from each of the input files into a list
    tweets1 = [line for line in open(path1)]
    tweets2 = [line for line in open(path2)]

    # get a list of all ids from the first list of tweets
    tweet1_ids = [int(line.split("::")[1]) for line in tweets1]

    # get a list of all ids from the second list of tweets
    tweet2_ids = [int(line.split("::")[1]) for line in tweets2]
       
    # get a list of the ids common to both set of tweets
    common_ids = list(set(tweet1_ids).intersection(tweet2_ids))

    # get the dictionaries for each tweet
    common_tweets = [tweet for tweet in tweets1 if int(tweet.split("::")[1]) in common_ids]

    # write each common tweet to the file specified in the third argument
    with open(outfile, 'w+') as f:
        for common_tweet in common_tweets:
            f.write(common_tweet)

if __name__ == '__main__':
    main()
