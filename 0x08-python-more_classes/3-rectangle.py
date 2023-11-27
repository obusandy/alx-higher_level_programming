#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle adjustable by:

        Arguments:
            width(int): width
            height(int): height"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Arguments:
            width (int): The width of the new rectangle(0).
            height (int): The height of the new rectangle(0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves the width of the rectangle.
        Returns: width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Assigns a new value to the width of the rectangle.

        Arguments:
            newvalue (int): The width value to set.

        Hnadles:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0(negative).
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the height of the rEctangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Assigns a value to the height of the Rectangle.

        Arguments:
            value (int): The height value to set.

        Handles:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0(negative).
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle.
        Width multiply by height"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle.
        width by two plus height by 2( round the rect.)
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return printable string representation of the Rectangle.

        Returns:
            str:  the rectangle using '#' characters.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for indx in range(self.__height):
            rect.extend(['#' for _ in range(self.__width)])
            if indx != self.__height - 1:
                rect.append("\n")
        return "".join(rect)
