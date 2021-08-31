# Challenge 043

"""
Ask which direction the user wants to count (up or down).
If they select up, then ask the for the top number and then count from 1 to that number.
If they select down, ask them to enter a number below 20 and then count down from 20 to that number.
If they entered something other than up or down, display the message "I don't understand."
"""

direction = input("Do you want to count up or down? up/down ")

if direction == "up":
    top = int(input("Enter the top number: "))
    for num in range(0, top + 1):
        print(num)
elif direction == "down":
    down = int(input("Enter a number below 20: "))
    for num in range(20, down - 1, -1):
        print(num)
else:
    print("I don't understand")
