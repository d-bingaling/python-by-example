# Challenge 033

"""
Ask the user to enter two numbers.
Use whole number division to divide the first number by the second
and also work out the remainder and display the answer in a user-friendly way.
"""

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Whole number division =", num1 // num2)
print("Division with remainder:", num1 % num2)
