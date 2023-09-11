# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
  principal = principal * (1 + rate / 12) - payment
  total_paid = total_paid + payment

print('Total paid', total_paid)

# Exercise 1.8
principal_1_8 = 500000.0
rate_1_8 = 0.05
payment_1_8 = 2684.11
total_paid_1_8 = 0.0
first_year = 12
months = 0

while principal_1_8 > 0:
  months = months + 1
  principal_1_8 = principal_1_8 * ( 1 + rate / 12) - payment_1_8
  if first_year > 0 :
    principal_1_8 = principal_1_8 - 1000
    total_paid_1_8 = total_paid_1_8 + 1000
    first_year = first_year - 1
  total_paid_1_8 = total_paid_1_8 + payment_1_8

print('Total paid', total_paid_1_8)
print('Total month', months)
