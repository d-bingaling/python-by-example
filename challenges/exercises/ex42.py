# Challenge 042

"""
Set a variable called total to 0.
Ask the user to enter five numbers, 
and after each input ask them if they want that number included.
If they do, then add that number to the total. 
If they do not want it included, then don't add it to the total.
After they have entered all five numbers, display the total.
"""

total = 0
for i in range(0, 5):
    num = int(input("Enter a number: "))
    answer = input("Include this number? y/n ")
    if answer == "y":
        total = total + num
    print(total)
