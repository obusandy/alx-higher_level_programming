#!/usr/bin/python3
""" function that defines a rectangle
"""


class Rectangle:
    """ class rectangle with adjustable width and height"""
    def __init__(self, width=0, height=0):
        """ Initialization the formers state of the
        rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrives new width value
        Returns: width value
        """
        return self.__width

    @property
    def height(self):
        """ retrieves new height value
        Returns: height value
        """
        return self.__height

    @width.setter
    def width(self, value):
        """ sets new width value
        Handles: TypeError and ValueError
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ sets new width vale
        Handles: TypeError and ValueError
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns: rectangle area
        Height times Width value"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns: rectangle perimeter
        width by two plus height by two"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """Returns: a printable strn of the rectangle with the character #

        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("\n".join(["".join(["#" for i in range(self.__width)])
                for j in range(self.__height)]))

    def __repr__(self):
        """ Returns: reproduction string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Method: __del__

        Print a bye message when an instance of Rectangle is deleted
        """
        print("Bye rectangle...")
