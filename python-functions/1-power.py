#!/usr/bin/env python3
# Define the pow function
def pow(a, b):
    # initialize result to 1
    result = 1

    # multiply a to itself b times
    # if b is negative, divide 1 by a b times
    for i in range(abs(b)):
        if b < 0:
            result /= a
        else:
            result *= a


