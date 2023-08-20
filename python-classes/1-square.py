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
            int: The area of the square (size times size).
        """
        return self.__size ** 2


# Test the Square class
try:
    square1 = Square("3")
    print(type(square1))
    print(square1.__dict__)
except Exception as e:
    print(e)

try:
    square2 = Square(3.14)
    print(type(square2))
    print(square2.__dict__)
except Exception as e:
    print(e)

try:
    square3 = Square(-89)
    print(type(square3))
    print(square3.__dict__)
except Exception as e:
    print(e)

square4 = Square(3)
print(type(square4))
print(square4.__dict__)

square5 = Square()
print(type(square5))
print(square5.__dict__)

print(square4.area())  # Output: 9
