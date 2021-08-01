# Your task is to sort a given string. Each word in the string will contain a single number. This number is the
# position the word should have in the result.
#
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
#
# If the input string is empty, return an empty string. The words in the input String will
# only contain valid consecutive numbers.


def order(sentence):

    if sentence == "":
        print("Given sentence is empty!")
        return sentence

    divided_sentence = sentence.split()
    new_sentence = []

    for string in divided_sentence:
        for char in string:
            if char.isdigit() and int(char) == 1:
                new_sentence.insert(0, string)
            elif char.isdigit() and int(char) == 2:
                new_sentence.insert(1, string)
            elif char.isdigit() and int(char) == 3:
                new_sentence.insert(2, string)
            elif char.isdigit() and int(char) == 4:
                new_sentence.insert(3, string)
            elif char.isdigit() and int(char) == 5:
                new_sentence.insert(4, string)
            elif char.isdigit() and int(char) == 6:
                new_sentence.insert(5, string)

    string_new_sentence = " ".join(new_sentence)
    return string_new_sentence


print(order("is2 Thi1s T4est 3a"))


def order2(sentence):

    if sentence == "":
        print("Given sentence is empty!")
        return sentence

    divided_sentence = sentence.split()
    new_sentence = []

    for string in divided_sentence:
        for char in string:
            if char.isdigit() and char == '1':
                new_sentence.insert(0, string)
            elif char.isdigit() and char == '2':
                new_sentence.insert(1, string)
            elif char.isdigit() and char == '3':
                new_sentence.insert(2, string)
            elif char.isdigit() and char == '4':
                new_sentence.insert(3, string)
            elif char.isdigit() and char == '5':
                new_sentence.insert(4, string)
            elif char.isdigit() and char == '6':
                new_sentence.insert(5, string)

    string_new_sentence = " ".join(new_sentence)
    return string_new_sentence


print(order2("4of Fo1r pe6ople g3ood th5e the2"))


