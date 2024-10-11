#!/usr/bin/env python3
"""
function that returns the length of each element in a list of sequences.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple
    contains an element from the list and its length.

    Args:
        lst (Iterable[Sequence]): A list of sequences (e.g., strings, lists).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples.
        Each tuple contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
