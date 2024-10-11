#!/usr/bin/env python3
"""
This module contains a function that safely retrieves a value from a dictionary
returning a default value if the key is not present.
"""
from typing import TypeVar, Union, Mapping, Any


T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, Any], key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary by key. If the key is not present
    returns the default value.

    Args:
        dct (Mapping[Any, Any]): The dictionary to retrieve values from.
        key (Any): The key to look for in the dictionary.
        default (Union[T, None], optional): value to return if the key is not
        found. Defaults to None.

    Returns:
        Union[Any, T]: The value from the dictionary if the key exists,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
