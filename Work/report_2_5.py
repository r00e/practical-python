# pcost.py
#
# Exercise 2.5
import csv

def read_portofilo(filename):
  '''Computes the total cost (shares*price) of a portofolio file'''
  portfolio = []

  with open(filename, 'rt') as f:
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
      holding = (row[0], int(row[1]), float(row[2]))
      holding = {
          'name': row[0],
          'shares': int(row[1]),
          'price': float(row[2])
      }
      portfolio.append(holding)

  total = 0.0
  for s in portfolio:
    total += s['shares'] * s['price']
  print(total)

  return portfolio
