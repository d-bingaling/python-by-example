# Challenge 025


"""
Ask the user to enter their first name.
If the length of their first name is under five characters,
ask them to enter their surname and join them together (without a space)
and display the name in upper case.
If the length of the first name is five or more, 
display their first name in lower case.
"""


firstname = input("Enter your first name: ")

if len(firstname) < 5:
    lastname = input("Enter your surname: ")
    print(firstname.upper(), lastname.upper())
elif len(firstname) >= 5:
    print(firstname.lower())
