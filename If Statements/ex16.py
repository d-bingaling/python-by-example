# Challenge 016

"""
Ask the user if it is raining and convert their answer to lower case
so it doesn't matter what case they type it in.
If they answer 'yes', ask if it is windy.
If they answer 'yes' to this second question,
display the answer 'It is too windy for an umbrella.'
Otherwise display the answer 'Take an umbrella'.
If they do not enter 'yes' to the first question,
display the message 'Have a nice day!'
"""

raining = input("Is it raining? ")
# turning the string into lowercase
raining = str.lower(raining)

if raining == "yes":
    windy = input("Is it windy? ")
    windy = str.lower(windy)
    if windy == "yes":
        print("It is too windy for an umbrella.")
    else:
        print("Take an umbrella!")
else:
    print("Have a nice day!")
