#!/usr/bin/env python3
"""
A type-annotated function floor which takes a float n as argument
returns the floor of the float
"""

import math


def floor(n: float) -> int:
    """
    Returns the floor of a floating-point number.

    Args:
        n (float): The floating-point number.

    Returns:
        int: The floor of the number.
    """
    return math.floor(n)
