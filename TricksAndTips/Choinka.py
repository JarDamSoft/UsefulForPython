szerokosc = 1
wysokosc = 5
test = "*"

# for x in range(wysokosc):
#     print(test)
#     for y in range(szerokosc):
#         print("")
#     test = test + "**"

spacja = 5
gwiazdka = "*"
for i in range(spacja):
    print(" " * spacja + gwiazdka)
    gwiazdka += "**"
    spacja -= 1


# z = 5
# x = 1
# for i in range(5):
#     print(' ' * z + '+' * x + ' ' * z)
#     x += 2
#     z -= 1