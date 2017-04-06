#!/usr/bin/env python

# analyzer.py - does sentiment analysis on a file of json tweets
# March 4, 2017

import csv
import datetime
import tweepy
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8') #allows for emoji support
import os
import getopt
import frequent_words
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# file to compare words to
sentiment_analysis_file = os.path.dirname(sys.path[0]) + os.sep + "sentiment_analysis/AFINN/AFINN-111.txt"

# number of adjectives to track
num_adjectives = 3

# rating values: 0 - scale
scale = 10

def analyzeSentimentVader(tweet_file):
    sentiment_score = {}
    tweets = [json.loads(line) for line in open(tweet_file)]
    analyzer = SentimentIntensityAnalyzer()
    for tweet in tweets:
        vs = analyzer.polarity_scores(tweet["text"])
        sentiment_score[tweet["text"]] = vs["compound"] #this gives the compound feeling score on a scale of -1 to +1
    return sentiment_score

def clean_text(tweets):
    whitelist = set('abcdefghijklmnopqrstuvwxy \'1234567890')
    clean_tweets = []
    for tweet in tweets:
        cleaned = ''.join(filter(whitelist.__contains__, tweet['text'].lower()))
        tweet['text'] = cleaned
        clean_tweets.append(tweet)
    return clean_tweets

def initialize_sentiment_dict():
    '''
    initialize_sentiment_dict: function that creates a mapping from word to sentiment score
    used to get the overall sentiment score of a given tweet
    '''
    sentiment_scores = {}
    # get a list of all the words in each line of the sentiment analysis file
    lines = [line.split() for line in open(sentiment_analysis_file)]

    # for every line
    for line in lines:
        # case: single word
        if len(line) == 2:
            sentiment_scores[line[0]] = int(line[1])
        # case: more than one word phrase
        else:
            # reconstruct the phrase
            phrase = line[0]
            for i in range(len(line)-2):
                phrase += " " + line[i+1]
            sentiment_scores[phrase] = int(line[len(line)-1])
    
    # return the dictionary of words/phrases --> sentiment score
    return sentiment_scores

def separate_tweets_by_day(tweets):
    '''
    separate_tweets_by_day: function that given a list of tweets, returns a dictionary that maps from dates to tweets on that day
    used to get the rating score of a single day
    '''
    tweets_by_day = {}
    # for every tweet
    for tweet in tweets:
        # get the date object of the tweet
        date_object = datetime.datetime.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y').date()
        # if the date object is already in the dictionary, append the tweet to the key
        if date_object in tweets_by_day:
            tweets_by_day[date_object].append(tweet)
        # date object isn't in the dictionary yet
        else:
            # add the key and append the tweet
            tweets_by_day[date_object] = []
            tweets_by_day[date_object].append(tweet)
    
    count_by_day = {}
    for date in tweets_by_day:
        count_by_day[date] = len(tweets_by_day[date])
    # return the dictionary of date objects --> list of tweets
    return tweets_by_day, count_by_day

def get_ratings(tweets_by_day, scores):
    '''
    get_ratings: function that gets the average product rating of the a set of tweets associated with a
    date. Returns a map from date --> rating from 0 to 1
    '''
    ratings_by_day = {}
    # for every key in the dictionary
    for date in tweets_by_day:
        # populate the dictionary with the average rating
        ratings_by_day[date] = get_average_rating(tweets_by_day[date], scores)
    return ratings_by_day

def get_average_rating(list_of_tweets, scores):
    '''
    get_average_rating: function that gets the average rating of a day's tweets by adding up the compound scores for each tweet and diving by the number of tweets from that day
    '''
    score = 0
    numTweets = 0
    for tweet in list_of_tweets:
        numTweets += 1
        score += scores[tweet["text"]]

    return float(score)/numTweets

    '''
    get_average_rating: function that gets the average rating of a list of tweets by counting the positive,
    negative, and neutral tweets in the list
    '''
    # positive = 0
    # negative = 0
    # neutral = 0

    # # for each tweet, get the score and increment the proper counter
    # for tweet in list_of_tweets:
    #     score = get_score(tweet['text'], scores)
    #     if score > 0:
    #         positive += 1
    #     elif score < 0:
    #         negative += 1
    #     else:
    #         neutral += 1

    # # return the percentage of tweets that is positive
    # return float(positive)/len(list_of_tweets)

def get_score(tweet_text, scores):
    '''
    get_score: function that scores a given tweet_text based on scores in the scores dictionary. The score is a 
    summation of the scores for each word
    '''
    score = 0

    # make the tweet text lower case
    lower_text = tweet_text.lower()
    for word in scores:
        if word in lower_text:
            # increment the score by the value of the word/phrase
            score += scores[word]

    # return the score
    return score

def write_csv(ratings_by_day, count_by_day, frequent_words_by_day, outfile):
    '''
    write_csv: function that takes in the dictionary of ratings on a given day and writes outfile to be csv format
    '''
    with open(outfile,"w+") as f:
        writer = csv.writer(f)
        # write the header line
        writer.writerow(("date","rating","count","frequent words"))
    
        # for every element in the dictionary, sorted, write the information out
        for date in sorted(ratings_by_day.keys()):
            writer.writerow((date.strftime('%m/%d/%Y'),ratings_by_day[date]*scale,count_by_day[date],frequent_words_by_day[date]))

def get_frequent_words(tweets_by_day):
    '''
    get_frequent_words: function that takes in a dictionary of tweets on a day and envokes 
    frequent_words.frequent_words to get the ten most used adjevtives in the corpus. Returns a
    dictionary that maps from date --> list of most frequent words
    '''
    frequent_words_by_day = {}
    for date in tweets_by_day:
        frequent_words_by_day[date] = frequent_words.most_frequent_n_adjectives(tweets_by_day[date],num_adjectives)

    # return the dictionary
    return frequent_words_by_day

def sentiment(tweet_file, outfile):
    '''
    sentiment: function that computes the daily rating of a set of tweets and writes them to the outfile
    '''
    # get the dictionary of sentiment scores
    #scores = initialize_sentiment_dict()
    scores = analyzeSentimentVader(tweet_file)
    # load the tweets from the json file
    tweets = [json.loads(line) for line in open(tweet_file)]
    # get a mapping of dates --> list of tweets on that date
    tweets_by_day, count_by_day = separate_tweets_by_day(tweets)
    # get a mapping of dates --> rating of tweets on that date
    ratings_by_day = get_ratings(tweets_by_day, scores)
    # clean the tweet text to make lowercase, remove punctuation
    tweets = clean_text(tweets)
    # get the ten most frequent words on each day for the tweets
    frequent_words_by_day = get_frequent_words(tweets_by_day)
    # write the information to a csv file
    write_csv(ratings_by_day, count_by_day, frequent_words_by_day, outfile)

def main():
    # check the number of arguments and exit if the wrong number was supplied
    if len(sys.argv) != 3:
        print("Usage: analyzer.py path/to/tweet/file.json path/to/output/file.csv")
        exit(1)

    # get the arguments into variables
    tweet_file = sys.argv[1]
    outfile = sys.argv[2]

    # start the sentiment analysis
    sentiment(tweet_file, outfile)

if __name__ == '__main__':
    main()
