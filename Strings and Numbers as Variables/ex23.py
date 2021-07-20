# Challenge 023

"""
Ask the user to type in the first line of a nusery rhyme,
display the length of the string.
Ask for a starting number and an ending number,
display just that section of text.
"""


line_one = input("Enter the first line of a nusery rhyme: ")
print(len(line_one))

start = int(input("Enter a starting number: "))
end = int(input("Enter an end number: "))

section = line_one[start:end]
print(section)
