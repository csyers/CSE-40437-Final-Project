#!/usr/bin/env python

# simplify_json.py - given a file of JSON tweets, it simplifies it to the reduced form size with tweet id, text, and timestamp
# March 14, 2017

import ast
import tweepy
import json
import sys
import os
import re

def main():

    # check the number of arguments and exit if the wrong number was supplied
    if len(sys.argv) != 4:
        print("Usage: ./simplifier.py full_json_tweets.json outfile.txt next_field")
        exit(1)
    
    # get the arguments into variables
    json_file = sys.argv[1]
    outfile = sys.argv[2]
    next_field = sys.argv[3]

    print("=======================================================")
    print("Starting simplification of " + json_file)
    print("=======================================================")

    # load all the tweets from each of the input files into a list
    tweets = [line for line in open(json_file)]
    
   # write each tweet to the file specified in the second argument
    with open(outfile, 'w+') as f:
        print(next_field)
        for tweet in tweets:
            text_result = re.search("\"text\": (.*?), \"" + next_field,tweet)
            id_result = re.search("\"id\": (..................)",tweet)
            created_at_result = re.search("(... Mar .. ..:..:.. \+0000 2017)",tweet)
            if created_at_result and text_result and id_result:
                tweet_json_limited = {}
                tweet_json_limited['text'] = text_result.group(1)[1:-1]
                tweet_json_limited['id'] = int(id_result.group(1))
                tweet_json_limited['created_at'] = created_at_result.group(1)
                json.dump(tweet_json_limited, f)
                f.write('\n')
            else:
                print("Skipping weird tweet")


if __name__ == '__main__':
    main()
