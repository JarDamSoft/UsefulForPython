# Write a Python function that checks whether a passed string is palindrome or not


def check_if_palindrome():
    given_word = input("Give us some word: ")
    letter_list = []

    for letter in given_word:
        letter_list.append(letter)

    if letter_list[0::] == letter_list[::-1]:
        print("It's palindrome")
    else:
        print("It's not palindrome")
    print(letter_list)


check_if_palindrome()
