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
    f = open('quotes.pkl', 'w')
    pickle.dump(quotes, f)
    f.close()
    return quotes
  else:
    f = open('quotes.pkl', 'r')
    quotes = pickle.load(f)
    quotes = cleanUp(quotes)
    f.close()
    return quotes

if __name__ == '__main__':
  getQuotes()
