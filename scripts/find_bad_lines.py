#!/usr/bin/env python

# find_bad_lines.py - given a json file, print all the lines that are not valid json.
# April 26, 2017

import tweepy
import json
import sys
import os

def main():
    # check the number of arguments and exit if the wrong number was supplied
    if len(sys.argv) != 2:
        print("Usage: find_bad_lines.py tweets.json")
        exit(1)
    
    # get the arguments into variables
    path1 = sys.argv[1]

    # load all the tweets from each of the input files into a list
    count = 0
    bad_line = []

    # open the file and try to load each line, store line number in array
    with open(path1) as f:
        for line in f:
            try:
                count += 1
                tweet = json.loads(line)
            except ValueError:
                bad_line.append(count)
    print(bad_line)
        
if __name__ == '__main__':
    main()
