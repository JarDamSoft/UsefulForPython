############################################################################
#                       COMPREHENSION                                      #
#  Comprehension = creating a new collection of data in one line of code   #
############################################################################


# List examples:
x = [i for i in range(100)]
print(x)
x1 = [i for i in range(100) if i % 2 == 0]
print(x1)
x2 = [i * j for i in range(100) for j in range(10)]
print(x2)
x3 = [[0 for _ in range(5)] for _ in range(5)]  # "_" underscore sign in this case is used instead of variable
print(x3)

# Tuple example:
x4 = (i for i in "hello")  # creating generator
print(x4)
print(tuple(x4))

# Dictionary example:
numbers = [1, 2, 3, 4, 5]
japan_car_brands = ["Mitsubishi", "Honda", "Toyota", "Suzuki"]

x5 = {k: v for v in japan_car_brands for k in range(len(japan_car_brands))}
print(x5)
x6 = dict(zip(numbers, japan_car_brands))
print(x6)
x7 = dict(zip([x for x in range(len(japan_car_brands))], japan_car_brands))
print(x7)
