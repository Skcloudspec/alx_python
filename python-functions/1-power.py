#!/usr/bin/env python3
def pow(a, b):
    # Handle base cases for b.
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b < 0:
        return 1/pow(a, -b)
    else:
        # Compute the power recursively.
        p = pow(a*a, b//2)
        if b % 2 == 0:
            return p
        else:
            return p * a

