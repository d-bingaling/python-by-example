# Challenge 011

"""
Task the user to enter a number over 100
and then enter a number under 10
and tell them how many times the smaller number
goes into the larger number in a user-friendly format.
"""

big_num = int(input("Enter a number over 100: "))
small_num = int(input("Enter a number under 10: "))
# with remainder
# answer = big_num/small_num
# without remainder
answer = big_num//small_num

print(f"{small_num} goes into {big_num}, {answer} times.")

