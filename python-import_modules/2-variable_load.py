#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result

if __name__ == "__main__":
    # Case when a = 89
    a = 89
    b = 2
    print("When a = {}, b = {}".format(a, b))
    safe_print_division(a, b)

    # Case when a = -100
    a = -100
    b = 20
    print("\nWhen a = {}, b = {}".format(a, b))
    safe_print_division(a, b)

    # Case when a is missing
    b = 0
    print("\nWhen a is missing, b = {}".format(b))
    safe_print_division(None, b)
    from variable_load_2 import a

print(a)
