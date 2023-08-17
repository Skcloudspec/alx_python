import random

number = random.choice([0, "not a number", -5, 3, 8, -2, 98, -98])

if not isinstance(number, int):
    print("TypeError")
elif number > 0:
    print("{} is positive".format(number))
elif number < 0:
    print("{} is negative".format(number))
else:
    print("Zero")

