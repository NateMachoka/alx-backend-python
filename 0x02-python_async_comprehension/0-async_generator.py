#!/usr/bin/env python3
"""
Has a coroutine that takes no argument
yields a random number between 1 and 10
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
