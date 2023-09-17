# pcost.py
#
# Exercise 2.15
import sys

def portfoilo_cost(filename):
  cost = 0.0

  with open(filename, 'rt') as lines:
    next(lines)
    for lineno,line in enumerate(lines,start=1):
      try:
        info = line.split(',')
        amount = int(info[1])
        price = float(info[2])
        cost = cost + amount * price
      except ValueError:
        print(f'Line {lineno}: Bad line: {line}')

  return cost
