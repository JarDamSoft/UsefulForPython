def count_vowels(string):
    vowel_check = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0

    for letter in string:
        if letter in vowel_check:
            vowel_count += 1
        else:
            continue
    return vowel_count


result = count_vowels("Damian To Fajny Gość")
print(result)
