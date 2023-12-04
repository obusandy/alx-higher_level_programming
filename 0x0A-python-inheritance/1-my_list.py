#!/usr/bin/python3
"""Defines inherited built-in list class MyList."""


class MyList(list):
    """inherits from the list and prints in ascending order"""

    def print_sorted(self):
        """Print a list in sorted ascending order without
        interferring with original data."""
        print(sorted(self))
