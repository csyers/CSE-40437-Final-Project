#!/usr/bin/env python

# smoother.py - file that takes in a data set and smooths it according to a moving average smoothing algorithm.
#               The algorithm is taken from the following paper: http://www3.nd.edu/~dwang5/courses/spring17/papers/media-sensing/tweets-to-polls.pdf
# April 8, 2017

import json
import csv
import sys
import os
import re

def main():

    # check the number of arguments and exit if the wrong number was supplied
    if len(sys.argv) != 4:
        print("Usage: ./simplifier.py ratings.csv days_in_moving_average outfile.csv")
        exit(1)
    
    # get the arguments into variables
    ratings_csv = sys.argv[1]
    k = int(sys.argv[2])
    outfile_csv = sys.argv[3]

    # hold the ratings and lines in the following lists
    ratings = []
    lines = []

    # open the input file
    with open(ratings_csv, 'r') as f:
        reader = csv.reader(f)
        # hold the header line to put back into the output file
        header = next(reader);
        # get the ratings and the rest of the row
        for row in reader:
            ratings.append(float(row[1]))
            lines.append(row)

    # smooth the ratings
    ratings = smooth(ratings, k)

    # write the new information to the output file
    with open(outfile_csv,"w+") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i, line in enumerate(lines):
            line[1] = ratings[i]
            writer.writerow(line)

def smooth(ratings, k):
    '''
    smooth(ratings, k) - function that takes in a list of ratings and does a moving average smoothing
                         with k supplied by the second argument. Returns the new ratings
    '''
    for start_index, rating in enumerate(ratings):
        rating_sum = ratings[start_index]
        num_ratings = 1
        # get the index to start summing at, setting to 0 if there aren't k elements to sum
        end_index = start_index-k+1
        if end_index < 0:
            end_index = 0
        # sum the ratings
        while end_index < start_index:
            rating_sum += ratings[end_index]
            end_index += 1
            num_ratings += 1
        # calculate the smoothed ratings
        ratings[start_index] = rating_sum / num_ratings
    return ratings

if __name__ == '__main__':
    main()
