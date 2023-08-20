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
    
    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2


# Create a Square object with size 3
mysquare = Square(3)

# Calculate its area
print("Area of the square with size {}: {}".format(mysquare._Square__size, mysquare.area()))

# Create a Square object with size 89
mysquare_2 = Square(89)

# Calculate its area
print("Area of the square with size {}: {}".format(mysquare_2._Square__size, mysquare_2.area()))

# Create a Square object with default size (0)
mysquare_3 = Square()

# Calculate its area
print("Area of the square with default size {}: {}".format(mysquare_3._Square__size, mysquare_3.area()))

# Try to create a Square object with a non-integer size
try:
    mysquare_4 = Square("test")
except TypeError as e:
    print(e)

# Try to create a Square object with a negative size
try:
    mysquare_5 = Square(-5)
except ValueError as e:
    print(e)
