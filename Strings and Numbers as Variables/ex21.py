# Challenge 021

"""
Ask the user to enter their first name, 
and then ask them to enter their surname.
Join them together with a space between
and display the name and the length of whole name.
"""

firstname = input("What is your first name? ")
lastname = input("What is your last name? ")

fullname = firstname + " " + lastname
print("Full name:", fullname)

length = len(fullname)
print("Name length:", length)
