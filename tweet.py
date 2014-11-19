#!/usr/bin/python
import tweepy, time, sys
import json
import requests
import random
import time
import quotes as QuoteModule

def tweetQuote():
  data = open('keys.json')
  keys = json.load(data)
  data.close()

  auth = tweepy.OAuthHandler(keys["consumer_key"], keys["consumer_secret"])
  auth.set_access_token(keys["access_key"], keys["access_secret"])
  api = tweepy.API(auth)

  quotes = QuoteModule.getQuotes()
  if not quotes:
    return False

  while (len(quotes) > 0):
    quote = quotes.pop(random.randint(0, len(quotes)-1))

    if type(quote) is not str:
      continue

    try:
      api.update_status(quote)
      print "tweeted: %s" % quote
    except tweepy.TweepError:
      # dont stop if duplicate status happens
      continue

    # tweet again in 20 min
    time.sleep(60*20)

  return True

if __name__ == '__main__':
  tweetQuote()

