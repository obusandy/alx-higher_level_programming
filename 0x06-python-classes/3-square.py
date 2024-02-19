#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initializes a brand new Square.

        Arguments:
            size (int): The size of the new square.
            handles: Type and Value errors if the value is either
            not an int
            less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and returns area of the square
        Returns: The new square area
        """

        return (self.__size ** 2)
