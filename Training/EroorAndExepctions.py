import math

number1 = 7
number2 = "7"
number3 = 9

# # PRZYKLAD 1:
# try:
#     wynik = number1 + number2  # Wystapi blad, nie mozna dodac int do stringa, kolejne instrukcje sie nie wykonaja
# except:
#     print("Wyglada na to, ze wystapil blad. Nie dodajesz odpowiednich typow zmiennych do siebie")
# else:
#     print("Dzialanie powiodlo sie")
#     print("Rezultat: {}".format(wynik))
#
# print("Czy to sie pokaze w konsoli?")
#
# # PRZYKLAD 2:
# try:
#     plik = open('testowyplik', 'r')
#     plik.write("To jest testowa linijka kodu")
# except TypeError:
#     print("Wystapil blad typu danych")
# except OSError:
#     print("Masz blad typu OS")
# except:  # Wykonuje sie zawsze gdy inne wyjatki nie pasuja
#     print("Inee wyjatki nie pasowaly")
# finally:  # Wykonuje sie zawsze, niezaleznie od innych czynnikow
#     print("Zawsze sie wykonuje...")

# # PRZYKLAD 3:
def pobranie_liczby():

    while True:
        try:
            pobrane = int(input("Podaj liczbe:"))
            print("Podano prawidlowa liczbe")
        except:
            print("Wystapil blad. To nie jest liczba")
            print("Sprobuj ponownie...")
            continue
        else:
            print("Program zakonczyl prace bez bledow")
            break
        finally:
            print("Koniec sprawdzania bledow...")


pobranie_liczby()

                                                        # CWICZENIA

# 1. Handle the exception thrown by the code below by using try and except blocks.
try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except:
    print("Wystapil blad... :/")
    print("Nie mozna potegowac wartosci typu string")


# 2. Handle the exception thrown by the code below by using try and except blocks.
# Then use a finally block to print 'All Done.'
try:
    x = 5
    y = 0
    z = x/y
except:
    print("Wystapil blad 2... ;/")
    print("Nie mozna dzielic przez 0")
finally:
    print("Wszystko sie udalo")


# 3. Write a function that asks for an integer and prints the square of it.
# Use a while loop with a try, except, else block to account for incorrect inputs.
def podajliczbe():
    while True:
        try:
            liczba = int(input("Podaj z jakiej liczby chcesz obliczyc pierwiastek:"))
            pierwiastek = math.sqrt(liczba)
        except:
            print("Wystapil blad. Podaj prawidlowa liczbe jeszcze raz...")
            continue
        else:
            print("Pierwiastek z liczby {} to: {}".format(liczba, pierwiastek))
            break

podajliczbe()

