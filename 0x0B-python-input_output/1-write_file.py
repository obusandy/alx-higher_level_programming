#!/usr/bin/python3
"""
Module: write_file

Contains a function that writes content to a text file.
"""

def write_file(file_name="", txt=""):
    """
    Writes content to a specific text file.

    Arguments:
        file_path (str): The path to the file.
        txt (str): The text to be written on the file.

    Raises:
        Exception: For general errors while opening or writing to the file.
    Returns: 
        no of characters
    """
    with open(file_name, "w", encoding="utf-8") as f:
        return f.write(txt)
