# Challenge 045


"""
Set the total to 0 to start with.
While the total is 50 or less, ask the user to input a number.
Add that number to the total and print the message "This is the [total]".
Stop the loop when the total is over 500.
"""


def less_than_fifty(num):
    total = 0
    if isinstance(num, int):
        while total <= 50:
            total = total + num
            print(f"The total is, {total}")
        return total
    raise TypeError("Please make sure you've entered a number.")


def user_input():
    num = int(input("Enter a number: "))
    return num


def main():
    num = user_input()
    less_than_fifty(num)


if __name__ == "__main__":
    main()
