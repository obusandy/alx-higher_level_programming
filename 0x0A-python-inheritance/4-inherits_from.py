#!/usr/bin/python3
"""checks if object beolongs to a class that
inherited from the specified class
Args: obj and class to check inheritance r/ships
"""


def inherits_from(obj, a_class):
    """Returns true if object is an instance of a class that inherited
    from the specified class; False otherwise
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
