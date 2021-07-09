# Challenge 006 

"""
Ask how many slices of pizza the user started with,
and ask how many slices have been eaten.
Work out how many slices they have left
and display the answer in a user-friendly format. 
"""

original_pizza = int(input("How many slices of pizza did you start with? "))
eaten_pizza = int(input("How many slices of pizza have been eaten? "))

leftover_pizza = original_pizza - eaten_pizza

print(f"You have {leftover_pizza} slices of pizza leftover, enjoy!")