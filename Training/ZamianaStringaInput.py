# WZOR JAK TO MA WYGLADAC
liczby = [0, 3, 4]
print(liczby)

# METODA 1
liczby2 = [int(x) for x in input("Podaj liczby: ").split()]
print(liczby2)

# METODA 2
s = input("Podaj liczby: ")
liczby3 = list(map(int, s.split()))
print(liczby3)

# METODA 3
liczby4 = list(map(int, input("Podaj liczby: ").split()))
print(liczby4)