#!/usr/bin/python3
"""Defines the rectangle inheriting properties from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle to be defined using BaseGeometry."""

    def __init__(self, wdth, hght):
        """Intialize a new Rectangle object.

        Args:
            wdth (int): The width of the new rectangle.
            hght (int): The height of the new rectangle.
        """
        self.integer_validator("width", wdth)
        self.__wdth = wdth
        self.integer_validator("height", hght)
        self.__hght = hght
