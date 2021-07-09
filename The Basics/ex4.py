# Challenge 004 

"""
ask the user to enter two numbers then display 
the answer as 'The total is [answer]'
"""

# my answer
num1 = input("Please enter a number ")
num2 = input("Please enter another number ")
total_num = (int(num1) + int(num2))

print(f"The total is {total_num}")

# expected answer 

num1 = int(input("Please enter a number "))
num2 = int(input("Please enter another number "))
total_num = num1 + num2

print(f"The total is {total_num}")

# this way makes more sense, as they are making
# both inputs an int from the start
# meaning either of the variables can be called
# and will each have an int value
# my way only set the total_num as an int
