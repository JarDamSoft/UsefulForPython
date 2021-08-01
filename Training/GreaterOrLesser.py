#  Write a function that returns the lesser of two given numbers if both numbers are even,
#  but returns the greater if one or both numbers are odd


def lesser_greater(n1, n2):
    # greater_number = 0
    # lesser_number = 0

    if n1 > n2:
        greater_number = n1
        lesser_number = n2
    else:
        greater_number = n2
        lesser_number = n1

    if n1 % 2 == 0 and n2 % 2 == 0:
        print("Both numbers are even")
        print("Return the lesser one: {}" .format(lesser_number))
    else:
        print("At least one of the given numbers is odd")
        print("Return the greater one: {}" .format(greater_number))


lesser_greater(20, 10)
