#!/usr/bin/python3
from add_0 import add

a = 1
b = 2

print("{0:d} + {1:d} = {2:d}".format(a, b, add(a, b)))
if __name__ == "__main__":
    # Main program code goes here
a = 1
b = 2
from add_0 import add
result = add(a, b)
print("{} + {} = {}".format(a, b, result))

