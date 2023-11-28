#!/usr/bin/python3

"""function that defines a locked class"""

class LockedClass:
    """Defines a compltely locked class allowing only the creation of the instance
    attribute which is first name

    Attribut:
    first_name: the first name

    """
    __slots__ = ['first_name']
