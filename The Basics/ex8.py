# Challenge 008 

"""
Ask for the total price of the bill,
then ask how many diners there are.
Divide the total bill by the number of diners
and show how much each person must pay.
"""

bill = int(input("How much is the total bill? "))
diners = int(input("How many diners are there? "))

amount_to_pay = bill/diners

print("Each person needs to pay £", amount_to_pay)