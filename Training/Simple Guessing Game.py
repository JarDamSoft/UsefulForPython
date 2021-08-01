import random


def generate_number():
    print("WELCOME TO THE GUESSING GAME")
    global random_number
    random_number = random.randint(0, 100)
    guess()


def guess():
    user_pick = int(input("Please, give us your number (from 0 to 100): "))
    warm_cold(user_pick)


def warm_cold(pick):
    while True:
        if pick == random_number:
            print("WIN! You guessed the number")
            break
        elif (pick <= (random_number - 10) or pick >= (random_number + 10)) and (pick >= 0) and (pick <= 100):
            print("It's cold...")
            guess()
        elif (pick <= (random_number - 15) or pick >= (random_number + 15)) and (pick >= 0) and (pick <= 100):
            print("It's colder...")
            guess()
        elif (pick <= (random_number - 5) or pick >= (random_number + 5)) and (pick >= 0) and (pick <= 100):
            print("It's warm...")
            guess()
        elif (pick <= (random_number - 2) or pick >= (random_number + 2)) and (pick >= 0) and (pick <= 100):
            print("It's warmer...")
            guess()
        else:
            print("There is an error.")
            guess()


generate_number()
