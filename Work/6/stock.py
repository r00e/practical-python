#4.1

class Stock:
  def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price

  def __getitem__(self, key):
    if key == 'name':
      return self.name
    elif key == 'shares':
      return self.shares
    elif key == 'price':
      return self.price
    else:
      raise KeyError(f"{key} not found")

  def cost(self):
    return self.shares * self.price

  def sell(self, amount):
    self.shares -= amount
