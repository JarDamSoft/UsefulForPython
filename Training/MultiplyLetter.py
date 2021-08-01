# Given a string, return a string where for every character in the original there are three characters


def multiply_letter(string):
    string_changed = ""
    for letter in string:
        string_changed = string_changed + (letter * 3)
    return string_changed


print(multiply_letter("Hello to everyone"))
