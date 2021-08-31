def display_sorted_sports(fave_sport):
    sports_list = ["Volleyball", "Gymnastics", "Badminton", "Handball"]
    sports_list.append(fave_sport)
    if fave_sport == fave_sport.capitalize():
        ordered_sports_list = sorted(sports_list)
        print(ordered_sports_list)
        return ordered_sports_list
    else:
        raise TypeError("Input was capitalized.")


def user_input():
    fave_sport = input("What is your favourite sport? ")
    return fave_sport


def main():
    fave_sport = user_input()
    display_sorted_sports(fave_sport)


if __name__ == "__main__":
    main()
