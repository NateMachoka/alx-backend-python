#!/usr/bin/env python3
"""
return the sum of a  mixed_list of integers and floats
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and floats.

    Returns:
        float: The sum of the numbers in the list as a float.
    """
    total: float = 0.0
    for n in mxd_lst:
        total += n
    return total
