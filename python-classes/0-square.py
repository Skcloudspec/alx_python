#!/usr/bin/python3
class Square:
    def __init__(self, size):
        self.__size = size

    def __dict__(self):
        my_dict = {'size': self.__size}
        return my_dict

# Test case 1
mysquare = Square(3)
print(type(mysquare))
print(mysquare.__dict__)

# Test case 2
mysquare = Square(89)
print(type(mysquare))
print(mysquare.__dict__)

# Test case 3
mysquare = Square(3)
print(type(mysquare))
print(mysquare.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

try:
    print(mysquare._size)
except Exception as e:
    print(e)
```


