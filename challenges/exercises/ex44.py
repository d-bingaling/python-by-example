# Challenge 044

"""
Ask how many people the user wants to invite to a party.
If they enter a number below 10,
ask for the names and after each name display "[name] has been invited".
If they enter a number which is 10 or higher, display the message "Too many people".
"""

num_of_people = int(input("How many people are invited to the party? "))

if num_of_people < 10:
    for num in range(0, num_of_people):
        name = input("Enter the name of the invited person: ")
        print(f"{name} has been invited.")
elif num_of_people > 10:
    print("Too many people invited.")
