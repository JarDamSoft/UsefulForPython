#############################################################################
#                   UNPACKING COLLECTIONS OF DATA                           #
#############################################################################

list_example = [1, 2, 3, 4, 5]
tuple_example = ("Test", 1, 5, 10)
dictionary_example = {"1": "Test1", "2": [2, 1, 3]}
string_example = "Testowy"

# ---------------------------------------------------------------------------
# The old way to apply unpacking:
# ---------------------------------------------------------------------------
a = list_example[0]
b = list_example[1]
c = list_example[2]
d = list_example[3]
e = list_example[4]
print(a, b, c, d, e)

# the new way to apply unpacking:
a1, b1, c1, d1, e1 = list_example
print(a1, b1, c1, d1, e1)

# unpacking for tuple:
a2, b2, c2, d2 = tuple_example
print(a2, b2, c2, d2)

# unpacking for string:
s1, s2, s3, s4, s5, s6, s7 = string_example
print(s1, s2, s3, s4, s5, s6, s7)

# unpacking for dictionary:
a3, b3 = dictionary_example.values()
print(a3, b3)
a4, b4 = dictionary_example.items()
print(a4, b4)

print("\n------------------------------------------")

# ---------------------------------------------------------------------------
# Best method to unpack collections:
# ---------------------------------------------------------------------------
print(*list_example)
print(*tuple_example)
print(**dictionary_example)
print(*string_example)
