#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary

def print_sorted_dictionary(my_dict):
    """ Print sorted dictionary """
    keys = sorted(my_dict.keys())
    for k in keys:
        print("{}: {}".format(k, my_dict[k]))

# Test case 1
my_dict = { 'a': "a", 'b': "b" , 'c': "c", 'd': "d", 'e': "e" }
key = "a"
value = "A"
new_dict = update_dictionary(my_dict, key, value)
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(my_dict)

# Test case 2
print("--")
print("--")

my_dict = { 'a': "a", 'b': "b" , 'c': "c", 'd': "d", 'e': "e" }
key = "e"
value = "E"
new_dict = update_dictionary(my_dict, key, value)
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(my_dict)

# Test case 3
print("--")
print("--")

my_dict = { 'a': "a", 'b': "b" , 'c': "c", 'd': "d", 'e': "e" }
key = "a"
value = 89
new_dict = update_dictionary(my_dict, key, value)
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(my_dict)

# Test case 4
print("--")
print("--")

my_dict = { 'a': "a", 'b': "b" , 'c': "c", 'd': "d", 'e': "e" }
key = "f"
value = "A"
new_dict = update_dictionary(my_dict, key, value)
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(my_dict)

# Test case 5
print("--")
print("--")

my_dict = { }
key = "a"
value = "a"
new_dict = update_dictionary(my_dict, key, value)
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(my_dict)
