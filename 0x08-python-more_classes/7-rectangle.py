#!/usr/bin/python3
""" function that defines a rectangle
"""


class Rectangle:
    """ representation of a rectangle
        Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (###): The symbol used for string representation.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialiization of the original rectangle
        Arguments:
            width(int): width
            height(int): height
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ width current value
        Arguments:
        value(int): width value
        Returns: width value
        """
        return self.__width

    @property
    def height(self):
        """ height current value
        Returns: height value
        """
        return self.__height

    @width.setter
    def width(self, value):
        """ assigns the value of the width
        Handles: Type and value error
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ assigns the value of the width
        Handles: TH type an value errors
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns: rectangle area
        width times height"""
        return self.__width * self.__height

    def perimeter(self):
        """ Returns: rectangle perimeter
        Width by two plus height by two"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """returns printable string representation of the rectangle"""
        strn = ""
        if self.__width != 0 and self.__height != 0:
            strn += "\n".join(str(self.print_symbol) * self.__width
                                for k in range(self.__height))
        return strn

    def __repr__(self):
        """ Returns:
        strn: a string representation of the rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Prints bye message when an instance of Rectangle is deleted
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
