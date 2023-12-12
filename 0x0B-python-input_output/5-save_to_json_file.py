#!/usr/bin/python3
"""
Module: save_to_json_file

Contains a function that writes content to a text file.
"""


def def save_to_json_file(my_obj, filename):
    """
    Writes content to a specific text file.

    Arguments:
        filename (str): The path to the file.
        my_obj (str): The text to be written on the file.

    Raises:
        Exception: For general errors while opening or writing to the file.
    Returns:
        no of characters
    """

     with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
