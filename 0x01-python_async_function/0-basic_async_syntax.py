#!/usr/bin/env python3
"""
A module that contains a basic wait_random coroutine
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynch coroutine waits for a random delay between 0 and max_delay seconds.
    Args:
        max_delay (int): Max value for the delay in seconds (default is 10).
    Returns:
        float: The actual random delay waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
