# Write a function takes a two-word string and returns True if both words begin with same letter


def two_words(string):
    words_split = string.split()
    if words_split[0][0].lower() == words_split[1][0].lower():
        return True
    else:
        return False


print(two_words("Hello World"))
