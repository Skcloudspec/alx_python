#!/usr/bin/python3
class Square:

    """
    A class Square that defines a square by size.
    """

    def __init__(self, size=0):
        """
        Initializes an instance of the Square class.
        Args:
            size (int): size of the square
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieves the value of size attribute.
        Returns:
            int: The value of size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the value of size attribute.
        Args:
            value (int): The value to set size attribute to.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints a square made of '#' characters to the standard output (stdout).
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)


# Test cases
if __name__ == '__main__':
    """
    Test cases for Square class.
    """
    # Test 1 - my_square = Square(3)
    print("Test 1 - my_square = Square(3)")
    my_square = Square(3)
    my_square.my_print()
    print()

    # Test 2 - my_square = Square(10)
    print("Test 2 - my_square = Square(10)")
    my_square = Square(10)
    my_square.my_print()
    print()

    # Test 3 - my_square = Square(0)
    print("Test 3 - my_square = Square(0)")
    my_square = Square(0)
    my_square.my_print()
    print()
