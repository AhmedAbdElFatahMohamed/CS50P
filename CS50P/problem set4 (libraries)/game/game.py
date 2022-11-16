# Trick:Had to use two loops on to check for valid input and the other to get promt another guess

import random

while True:
    try:
        level = int(input("level: "))
        answer = random.randint(1, level)
        break
    except:
        continue
while True:
    try:
        guess = int(input("Guess: "))
        if answer < guess:
            print("Too large!")
            continue
        elif answer > guess:
            print("Too small!")
            continue
        else:
            print("just right!!")
            break
    except:
        continue
