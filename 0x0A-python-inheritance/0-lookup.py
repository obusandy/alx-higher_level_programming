#!/usr/bin/python3
"""Retrieves and returns a list of all object's attribute.
    Arguments:
        obj: whose attributes are to be listed"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object"""
    return (dir(obj))
