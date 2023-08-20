#!/usr/bin/python3
def raise_exception():
    x = "hello"
    y = 42
    if type(x) != type(y):
        raise TypeError("x and y must be of the same type")
