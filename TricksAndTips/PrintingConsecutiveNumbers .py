#############################################################################
#                   CONSECUTIVE NUMBERS                                     #
#############################################################################

counter = 5

result = [x for x in range(counter)]
result2 = [x for x in range(1, counter+1)]
result3 = [str(x) for x in range(1, counter+1)]
result4 = list(filter(lambda x: x, [x for x in range(1, counter+1)]))
result5 = list(map(lambda x: x, [x for x in range(1, counter+1)]))


def make_string(number: int):
    for elem in range(1, number+1):
        print(elem, end="")


make_string(10)
