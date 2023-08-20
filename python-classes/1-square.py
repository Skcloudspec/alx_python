#!/usr/bin/python3
class Square:
    """A class that defines a square by its size."""
    def __init__(self, size=0):
        """Initializes a Square instance with an optional size.

        Args:
            size (int): The size of the square (default 0).
        Raises:
            TypeError: If the size argument is not an integer.
            ValueError: If the size argument is negative.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
class Square:
    def __init__(self, size):
        self.__size = size

    def area(self):
        print(Square.area.__doc__)
        return self.__size ** 2
    __doc__ = """
    this is documentation for my class
    """
__doc__ = """
this is documentation for my module
class Square:
    """A class that defines a square by its size."""
    def __init__(self, size=0):
        """Initializes a Square instance with an optional size.

        Args:
            size (int): The size of the square (default 0).
        Raises:
            TypeError: If the size argument is not an integer.
            ValueError: If the size argument is negative.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    
    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square (size times size).
        """
        return self.__size ** 2
