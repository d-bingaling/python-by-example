# Challenge 032

import math

"""
Ask for the radius and the depth of the cylinder and
work out the total volume (circle area* depth)
rounded to three decimal spaces.
"""

radius = int(input("Enter the radius of the cylinder: "))
depth = int(input("Enter the depth of the cylinder: "))
area = math.pi * (radius ** 2)

print(round(area * depth, 3))
