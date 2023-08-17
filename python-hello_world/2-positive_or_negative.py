#!/usr/bin/python3
import random

number = random.choice([-98, -2, 0, 3, 8, 98])

if not isinstance(number, int):
    print("TypeError")
else:
    if number > 0:
        print("{} is positive".format(number))
    elif number == 0:
        print("0 is zero")
    else:
        print("{} is negative".format(number))

