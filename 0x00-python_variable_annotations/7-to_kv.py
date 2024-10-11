#!/usr/bin/env python3
"""
This module contains a function to create a tuple from a string and a number.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing a string and the square of a number.

    Args:
        k (str): The string key.
        v (Union[int, float]): The integer or float value.

    Returns:
        Tuple[str, float]: A tuple with the string and the square of the value.
    """
    return (k, float(v ** 2))
