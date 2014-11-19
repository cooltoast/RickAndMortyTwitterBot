import requests
import os
import pickle
from bs4 import BeautifulSoup
from cleanup import cleanUp

def generateQuotes():
  re = requests.get('http://www.rickandmortytime.com/wiki/Quotes')
  soup = BeautifulSoup(re.content)
  '''
  re2 = requests.get('http://www.reddit.com/r/rickandmorty/comments/1wntlj/rick_and_morty_official_quote_thread/')
  soup2 = BeautifulSoup(re2.content)
  '''

  quotes = soup.find_all('p')
  quotes = [str(x)[3:-5] for x in quotes if not '<br' in str(x)]
  quotes = [x for x in quotes if len(str(x)) > 0]

  return quotes

def getQuotes():
  if not os.path.exists('quotes.pkl'):
    quotes = generateQuotes()
    quotes = cleanUp(quotes)
    with open('quotes.pkl', 'w') as f:
      pickle.dump(quotes, f)
  else:
    with open('quotes.pkl', 'r') as f:
      quotes = pickle.load(f)
      quotes = cleanUp(quotes)

  return quotes

if __name__ == '__main__':
  getQuotes()
