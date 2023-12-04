#!/usr/bin/python3
"""9 rectangle defines a rectangle subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a class square"""

    def __init__(self, size):
        """Initialize a new square object
            Arguments: size, the size of the square

        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
