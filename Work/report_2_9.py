# report.py
import csv

def read_portfolio(filename):
  '''
  Read a stock portfolio file into a list of dictionaries with keys
  name, shares, and price.
  '''
  portfolio = []
  with open(filename) as f:
    rows = csv.reader(f)
    headers = next(rows)

    for row in rows:
      stock = {
        'name'   : row[0],
        'shares' : int(row[1]),
        'price'   : float(row[2])
      }
      portfolio.append(stock)

  return portfolio

def read_prices(filename):
  '''
  Read a CSV file of price data into a dict mapping names to prices.
  '''
  prices = {}
  with open(filename) as f:
    rows = csv.reader(f)
    for row in rows:
      try:
        prices[row[0]] = float(row[1])
      except IndexError:
        pass

  return prices

def make_report(portfolio, prices):
  report = []
  for stock in portfolio:
    if stock['name'] in prices:
      curPrice = float(prices[stock['name']])
      originalPrice = float(stock['price'])
      report.append((stock['name'], int(stock['shares']), curPrice, curPrice - originalPrice))

  return report
