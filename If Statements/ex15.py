# Challenge 015


"""
Ask the user to enter their favourite colour.
If they enter 'red', 'RED, or 'Red'
display the message 'I like red too',
otherwise display the message 'I don't like [colour], I prefer red.'
"""

fave_colour = input("Enter your favourite colour: ")

if fave_colour == "RED" or fave_colour == "Red" or fave_colour == "red":
    print("I like red too")
else:
    print(f"I don't like {fave_colour}, I prefer red.")
