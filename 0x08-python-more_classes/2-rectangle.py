#!/usr/bin/python3
"""
Defines a class Rectangle with width and height properties
"""


class Rectangle:
    """Representation of a rectangle based on:

    Arguments:
        width(int): width
        height(int): height
    """
    def __init__(self, width=0, height=0):
        """Initializes the new rectangle object"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets the value for the private instance attribute width

        Returns: width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value for the private instance attribute width
        Handles: TypeError and the ValueError"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the value for the private instance attribute height

        Returns: height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value for the private instance attribute height

        Handles: TypeError and the ValueError if not int or not-neg"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle

        which is the value of width multiply by the height"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle

        which is the width by two added to he height by two"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
