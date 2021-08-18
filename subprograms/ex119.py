import random


def pick_num():
    low_num = int(input("Enter a low number: "))
    high_num = int(input("Enter a high number: "))
    comp_num = random.randint(low_num, high_num)
    return comp_num


def first_guess():
    print("I am thinking of a number... ")
    guess_1 = int(input("Guess the number I am thinking of: "))
    return guess_1


def checking(comp_num, guess_1):
    try_again = True
    while try_again == True:
        if comp_num == guess_1:
            print("Correct, you win!")
            try_again == False
        elif comp_num > guess_1:
            guess_1 = int(input("Too low, try again: "))
        else:
            guess_1 = int(input("Too high, try again: "))


def main():
    comp_num = pick_num()
    guess_1 = first_guess()
    checking(comp_num, guess_1)


main()
