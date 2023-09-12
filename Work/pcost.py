# pcost.py
#
# Exercise 1.27
cost = 0.0

with open('Data/portfolio.csv', 'rt') as f:
  next(f)
  for line in f:
    info = line.split(',')
    amount = int(info[1])
    price = float(info[2])
    cost = cost + amount * price

print('Total cost', cost)


