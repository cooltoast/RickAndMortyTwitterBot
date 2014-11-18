#!/usr/bin/python
import tweepy, time, sys
import json
import requests
import random
import time
from quotes import getQuotes

def tweetQuote():
  data = open('keys.json')
  keys = json.load(data)
  data.close()

  auth = tweepy.OAuthHandler(keys["consumer_key"], keys["consumer_secret"])
  auth.set_access_token(keys["access_key"], keys["access_secret"])
  api = tweepy.API(auth)

  quotes = getQuotes()
  quote = random.choice(quotes)
  print "tweeted: %s" % quote
  api.update_status(quote)


if __name__ == '__main__':
  while(1):
    try:
      tweetQuote()
    except tweepy.TweepError: # dont stop when duplicate status happens
      continue
    # tweet again in 20 min
    time.sleep(60*20)

