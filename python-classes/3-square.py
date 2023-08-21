#!/usr/bin/python3
```
"""
This is the documentation for the Square class that defines a square by its size
"""

class Square:
    """
    This class defines a square by its size
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance with a given size

        Args:
            - size (int): the length of a side of the square (default: 0)
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter method for private instance attribute size

        Returns:
            - The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for private instance attribute size

        Args:
            - value (int): the length of a side of the square

        Raises:
            - TypeError: if value is not an integer
            - ValueError: if value is less than 0
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes and returns the area of the square

        Returns:
            - The area of the square
        """
        return self.__size ** 2


# test cases
if __name__ == '__main__':
    mysquare = Square(89)
    print(mysquare.size)  # output: 89
    print(mysquare.area())  # output: 7921
    mysquare.size = 33
    print(mysquare.size)  # output: 33
    print(mysquare.area())  # output: 1089

    mysquare = Square(89)
    print(mysquare.size)  # output: 89

    mysquare = Square()
    print(mysquare.size)  # output: 0

    mysquare = Square(89)
    print(mysquare.size)  # output: 89
    mysquare.size = 33
    print(mysquare.size)  # output: 33

    try:
        mysquare = Square(89)
        print(mysquare.size)  # output: 89
        mysquare.size = "89"
        print(mysquare.size)
    except Exception as e:
        print(e)
        # output: size must be an integer
```
