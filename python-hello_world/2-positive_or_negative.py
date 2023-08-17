#!/usr/bin/python3
import random

number1 = random.choice([-98, -2, 0, 3, 8, 98])

if type(number1) == str:
    print("TypeError")
elif number1 > 0:
    print(str(number1) + " is positive")
elif number1 == 0:
    print("0 is zero")
else:
    print(str(number1) + " is negative")

number2 = random.randint(-10, 10)

if number2 % 2 == 0:
    print(str(number2) + " is even")
else:
    print(str(number2) + " is odd")

