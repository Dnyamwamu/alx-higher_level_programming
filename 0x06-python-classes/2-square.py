#!/usr/bin/python3

"""Square: A class that defines a square."""

class Square:
    """Empty class representing a square."""

    def __init__(self, size=0):
        """Initialization method with a private size attribute."""
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
