#!/usr/bin/python3
""" function that defines a rectangle
"""


class Rectangle:
    """ represent class rectangle"""
    def __init__(self, width=0, height=0):
        """ Initializes the rectangles width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Returns: width value
        """
        return self.__width

    @property
    def height(self):
        """ Returns: value of the height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """ Sets the width new value
        Arguments: new Width(int)
        Handles: TypeError and ValueError
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ Sets the height new value
        Arguments: newheight(int)
        Handles:
        TypeError and ValueError for non int
        and negative values
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns: rectangle area
        Width times Height"""
        return self.__width * self.__height

    def perimeter(self):
        """ Returns: perimeter value
        Width by two plus height by two"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """ Returns:
        a str representing the rectangle with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("\n".join(["".join(["#" for indx in range(self.__width)])
                for k in range(self.__height)]))

    def __repr__(self):
        """ Returns:
        str: a string representation of the rectangle with eval.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
