# Write a function that checks whether a number is in a given range (inclusive of high and low)


def check_number(num, start, end):
    if num in range(start, end+1):
        print("Number {} is in range between {} and {}" .format(num, start, end))
    else:
        print("Number is beyond given range")


check_number(5, 2, 7)
