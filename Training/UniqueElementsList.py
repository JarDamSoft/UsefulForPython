# Write a Python function that takes a list and returns a new list with unique elements of the first list.


def unique_elements(given_list):
    new_list = []
    for element in given_list:
        if element not in new_list:
            new_list.append(element)
    return new_list


result = unique_elements([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])
print("Unique elements for given list: {}" .format(result))
