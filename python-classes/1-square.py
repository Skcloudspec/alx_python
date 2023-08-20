#!/usr/bin/python3
class Square:
    """
    Square class represents a square shape.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
            str: A string representing the Square.
        """
        return f"Square(size={self.__size})"

    def area(self):
        """
        Calculates the area of the Square.

        Returns:
            int: The area of the Square.
        """
        return self.__size ** 2


# Correct output - case: mysquare = Square(3)
mysquare = Square(3)
print(type(mysquare))  # <class '__main__.Square'>
print(mysquare.__dict__)  # {'_Square__size': 3}

# Correct output - case: mysquare = Square(89)
mysquare = Square(89)
print(type(mysquare))  # <class '__main__.Square'>
print(mysquare.__dict__)  # {'_Square__size': 89}

# Correct output - case: mysquare = Square()
mysquare = Square()
print(type(mysquare))  # <class '__main__.Square'>
print(mysquare.__dict__)  # {'_Square__size': 0}

# Correct output - case: try: mysquare = Square("3")
try:
    mysquare = Square("3")
    print(type(mysquare))
    print(mysquare.__dict__)
except Exception as e:
    print(e)  # size must be an integer

# Correct output - case: try: mysquare = Square(3.14)
try:
    mysquare = Square(3.14)
    print(type(mysquare))
    print(mysquare.__dict__)
except Exception as e:
    print(e)  # size must be an integer

# Correct output - case: try: mysquare = Square(-89)
try:
    mysquare = Square(-89)
    print(type(mysquare))
    print(mysquare.__dict__)
except Exception as e:
    print(e)  # size must be >= 0
