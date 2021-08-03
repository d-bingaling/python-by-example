# Challenge 048

"""
Ask for the name of somebody the user wants to invite to a party.
After this, display the message '[name] has now been invited and add 1 to the count.'
Then ask if they want to invite someone else.
Keep repeating this until they no longer want to invite anyone else to the party,
and then display how many people they have coming to the party.
"""

count = 0
invite = "y"

while invite == "y":
    name = input("Enter the name of the person you're inviting to the party: ")
    print(f"{name} has been invited.")
    count = count + 1
    invite = input("Do you want to invite anyone else? y/n: ")
print(f"You have {count} peeople, coming to your party.")
