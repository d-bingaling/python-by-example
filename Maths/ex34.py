# Challenges 034

"""
Display the following message:
    1) Square
    2) Triangle

    Enter a number:

If the user enters 1, 
then it should ask them for the length of one of the sides, 
and display the area.
If they select 2, it should ask for the base
and height of the triangle and display the area.
If they type anything else, it should give them a error message.
"""


print("1) Square")
print("2) Triangle")
num = int(input("Enter a number: "))


if num == 1:
    side_length = int(input("Enter the length of one of the sides: "))
    area = side_length * side_length
    print(f"The area of your shape is: {area}")
elif num == 2:
    base = int(input("Enter the length of the base: "))
    height = int(input("Enter the height of the triangle: "))
    area = (base * height) / 2
    print(f"The area of your shape is: {area}")
else:
    print("Incorrect number, please try again.")
