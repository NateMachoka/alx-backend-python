#!/usr/bin/env python3
"""
returns another function to multiply a float by a given multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the specified multiplier.

    Args:
        multiplier (float): The multiplier to use.

    Returns:
        Callable[[float], float]: multiplies a float by the multiplier.
    """
    def multiplier_func(value: float) -> float:
        """
        Multiplies the given float by the multiplier.

        Args:
            value (float): The float to multiply.

        Returns:
            float: The result of the multiplication.
        """
        return value * multiplier

    return multiplier_func
