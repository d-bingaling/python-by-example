# Challenge 049


"""
Create a variable called compnum and set the value to 50.
Ask the user to enter a number.
While their guess is not the same as the compnum value,
tell them if their guess is too high, or too low and ask them to have another guess.
If they enter the same value as the compnum, display the message
'Well done, you took [count] attempts'.
"""

compnum = 50
count = 0
num = int(input("Guess the number: "))

while num != compnum:
    count = count + 1
    if num < compnum:
        print("Your guess was too low.")
    else:
        print("Your guess was too high.")
    num = int(input("Have another guess: "))
print(f"Well done, you took {count} attempts.")
