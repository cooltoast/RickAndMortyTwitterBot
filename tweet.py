#!/usr/bin/env python
import tweepy, time, sys
import json

data = open('keys.json')
keys = json.load(data)
data.close()

auth = tweepy.OAuthHandler(keys["consumer_key"], keys["consumer_secret"])
auth.set_access_token(keys["access_key"], keys["access_secret"])
api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
      print tweet.text
