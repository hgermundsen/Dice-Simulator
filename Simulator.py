# Hunter Germundsen
# 06/05/19


import random

while 1:
    answer = int(input("Hello, would you like 6 sided or 20 sided? Number: "))

    if answer != 20 and answer != 6:
        answer = input("That wasn't a valid choice, please press enter to restart")
        continue
    elif answer == 20:
        num = random.randint(1, 20)
        print("You rolled a(n) %d" % num)
        again = input("Would you like to continue? y/n? Choice: ")
        if again == "y":
            continue
        elif again == "n":
            break
        else:
            print("That wasn't a valid input, please press enter to try again")
            continue
    elif answer == 6:
        amount = int(input("Would you like 1 die, or 2? Number: "))
        num = random.randint(1, 6)
        if amount == 1:
            print("You rolled a(n) %d" % num)
            again = input("Would you like to continue? y/n? Choice: ")
            if again == "y":
                continue
            elif again == "n":
                break
            else:
                print("That wasn't a valid input, please press enter to try again")
                continue
        elif amount == 2:
            num2 = random.randint(1, 6)
            print("You rolled a(n) %d and a(n) %d" % (num, num2))
            again = input("Would you like to continue? y/n? Choice: ")
            if again == "y":
                continue
            elif again == "n":
                break
            else:
                print("That wasn't a valid input, please press enter to try again")
                continue
        else:
            print("That wasn't a valid choice, please press enter to try again")
            continue
