def zamiana_liter(tekst):
    index = [int(x) for x in input("Podaj ktore litery chcesz powiekszyc").split()]
    # indices = [0, 3, 4]
    imie_poprawione = []
    index_count = 1
    # METODA 1
    # for i, litera in enumerate(tekst):
    #     if i in index:
    #         print("".join(litera.upper()))
    #     else:
    #         print("".join(litera))

    # METODA 2
    # for litera in tekst:
    #     if index_count in index:
    #         print(imie_poprawione.join(litera.upper()), end=" ")
    #     else:
    #         print(imie_poprawione.join(litera), end=" ")
    #     index_count += 1

    # METODA 3
    for litera in tekst:
        if index_count in index:
            imie_poprawione.append(litera.upper())
        else:
            imie_poprawione.append(litera)
        index_count += 1

    print("".join(imie_poprawione))
    print(imie_poprawione)

    # METODA 4
    # print("".join(c.upper() if i in indices else c for i, c in enumerate(s)))


zamiana_liter("Damian")