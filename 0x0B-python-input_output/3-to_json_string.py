#!/usr/bin/python3
"""
Module:to_json_string

Defines a function that converts a Python object to its JSON representation.
"""

import json



def to_json_string(my_obj):
    """
     Arguments:
        my_obj: The Python object to be converted.

    Returns:
        str: A string containing the JSON representation 


    """
    return json.dumps(my_obj)
