#!/usr/bin/python3
"""
Defines a class Rectangle using width and height properties
"""


class Rectangle:
    """Representation of a rectangle with the specified 
    width and height attributes"""
    def __init__(self, width=0, height=0):
        """Initializes the state of the rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Accessor method for the private instence property width"""
        return self.__width

    @width.setter
    def width(self, value):
        """assigns the new value private instance attribute width
        checks if the new value is an interger or is not a negative

        Handles: TypeError and ValueError"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets/sets the value for private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """assigns the value for the private instance attribute height
        checks if the new value is an int or not a negative

        Handles: TypeError and ValueError"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
