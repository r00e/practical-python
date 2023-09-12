# pcost.py
#
# Exercise 1.30
import sys

def portofilo_cost(filename):
  cost = 0.0

  with open(filename, 'rt') as f:
    next(f)
    for line in f:
      try:
        info = line.split(',')
        amount = int(info[1])
        price = float(info[2])
        cost = cost + amount * price
      except ValueError:
        print('Could not parse:', line)

  return cost

if len(sys.argv) == 2:
  filename = sys.argv[1]
else:
  filename = 'Data/portfolio.csv'

cost = portofilo_cost(filename)

print('Total cost', cost)


