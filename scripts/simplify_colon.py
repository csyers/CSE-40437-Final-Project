#!/usr/bin/env python

# simplify_colon.py - given a file of colon separated tweets, simply to the desired reduced json format
# March 14, 2017


import tweepy
import json
import sys
import os

def main():

    # check the number of arguments and exit if the wrong number was supplied
    if len(sys.argv) != 3:
        print("Usage: ./simplifier.py colon_separated_tweets.txt outfile.txt")
        exit(1)
    
    
    # get the arguments into variables
    tweet_file = sys.argv[1]
    outfile = sys.argv[2]

    print("=======================================================")
    print("Starting simplification of " + tweet_file)
    print("=======================================================")

    # load all the tweets from each of the input files into a single varaible 
    with open(tweet_file, 'r') as f:
        tweet_data = f.read()

    # split the string into a list of likely tweets
    split_on_date = tweet_data.split(sep='2017"\n')

    with open(outfile, 'w+') as f:
        for tweet in split_on_date:
            # split the likely tweet by ::
            separated = tweet.split(sep='::')
            # if there was 2017\n in place in the tweet of the text, it has to be skipped
            if len(separated) != 3:
                print("Skipping weird tweet")
            else:
                # write normal tweets in the right format
                tweet_json_limited = {}
                tweet_json_limited['text'] = separated[0][1:]
                tweet_json_limited['id'] = int(separated[1].replace(':',''))
                tweet_json_limited['created_at'] = separated[2] + '2017'
                json.dump(tweet_json_limited, f)
                f.write('\n')


if __name__ == '__main__':
    main()
