# mortgage.py
#
# Exercise 1.11

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
total_month = 0
cur_month = 1

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
  if cur_month >= extra_payment_start_month and cur_month <= extra_payment_end_month:
    principal = principal * (1 + rate / 12) - payment - extra_payment
    total_paid = total_paid + payment + extra_payment
  else:
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment

  if principal < 0:
    overpayment = 0 - principal
    principal = 0
    total_paid = total_paid - overpayment

  print(cur_month, round(total_paid,2), round(principal, 2))

  total_month = total_month + 1
  cur_month = cur_month + 1

print('Total paid', round(total_paid, 2))
print('Months', total_month)
