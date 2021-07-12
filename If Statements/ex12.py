# Challenge 012

"""
Ask for two numbers. 
If the first one is larger than the second, 
display the second number first and then the first number
otherwise show the first number first and then the second. 
"""


num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))


if num1 > num2:
    print(f"Second number: {num2}")
    print(f"First number: {num1}")
else:
    print(f"First number: {num1}")
    print(f"Second number: {num2}")
