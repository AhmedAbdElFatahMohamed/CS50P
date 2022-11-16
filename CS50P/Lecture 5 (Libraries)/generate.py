#Choice
import random

coin=random.choice(["Heads","Tails"])

print(coin)


# another Approach : we import specific finction from the library
#first solution is better cuz it leaves the keyword "choice" availabe for later use

from random import choice
coin =choice(["Heads","Tails"])
print(coin)

#randint:retunts random intefar from range

import random
number =random.randint(0,10)
print(number)

#shuffle:shuffles a list

import random
cards=["Ace","King","Queen","Jack"]
random.shuffle(cards)
for card in cards:
    print(card)

#mean:returns the mean value for a list of int

import statistics
print(statistics.mean([100,90,80]))
