#!/usr/bin/python3
"""
Module: load_from_json_file

Contains a function that loads content to a text file.
"""
import json



def load_from_json_file(filename):
    """
    Writes content to a specific text file.

    Arguments:
        filename (str): The path to the file.


    Raises:
        Exception: For general errors while opening or writing to the file.
    Returns:
        no of characters
    """

    with open(filename) as f:
        return json.load(f)
