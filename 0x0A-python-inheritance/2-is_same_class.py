#!/usr/bin/python3
"""Does a checks to determine if object is an instance of a class"""

def is_same_class(obj, a_class):
    """
    Args: an object and a class to be compared to
    Returns:
    bool: true if object is an instance of the
    class, otherwise false
    """
    return (type(obj) == a_class)
