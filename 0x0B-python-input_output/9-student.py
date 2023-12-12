#!/usr/bin/python3
"""
Module: init, student

Defines a class student with a method for changing to a dict.
"""

class Student:
    """
    Represents a student.

    Attr:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a brand new Student.

        Arguments:
            first_name (str): The first name ofstudent.
            last_name (str): The last name of student.
            age (int): The age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns:
            dict: A dictionary containing the attributes
        """
        return self.__dict__
