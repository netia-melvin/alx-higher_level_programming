#!/usr/bin/python3
# 3-say_my_name.py
# Netia Melvin
"""Definition of a name-printing function."""


def say_my_name(first_name, last_name=""):
    """Print a name.

    Args:
        first_name (str): The first name to printed
        last_name (str): The last name to be printed.
    Raises:
        TypeError: If either of the names are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
