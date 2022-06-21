#!/usr/bin/python3
class Square:
    """Represents a square.
	Attributes: 
	__size(int): size of the side of the square
    Instantiation with size (no type/value verification).
    """

    def __init__(self, size):
        """Initializes the square."""
        self.__size = size
