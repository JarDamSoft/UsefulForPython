# Given an integer n, return True if n is within 10 of either 100 or 200


def wOdleglosci(num):
    # METHOD 1
    # return ((abs(100 - num) <= 10) or (abs(200 - num) <= 10))
    # METHOD 2
    result = num - 100
    result2 = num - 200
    if (result >= 0 and result <= 10) or (result >= -10 and result <= 0):
        return True
    elif (result2 >= 0 and result2 <= 10) or (result2 >= -10 and result2 <= 0):
        return True
    else:
        return False


print(wOdleglosci(209))
