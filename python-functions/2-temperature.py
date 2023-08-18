#!/usr/bin/env python3
def convert_to_celsius(fahrenheit):
    celsius = round((fahrenheit - 32) * 5/9, 14)  # rounding to 14 decimal places
    return round(celsius, 2)

