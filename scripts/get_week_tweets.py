#!/usr/bin/env python

# crawler.py - given a series of keywords, start a stream for each and collect tweets with those keywords
# February 27, 2017

import tweepy
import json
import sys
import os

data_path = "data/"

class KeywordCrawler(tweepy.StreamListener):

    def set_keywords(self, keywords):
        # self.keywords is a list of keywords to search for
        # self.count is used for printing status
        self.keywords = keywords
        self.count = 0

    def on_status(self, tweet):
        # increment count and display characters based on the count
        self.count += 1
        if self.count % 1000 == 0:
            self.count = 0
            sys.stdout.write('+')
            sys.stdout.flush()
        elif self.count % 100 == 0:
            sys.stdout.write('.')
            sys.stdout.flush()

        # get the json version of the tweet
        tweet_json = json.dumps(tweet._json)
        tweet_json = json.loads(tweet_json)
        
        # for every word in the tweet that matches the keyword list, write to that json file
        for word in self.keywords:
            if word in tweet_json['text'].lower():
                tweet_json_limited = {}
                tweet_json_limited['text'] = tweet_json['text']
                tweet_json_limited['id'] = tweet_json['id']
                tweet_json_limited['created_at'] = tweet_json['created_at']
                self.write_tweet_to_file(word,tweet_json_limited)

        return True
    
    def write_tweet_to_file(self,word,tweet):
        # write the json dump to the file
        destination_file = data_path + word + ".json"
        with open(destination_file, 'a+') as f:
            json.dump(tweet, f)
            f.write('\n')
            
            

def main():
    
    # check arguments
    if len(sys.argv) != 3:
        print("Please specify at least one keyword. Usage: ./get_week_tweets.py keyword1 output.json")
        exit(1)

    # keys and access tokens
    consumer_key = "5JlX6y9wOCIdeHpKbSaIlxnO3"
    consumer_secret = "LwkmtQ0pxzswrxzwBTGMEmnscbqQmndGCKW1BcQyAWUZqddmHJ"

    access_token = "481726305-oWB5IAO02uvfCuqMUQk15PDvd2xGJsN7p9ohyIEQ"
    access_token_secret = "HDeeh7giVDGpdaGVQqnmplXbabr2oM2FJU1HyIqmuEmpo"

    # set up authorization
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # retrieve the api object
    api = tweepy.API(auth)

    tweets = [status for status in tweepy.Cursor(api.search, q=sys.argv[1], since = "2017-04-23", until = "2017-05-01", lang = "en", count=100).items()]    

    lim_tweets = []

    for tweet in tweets:
        tweet_json = json.dumps(tweet._json)
        tweet_json = json.loads(tweet_json)

        tweet_json_limited = {}
        tweet_json_limited['text'] = tweet_json['text'].encode('utf-8')
        tweet_json_limited['id'] = tweet_json['id']
        tweet_json_limited['created_at'] = tweet_json['created_at']
        lim_tweets.append(tweet_json_limited)
    
    with open(sys.argv[2],'a+') as f:
        for tweet in lim_tweets:
            json.dump(tweet,f)
            f.write('\n')
        

   
if __name__ == '__main__':
    main()
