
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
return result
if __name__ == "__main__":
    # Code to run when the file is executed as a script
    safe_print_division(10, 2)
