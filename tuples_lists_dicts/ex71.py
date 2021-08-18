def display_sorted_sports(fave_sport):
    sports_list = ["Volleyball", "Gymnastics", "Badminton", "Handball"]
    sports_list.append(fave_sport)
    print(sorted(sports_list))


def user_input():
    fave_sport = input("What is your favourite sport? ")
    return fave_sport


def main():
    fave_sport = user_input()
    display_sorted_sports(fave_sport)


if __name__ == "__main__":
    main()
