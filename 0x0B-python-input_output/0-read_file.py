#!/usr/bin/python3
"""
Module: file_reader

which Contains a function that reads content from a file.
"""

def read_file(file_name=""):
    """
    Reads the content from a specific file.

    Arguments:
        file_name (str): The path to the file.

    Raises:
        FileNotFoundErr: If the file is not found, read or opened.
    """

    with open(file_name, encoding="utf-8") as f:
         print(f.read(), end="")
