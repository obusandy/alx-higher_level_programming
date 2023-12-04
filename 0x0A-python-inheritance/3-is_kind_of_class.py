#!/usr/bin/python3
"""checks if object is belongs to a class
or an inherited class

Args: Obj and class which to compare the object
"""


def is_kind_of_class(obj, a_class):
    """returns true if object is an instance of a class
    or a class it inherits from or false if otherwise
    """
    return (isinstance(obj, a_class))
