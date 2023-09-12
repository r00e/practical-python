# pcost.py
#
# Exercise 1.30
def portofilo_cost(filename):
  cost = 0.0

  with open(filename, 'rt') as f:
    next(f)
    for line in f:
      info = line.split(',')
      amount = int(info[1])
      price = float(info[2])
      cost = cost + amount * price

  return cost

cost = portofilo_cost('Data/portfolio.csv')

print('Total cost', cost)


