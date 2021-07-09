# Challenge 005 

"""
Ask the user to enter three numbers.
Add together the first two numbers, 
then multiply this total by the third.
Display the answer as 'The answer is [answer].'
"""

num1 = int(input("Enter a number "))
num2 = int(input("Enter another number "))
num3 = int(input("Enter a final number "))

num_total = ((num1 + num2) * num3)

print(f"The answer is {num_total}")
