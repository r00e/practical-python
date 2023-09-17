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

def print_report(report):
  headers = ('Name', 'Shares', 'Price', 'Change')
  print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
  separator = '-' * 10
  print(f'{separator} {separator} {separator} {separator}')
  for row in report:
    name, shares, price, change = row
    priceWithFormat = f'{price:.2f}'
    priceWithCurrency = '$' + priceWithFormat
    print(f'{name:>10s} {shares:>10d} {priceWithCurrency:>10s} {change:>10.2f}')
