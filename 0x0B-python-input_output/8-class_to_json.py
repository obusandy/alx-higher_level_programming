#!/usr/bin/python3
"""
Module: class_to_json

function that converts a Python class object to a dict representation.
"""

def class_to_json(obj):
    """
    Returns the dict representation of a given Python class object.

    Args:
        obj: The instance of the class to be converted.

    Returns:
        dict: A dictionary containing the characteristics.
    """
    return obj.__dict__
