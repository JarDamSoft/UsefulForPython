# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters


def count_letters(string):

    all_numbers = 0
    big_letters = 0
    small_letters = 0

    for letter in string:
        if letter.isalnum():
            all_numbers += 1
        if letter.isupper():
            big_letters += 1
        elif letter.islower():
            small_letters += 1
    print("Given string: {}" .format(string))
    print("All letters in given string: {}".format(all_numbers))
    print("Number of big letters in given string: {}" .format(big_letters))
    print("Number of small letters in given string: {}".format(small_letters))


count_letters("ThiS is A examPLe String")
