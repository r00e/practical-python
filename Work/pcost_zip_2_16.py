# pcost.py
#
# Exercise 2.16
import csv

def portfoilo_cost(filename):
  cost = 0.0

  with open(filename, 'rt') as f:
    lines = csv.reader(f)
    headers = next(lines)
    for lineno,line in enumerate(lines,start=1):
      record = dict(zip(headers, line))
      try:
        amount = int(record['shares'])
        price = float(record['price'])
        cost = cost + amount * price
      except ValueError:
        print(f'Line {lineno}: Bad line: {line}')

  return cost
