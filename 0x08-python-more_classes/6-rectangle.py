#!/usr/bin/python3
""" function that defines a rectangle
"""


class Rectangle:
    """ class rectangle with adjustable width and height"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Initiallization of the original rectangle"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ value of the width
        Returns: width value
        """
        return self.__width

    @property
    def height(self):
        """value of the height
        Returns: height value
        """
        return self.__height

    @width.setter
    def width(self, value):
        """ assigns the new value of the width
        Handles: Type and value Error if:
        not an int or value is less than 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ assigns the new value of the height
        Handles: Type and value Error if:
        not an int or value is less than 0
        """
        if type(value)!= int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns: rectangle's area
        Width times height"""
        return self.__width * self.__height

    def perimeter(self):
        """ Returns: rectangle perimeter
        Height by two plus width by two"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """ Returns: strn of the rectangle with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("\n".join(["".join(["#" for indx in range(self.__width)])
                for k in range(self.__height)]))

    def __repr__(self):
        """ Return: a strn representation of the rectangle for eval
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print bye message if an instance of Rectangle is deleted
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
