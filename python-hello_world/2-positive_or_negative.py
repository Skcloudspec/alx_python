import random

number = random.choice([0, "not a number", -5, 3, 8, -2, 0])

if type(number) != int:
    print("{} is not a valid number".format(number))
else:
    if number > 0:
        print("{} is a positive number".format(number))
    elif number < 0:
        print("{} is a negative number".format(number))
    else:
        print("{} is zero".format(number))
