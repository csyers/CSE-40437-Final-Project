#!/usr/bin/env python

# create_word_cloud.py - given a ratings file, creates a file for wordcloud to create an image out of, called temp.txt
# April 19, 2017

import json
import csv
import sys

def main():

    # check the number of arguments and exit if the wrong number was supplied
    if len(sys.argv) != 2:
        print("Usage: ./creat_word_cloud.py ratings.csv")
        exit(1)
    
    # get the arguments into variables
    ratings_csv = sys.argv[1]

    # hold the ratings and lines in the following lists
    adjectives = []

    # open the input file
    with open(ratings_csv, 'r') as f:
        reader = csv.reader(f)
        # hold the header line to put back into the output file
        header = next(reader);
        # get the ratings and the rest of the row
        for row in reader:
            json_string = row[3].replace("'","\"")
            json_string = json_string.replace("u\"","\"")
            d = json.loads(json_string)
            adjectives.append(d)
    count = 0
    with open("temp.txt","w") as f:
        for adjective in adjectives:
            for word in adjective:
                for i in range(adjective[word]):
                    f.write(word + ' ' + str(count) + ' \n')
                    count += 1

if __name__ == '__main__':
    main()
