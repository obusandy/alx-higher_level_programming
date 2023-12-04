#!/usr/bin/python3
"""Defines or acts as a blueprint for base geometry class."""


class BaseGeometry:
    """this specific class represents base geometry."""

    def area(self):
        """methos not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate if a parameter as a positive integer.

        Args:
            name (str): The name.
            value (int): Th valuee to check.
        Handless:
            TypeError:  value is not an integer.
            ValueError: value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
