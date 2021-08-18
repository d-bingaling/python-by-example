import random


def addition():
    num1 = random.randint(5, 20)
    num2 = random.randint(5, 20)
    user_ans = int(input(f"{num1} + {num2} = ? "))
    correct_ans = num1 + num2
    return (user_ans, correct_ans)


def subtraction():
    num1 = random.randint(25, 50)
    num2 = random.randint(1, 25)
    user_ans = int(input(f"{num1} - {num2} = ? "))
    correct_ans = num1 - num2
    return (user_ans, correct_ans)


def do_answers_match(user_ans, correct_ans):
    if user_ans == correct_ans:
        print("Correct!")
    else:
        print(f"Incorrect!, the correct answer is: {correct_ans}")


def main():
    print("1) Addition")
    print("2) Addition")
    addition_type = int(input("Enter 1 or 2: "))
    if addition_type == 1:
        user_ans, correct_ans = addition()
        do_answers_match(user_ans, correct_ans)
    elif addition_type == 2:
        user_ans, correct_ans = subtraction()
        do_answers_match(user_ans, correct_ans)
    else:
        raise Exception("Number entered is incorrect.")


main()
