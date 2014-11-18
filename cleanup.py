# removes entries that somehow
# made it through my filters
def cleanUp(quotes):
  quotes.pop(104)
  quotes.pop(38)
  quotes.pop(5)
  quotes.pop(2)
  return quotes
