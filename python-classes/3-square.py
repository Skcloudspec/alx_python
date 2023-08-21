#!/usr/bin/python3
class Square:
    """
    This is a class that represents a square.
    """

    def __init__(self, size=0):
        """
        This method initializes a Square object with a size attribute.
        :param size: An integer representing the size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """
        This method retrieves the size attribute for the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This method sets the size attribute for the square.
        :param value: An integer representing the size of the square.
        :raises ValueError: If value is not an integer or is less than 0.
        """
        if type(value) != int:
            raise ValueError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        This method calculates and returns the area of the square.
        """
        return self.__size ** 2


# Test Case 1
mysquare = Square(89)
print(mysquare.size)  # output: 89
print(mysquare.area())  # output: 7921
mysquare.size = 33
print(mysquare.size)  # output: 33
print(mysquare.area())  # output: 1089

# Test Case 2
mysquare = Square(89)
print(mysquare.size)  # output: 89

# Test Case 3
mysquare = Square()
print(mysquare.size)  # output: 0

# Test Case 4
mysquare = Square(89)
print(mysquare.size)  # output: 89
mysquare.size = 33
print(mysquare.size)  # output: 33

# Test Case 5
try:
    mysquare = Square(89)
    print(mysquare.size)  # output: 89
    mysquare.size = "89"
    print(mysquare.size)
except Exception as e:
    print(e)  # output: size must be an integer
Square = __import__('3-square').Square

my_square = Square(89)
print(my_square.size)
print(my_square.area())
my_square.size = 33
print(my_square.size)
print(my_square.area())
