# Challenge 035

"""
Ask the user to enter their name
and then display their name three times.
"""


# name = input("Enter your name: ")
# for i in range(0, 3):
#     print(name)


def display_input_three_times(name):
    arr = []
    for i in range(0, 3):
        print(name)
        arr.append(name)
    return arr


def get_user_input():
    name = input("Enter your name: ")
    return name


def main():
    name = get_user_input()
    display_input_three_times(name)


if __name__ == "__main__":
    main()
