# Challenge 029
import math

"""
Ask the user to enter an integer that is over 500.
Work out the square root of that number, 
display it to two decimal places.
"""

num = int(input("Enter a number over 500: "))
answer = math.sqrt(num)

print(round(answer, 2))
