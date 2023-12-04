#!/usr/bin/python3
"""Defines Rectangle which has subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square object."""

    def __init__(self, size):
        """Initializes new square object.

        Args:
            size (int): size of the brand new square.

        Attr:
            __size(interger): stores the size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
