# use of common method for sorting values
example_list = [[1, 4], [5, 8], [5, 4], [3, 2], [9, 1]]
print(example_list)
example_list.sort()     # the list must first be sorted and then printed, sort() method can't be used alongside with print() method
print(example_list)

# use of better method for sorting values
example_list.sort(key=lambda x: x[1])       # list will be sorted by second element of each list
print(example_list)
example_list.sort(key=lambda x: x[1], reverse=True)  # return reversed list
print(example_list)