#!/usr/bin/python3
"""
a type-annotated function that concatenates string str1 and string str2
returns a concatenated string
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concatenated string.
    """
    return str1 + str2
