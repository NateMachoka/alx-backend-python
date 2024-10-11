#!/usr/bin/env python3
"""
function that returns the first element in a list of sequence
element can be any type
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the sequence if it exists,
    otherwise returns None.

    Args:
        lst (Sequence[Any]): A sequence of elements of unknown type.

    Returns:
        Union[Any, None]: The first element of the sequence or
        None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
