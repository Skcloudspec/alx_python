#!/usr/bin/python3

import random

number = random.randint(-10, 10)

if number % 2 == 0:
    print("{} is even".format(number))
else:
    print("{} is odd".format(number))
