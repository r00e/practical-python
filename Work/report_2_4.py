# pcost.py
#
# Exercise 2.4
import csv

def read_portofilo(filename):
  '''Computes the total cost (shares*price) of a portofolio file'''
  portfolio = []

  with open(filename, 'rt') as f:
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
      holding = (row[0], int(row[1]), float(row[2]))
      portfolio.append(holding)

  total = 0.0
  for name, shares, price in portfolio:
    total += shares * price
  print(total)

  return portfolio
