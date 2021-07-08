# Challenge 009 

"""
Write a program that will ask for a number of days
and then will show how many hours, minutes and seconds
are in that number of days.
"""

days = int(input("How many days are there? "))
hours = days*24
mins = hours*60
secs = mins*60

print("There are", hours, "hours", mins, "minutes, and", secs, "seconds in", days, "days.")
