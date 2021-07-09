# Challenge 007 

"""
Ask the user for their name and their age.
Add 1 to their age and display the output as
'[name] next birthday you will be [new age]'
"""

name = input("What is your name? ")
age = int(input("What is your age? "))

new_age = age + 1 

print(f"{name} next birthday you will be {new_age}.")