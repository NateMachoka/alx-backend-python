#!/usr/bin/env python3
"""
function that zooms in on the elements of a tuple by a given factor,
returning a list of repeated elements.
"""

from typing import List, Tuple

def zoom_array(lst: Tuple, factor: int = 2) -> List[int]:
    """
    Zooms in on each element of the given tuple by the specified factor.

    Args:
        lst (Tuple[int, ...]): A tuple of integers to zoom in on.
        factor (int): The number of times to repeat each element. Defaults to 2.

    Returns:
        List[int]: A list containing the zoomed-in elements.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
