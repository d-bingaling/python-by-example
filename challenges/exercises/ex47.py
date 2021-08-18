# Challenge 047

"""
Ask the user to enter a number and then enter another number.
Add these together and then ask if they want to add another number.
If they enter 'y', ask them to enter another number and keep adding numbers
until they do not answer 'y'.
Once the loop has stopped, display the total.
"""

num1 = int(input("Enter a number: "))
total = num1
another = "y"
while another == "y":
    num2 = int(input("Enter another number: "))
    total = total + num2
    another = input("Do you wish to enter another number? y/n: ")
print(f"The total is {total}.")
