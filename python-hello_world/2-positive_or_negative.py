#!/usr/bin/python3
import random

# First random number generator
number1 = random.choice([-98, -2, 0, 3, 8, 98])

if not isinstance(number1, int):
    print("TypeError")
elif number1 > 0:
    print("{} is positive".format(number1))
elif number1 == 0:
    print("0 is zero")
else:
    print("{} is negative".format(number1))

# Second random number generator
number2 = random.randint(-10, 10)

if number2 % 2 == 0:
    print("{} is even".format(number2))
else:
    print("{} is odd".format(number2))
