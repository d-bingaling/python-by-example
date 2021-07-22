# Challenge 026

"""
Pig Latin takes the first consonant of a word,
moves it to the end of the word and adds on 'ay'.
If a word begins with a vowel you just add 'way' to the end.
For example, pig becomes igpay, banana becomes ananabay,
and aadvark becomes aadvarkway.
Create a program that will ask the user to enter a word
and change it into Pig Latin.
Make sure the new word is displayed in lower case.
"""

word = input("Enter a word: ").lower()

vowels = ["a", "e", "i", "o", "u"]
first_letter = word[0]
rest_of_word = word[1:]

if first_letter not in vowels:
    newword = rest_of_word + first_letter + "ay"
else:
    newword = first_letter + rest_of_word + "way"
print(newword)
