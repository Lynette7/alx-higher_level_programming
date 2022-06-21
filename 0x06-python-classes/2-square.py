#!/usr/bin/python3
"""Square class definition"""

class Square:
    """Represents a square.
    Attributes:
	__size(int): size of a side of the square
    Instantiation with optional size.
    """

    def __init__(self, size=0):
        """Initializes the square."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
