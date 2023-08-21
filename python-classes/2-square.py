#!/usr/bin/puyhon3
```
"""
This module defines a Square class that represents a square shape
"""

class Square:
    """
    This class represents a square shape
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance
        Args:
            - size: the size of the square (default: 0)
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Computes the area of the square
        Returns:
            - the area of the square
        """
        return self.__size * self.__size

# create objects and test methods
if __name__ == "__main__":
    mysquare = Square(3)
    print("Area:", mysquare.area())  # output: Area: 9

    mysquare = Square(89)
    print("Area:", mysquare.area())  # output: Area: 7921

    mysquare = Square()
    print("Area:", mysquare.area())  # output: Area: 0
```
