"""Number Guess Game"""

import random

com = random.randint(1,100)
tries = 0

while True:
    tries += 1
    try:
        hum = int(input("guess your number between (1 - 100) :- "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")

    if com == hum:
        print(f"congratulations you have won in {tries} tries!")
        break

    elif hum > com:
        print("sorry wrong guess go lower !")

    elif hum < com:
        print("sorry wrong guess go higher !")