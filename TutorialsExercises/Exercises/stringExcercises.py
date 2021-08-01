"""
Exercise 1:
-----------
Write a code that asks user to input a number between 1 and 5 inclusive. The code will take the integer value and
print out the string value. So for example if the user inputs 2 the code will print two. Reject any input that is not
a number in that range
"""


# while True:
#     user_num = int(input("Type a number between 1 and 5"))
#     if isinstance(user_num, int):
#         if (user_num == 1 or user_num >= 1) and (user_num <= 5 or user_num == 5):
#             print(user_num)
#             print("Your number is within range. Thank you for playing :)")
#             break
#         else:
#             print("You gave number out of range. Try again...")
#             continue
#     else:
#         print("It's not a number \n Please type number value")
#         continue


"""
Exercise 2:
-----------
Write a code that asks user to input a string with number between 1 and 5 inclusive. Reject any input that is not
a number in that range
"""


# stringValues = ['one', 'two', 'three', 'four', 'five']
#
# while True:
#     user_num = input("Type a number between 1 and 5. It must be string value")
#     if isinstance(user_num, str):
#         if user_num.lower() in stringValues:
#             print(user_num)
#             print("Your number is within range. Thank you for playing :)")
#             break
#         else:
#             print("You gave number out of range, or it's not a string value. Please, try again...")
#             continue
#     else:
#         print("It's not a string number \n Please type string value")
#         continue


"""
Exercise 3:
-----------
Create a variable containing an integer between 1 and 10 inclusive. Ask the user to guess the number.
If they guess to high or too low, tell them they have not won. Tell them they win if they guess the correct number.
"""


# intContainer = 5
#
# while True:
#     givenNumber = int(input("Try to guess a number between 1-10"))
#     if isinstance(givenNumber, int):
#         if givenNumber < 1 or givenNumber > 10:
#             print("Typed number is out of given range. Try again...")
#             continue
#         elif givenNumber > intContainer:
#             print("Given number is to high. Try again...")
#             continue
#         elif givenNumber < intContainer:
#             print("Given number is to low. Try again...")
#             continue
#         elif givenNumber == intContainer:
#             print("Congratulations! :) You've guessed the correct number.")
#             break
#     else:
#         print("It's not a number \n Please type number value")
#         continue


"""
Exercise 4:
-----------
Ask the user for two integers between 1 and 20. If they are both greater than 15 return their product.
If only one is greater than 15 return their sum, if neither are greater than 15 return zero.
"""

while True:
    num1, num2 = map(int, input("Give us two numbers between 1 and 20 (separated with comma)").split(","))
    if isinstance(num1, int):
        if (num1 and num2) > 15:
            print(num1*num2)
        elif (num1 or num2) > 15:
            print(num1+num2)
        elif (num1 and num2) < 15:
            print(0)
    else:
        print("It's not a number")
        continue
    decision = input("Do you want to continue? Yes/No")
    if isinstance(decision, str):
        if decision.lower().startswith("y"):
            continue
        elif decision.lower().startswith("n"):
            print("Thank you for playing :) Bye!")
            break
    else:
        print("It's not a string")
        continue
