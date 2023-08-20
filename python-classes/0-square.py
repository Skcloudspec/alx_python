#!/usr/bin/python3
class Square:
    """
    A class that defines a square by its size.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size):
        """
        The constructor for the Square class.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    @property
    def dict_(self):
        """
        Gets the dictionary representation of a Square instance.
        """
        return {'size': self.__size}


# Create a Square object with size 3
mysquare = Square(3)

# Print the type of the object and its dictionary representation
print(type(mysquare))
print(mysquare.dict_)

# Try to access the private __size attribute using the size and __size names
try:
    print(mysquare.size)
except AttributeError as e:
    print(e)

try:
    print(mysquare._Square__size)
except AttributeError as e:
    print(e)

# Create a Square object with size 89
mysquare_2 = Square(89)

# Print the type of the object and its dictionary representation
print(type(mysquare_2))
print(mysquare_2.dict_)

# Try to access the private __size attribute using the size and __size names
try:
    print(mysquare_2.size)
except AttributeError as e:
    print(e)

try:
    print(mysquare_2._Square__size)
except AttributeError as e:
    print(e)
