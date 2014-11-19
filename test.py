import unittest
import quotes as QuoteModule
import tweet as TweetModule

def testTweetEmpty():
  QuoteModule.getQuotes = lambda: []
  assert not TweetModule.tweetQuote()

def testTweetObject():
  obj = object()
  QuoteModule.getQuotes = lambda: [obj]
  # object wont get tweeted, but loop continues to True
  assert TweetModule.tweetQuote()

def runTests():
  testTweetEmpty()
  testTweetObject()

if __name__ == '__main__':
  runTests()
  print 'all tests ran, nice'
