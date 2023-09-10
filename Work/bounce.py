# bounce.py
#
# Exercise 1.5
height = 100
for i in range(10):
  newHeight = height * (3 / 5)
  print(i + 1, round(newHeight, 4))
  height = newHeight
