#!/usr/bin/python3
class LockedClass:
    """Defines a completely locked class allowing only the creation of the instance
    attribute which is first name

    Attribut:
    first_name: the first name

    """
    __slots__ = ['first_name']
