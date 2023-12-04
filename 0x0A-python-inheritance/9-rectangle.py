#!/usr/bin/python3
"""Defines the class Rectangle inheriting from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents rectangle object using BaseGeometry."""

    def __init__(self, wdth, hght):
        """Intialize a new Rectangle object.

        Args:
            wdth (int): The width of the new Rectangle.
            hght (int): The height of the new Rectangle.
        """
        super().integer_validator("width", wdth)
        self.__wdth = wdth
        super().integer_validator("height", hght)
        self.__hght = hght

    def area(self):
        """Return the area of the rectangle."""
        return self.__wdth * self.__hght

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        strn = "[" + str(self.__class__.__name__) + "] "
        strn += str(self.__wdth) + "/" + str(self.__hght)
        return strn
