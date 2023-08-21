#!/usr/bin/puyhon3
class Square:
    """
    This is a Square class
    """
    def __init__(self, size=0):
        """
        Initialize a new Square object with a given size
        Args:
        - size: an integer representing the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculate the area of the square
        Returns:
        - the area of the square
        """
        return self.__size ** 2


if __name__ == '__main__':
    """
    Test cases for the Square class
    """
    mysquare = Square(3)
    print("Area: {}".format(mysquare.area()))  # output: Area: 9

    mysquare = Square(89)
    print("Area: {}".format(mysquare.area()))  # output: Area: 7921

    mysquare = Square()
    print("Area: {}".format(mysquare.area()))  # output: Area: 0

