# Challenge 022

"""
Ask the user to enter their first name and last name in lower case.
Change the case to title case and join them together. 
Display the finished result.
"""

firstname = input("Enter your first name in lower case: ")
lastname = input("Enter your last name in lower case: ")
firstname_title = firstname.title()
lastname_title = lastname.title()

fullname = f"{firstname_title} {lastname_title}"

print("Full name is: ", fullname)
