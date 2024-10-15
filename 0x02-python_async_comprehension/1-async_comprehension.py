#!/usr/bin/env python3
"""
The async_comprehension coroutine handles the collection of 10 random numbers
returns them as a list
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from async_generator using async comprehension.
    """
    result = [i async for i in async_generator()]
    return result
